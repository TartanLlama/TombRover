
import pygame
from pygame.locals import *
import sys
import time
import pickle
import os
import os.path

from Game.Objects.CharacterClass import *
from Game.Objects import Player
from Game import World
import RogueCanvas
from Static import *
import Sidebar

#Initialise PyGame:
pygame.init()



def start():
    rw = RogueWindow()
    rw.handleEvents()



###############################################################################
#RogueWindow class - manages the player's interaction with the game.
###############################################################################

class RogueWindow():
    """
    Manages the player's interaction with the game.
    Handles control listening and display.
    """
    
    ###########################################################################
    #Constructor: to initialise the RogueWindow
    ###########################################################################
    
    def __init__(self):
        self.world = None
        
        #Load textures needed by the game:
        self.img_size = -1
        #supports plain colour graphics if textures are unavailable:
        try:
            self.images = loadImages()
            self.player_generator = PlayerGenerator()
            self.using_images = True
            
            icon = self.images["gold"].copy()
            pygame.display.set_icon(icon)
        except Exception as e:
            print e
            self.images = None
            self.player_generator = None
            self.using_images = False
        
        #Take first mode, as this is generally the screen's default resolution:
        self.resolution = pygame.display.list_modes()[0]
        self.window = pygame.display.set_mode(self.resolution, FULLSCREEN, 32)
        self.screen = pygame.display.get_surface()
        
        #File list is list of save files:
        self.getFileList()
        
        #Make mouse cursor invisible:
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("Tomb Rover")
        
        self.playing_game = False
        self.start_screen = StartScreen(self, self.resolution)
        self.end_screen = None
        self.game_over = False
        
        #Draw UI for the first time:
        self.draw()
    
    ###########################################################################
    #End of constructor
    ###########################################################################
    
    
    
    ###########################################################################
    #Draw code - to draw components of the game to the screen
    ###########################################################################
    
    def draw(self):
        """
        Draws components of the game to the screen.
        """
        if self.playing_game:
            self.sidebar.draw()
            self.rogue_canvas.draw()
            
            self.screen.blit(self.sidebar, self.sidebar_pos)
            self.screen.blit(self.rogue_canvas, self.rogue_canvas_pos)
        elif not self.game_over:
            self.start_screen.draw()
            self.screen.blit(self.start_screen, (0, 0))
        else:
            self.end_screen.draw()
            self.screen.blit(self.end_screen, (0, 0))
        pygame.display.flip()
    
    def drawSidebarOnly(self):
        """
        Doesn't draw the RogueCanvas, only draws sidebar.
        For use if something changes which isn't in the game world.
        """
        if self.playing_game:
            self.sidebar.draw()
            
            self.screen.blit(self.sidebar, self.sidebar_pos)
            
        pygame.display.flip()
    
    ###########################################################################
    #End of draw code.
    ###########################################################################
    
    
    
    ###########################################################################
    #Saving/loading/initialisation code
    ###########################################################################
    
    def initialiseGame(self):
        """
        Initialises all UI elements for gameplay, assumes world is already
        initialised.
        """
        
        (width, height) = self.resolution
        #Creat the game world object - stores the game state
        
        #Sidebar is a constant width, rogue canvas fills remaining space
        rogue_canvas_size = (width - SIDEBAR_WIDTH, height)
        self.rogue_canvas_pos = (SIDEBAR_WIDTH, 0)
        self.sidebar_pos = (0, 0)
        self.sidebar = Sidebar.Sidebar(self, height)
        self.rogue_canvas = RogueCanvas.RogueCanvas(self, rogue_canvas_size)
        
        #If the UI is waiting for the player to make a decision of some kind:
        self.waiting = { "armour" : False,
                         "weapon" : False,
                         "food"   : False,
                         "drop"   : False,
                         "pickup" : False,
                         "ranged" : False,
                         "quaff"  : False,
                         "load"   : False  }
        #Movement in various directions:
        self.moving = (False, False, False, False)
        
        self.playing_game = True
        self.game_over = False
        
        RogueWindow.displayMessage = property(lambda self: self.sidebar.displayMessage)
        
        self.draw()
    
    def saveGame(self):
        """
        Save the current game world to "Saves\timeAndDate.dsav"
        """
        try:
            if not os.path.exists("Saves"):
                os.mkdir("Saves")
            #time and date, e.g. 2010-12-7_22:04:15
            time_string = time.strftime("%Y-%m-%d_%H-%M-%S")
            f = open("Saves/" + time_string + ".dsav", "wb")
            #Can't save game while world is generating a map, checkMapGenerated
            #blocks until this is completed.
            self.world.checkMapGenerated()
            #Save the world to f in binary format
            pickle.dump(self.world, f, 1)
            f.close()
            self.displayMessage("Saved data.")
        except IOError:
            self.displayMessage("Could not save data.")
    
    def loadGame(self, filename):
        """
        Loads Saves\filename.dsav, and if succesful, replaces the current game
        world with the loaded one.
        """
        try:
            f = open("Saves/" + filename + ".dsav", "rb")
            world = pickle.load(f)
            self.world = world
            self.initialiseGame()
            self.displayMessage("Loaded data.")
            self.draw()
        except (IOError, pickle.PickleError):
            self.displayMessage("Could not load data.")
            self.draw()
    
    def getFileList(self):
        """
        Sets the variable "file_list" to a list of filenames in the Saves
        directory.
        """
        try:
            files = os.listdir("Saves")
            files = [f for f in files if f[len(f)-4:] == "dsav"]
            #Reverse list so later files are at the front:
            files = sorted(files, reverse=True)
            file_dictionary = {}
            i = 0
            for letter in ALPHABET:
                if i >= len(files):
                    break
                file_dictionary[letter] = files[i][:len(f)-5]
                i += 1
            self.file_list = file_dictionary
        except (IOError, OSError):
            self.file_list = {}
    
    ###########################################################################
    #End of saving and loading code.
    ###########################################################################
    
    
    
    ###########################################################################
    #Event handling code: for control listening and user input
    ###########################################################################
    
    
    #handleEvents method
    def handleEvents(self):
        """
        handleEvents: must be called after RogueWindow creation to start the
        event listen/respond loop.
        """
        while True:
            
            if self.playing_game and not self.game_over:
                
                #check player death:
                if self.world.playerDead():
                    self.playing_game = False
                    self.game_over = True
                    self.end_screen = EndScreen(self.resolution, self,
                                                self.world.player,
                                                self.world.getScore(),
                                                self.world.getPlayerLevel(),
                                                self.world.getPlayerGold(),
                                                self.world.current_map + 1)
                    self.draw()
                else:
                    self.performMovement()
            
            #Handle list of events:
            events = pygame.event.get()
            for event in events:
                
                if event.type == QUIT or (event.type == KEYDOWN and \
                                          event.key == K_ESCAPE):
                    sys.exit(0)
                
                elif self.playing_game and not self.game_over:
                    if event.type == KEYDOWN:
                        key = event.key
                        #keys pressed while the current key was pressed:
                        keys_pressed = pygame.key.get_pressed()
                        #(draw_sbar, draw_world) - what we have to draw
                        (draw_sbar, draw_world) = self.keyDown(key,
                                                               keys_pressed)
                        if draw_world:
                            self.draw()
                        elif draw_sbar:
                            self.drawSidebarOnly()
                    
                    #Key up events are less important, merely change variables
                    #used by performMovement
                    elif event.type == KEYUP:
                        key = event.key
                        self.keyUp(key)
                elif not self.playing_game and not self.game_over:
                    #Game has not started yet, player is in options menu
                    if event.type == KEYDOWN:
                        if self.start_screen.loading_game:
                            if event.key in KEYCODE_DICT:
                                key = KEYCODE_DICT[event.key]
                                if key in self.file_list:
                                    self.loadGame(self.file_list[key])
                            elif event.key == K_BACKSPACE:
                                self.start_screen.back()
                                self.draw()
                        else:
                            if event.key == K_f:
                                self.world = World.World(fighter)
                                self.initialiseGame()
                            elif event.key == K_r:
                                self.world = World.World(ranger)
                                self.initialiseGame()
                            elif event.key == K_t:
                                self.world = World.World(thief)
                                self.initialiseGame()
                            elif event.key == K_l:
                                self.start_screen.loading_game = True
                                self.getFileList()
                                self.draw()
                else:
                    #Game is over, player has died
                    if event.type == KEYDOWN and event.key == K_RETURN:
                        end_screen = None
                        self.game_over = False
                        self.playing_game = False
                        self.draw()
    #end of handleEvents method
    
    
    #performMovement method
    def performMovement(self):
        """
        Used to make the player move.
        Includes basic timing to attempt to ensure that this method takes the
        same amount of time no matter what.
        """
        #perform movement, including basic timing:
        (up, down, left, right) = self.moving
        if up or down or left or right:
            x_dist = 0
            y_dist = 0
            #don't allow left and right movement at the same time, etc.
            if left and not right:
                x_dist = -1
            elif right and not left:
                x_dist = 1
            if down and not up:
                y_dist = 1
            elif up and not down:
                y_dist = -1
            if x_dist != 0 or y_dist != 0:
                #Timing elements to compensate for delay in drawing to the
                #screen every time the player moves, attempts to ensure
                #that there will always be MOVE_TIME seconds between each
                #move.
                start_time = time.clock()
                self.world.movePlayer(x_dist, y_dist)
                self.draw()
                time_taken = time.clock() - start_time
                sleep_time = MOVE_TIME - time_taken
                if sleep_time > 0:
                    time.sleep(sleep_time)
    #End of performMovement
    
    
    #keyDown method
    def keyDown(self, key, keys_pressed):
        """
        For when the user presses a key down.
        returns (draw_sidebar, draw_world) to inform what, if anything, needs
        to be re-drawn.
        """
        
        #If the user is scrolling through the sidebar list:
        if key == K_PLUS or key == K_EQUALS or key == K_PAGEDOWN:
            self.sidebar.scroll(False)
            return (True, False)
        elif key == K_MINUS or key == K_UNDERSCORE or key == K_PAGEUP:
            self.sidebar.scroll(True)
            return (True, False)
        
        #If the user interface is waiting for the player to make a choice:
        elif reduce((lambda x, y: x or y), [self.waiting[k] for k in self.waiting]):
            self.makeChoice(key)
            return (True, True)
        
        else:
            #movement controls:
            (up, down, left, right) = self.moving
            if key == K_LEFT or key == K_h:
                left = True
            elif key == K_RIGHT or key == K_l:
                right = True
            elif key == K_DOWN or key == K_j:
                down = True
            elif key == K_UP or key == K_k:
                up = True
            elif key == K_y:
                up = True
                left = True
            elif key == K_u:
                up = True
                right = True
            elif key == K_b:
                down = True
                left = True
            elif key == K_n:
                down = True
                right = True
            self.moving = (up, down, left, right)
            #end of movement controls
            
            #Saving and loading the game
            #load = ctrl+o
            #save = ctrl+s
            #new game = ctrl+n
            if key == K_s and (keys_pressed[K_LCTRL] or \
                                 keys_pressed[K_RCTRL]):
                self.saveGame()
                return (True, False)
            elif key == K_o and (keys_pressed[K_LCTRL] or \
                                 keys_pressed[K_RCTRL]):
                self.getFileList()
                self.waiting["load"] = True
                return (True, False)
            elif key == K_n and (keys_pressed[K_LCTRL] or \
                                 keys_pressed[K_RCTRL]):
                self.playing_game = False
                self.draw()
            
            # < or > for going up or down stairs:
            elif key == K_PERIOD and (keys_pressed[K_LSHIFT] or \
                                      keys_pressed[K_RSHIFT]):
                self.world.goDown()
                return (True, True)
            elif key == K_COMMA and (keys_pressed[K_LSHIFT] or \
                                     keys_pressed[K_RSHIFT]):
                self.world.goUp()
                return (True, True)
            
            # '.' key for waiting one turn:
            elif key == K_PERIOD:
                self.world.movePlayer(0, 0)
                return (True, True)
            
            # w or W for wielding a weapon or wearing armour.
            elif key == K_w:
                if keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]:
                    self.waiting["armour"] = True
                    return (True, True)
                else:
                    if self.world.playerWielding():
                        self.world.turn_messages = []
                        self.world.turn_messages.append('Already holding weapon')
                    else:
                        self.waiting["weapon"] = True
                return (True, True)
            
            # e for eating food:
            elif key == K_e:
                self.waiting["food"] = True
                return (True, True)
            
            # d for dropping an item:
            elif key == K_d:
                self.waiting["drop"] = True
                return (True, True)
            
            # t to unwield a weapon, T to take off armour:
            elif key == K_t:
                if keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]:
                    self.world.playerTakeOff()
                    return (True, True)
                else:
                    self.world.playerUnwield()
                    return (True, True)
            
            # ',' for picking an item up:
            elif key == K_COMMA:
                self.waiting["pickup"] = True
                return (True, True)
            
            # f for a ranged attack, if the player is wielding a bow:
            elif key == K_f and self.world.playerWieldingRanged():
                self.waiting["ranged"] = True
                return (True, True)
            
            # q to 'quaff' a potion:
            elif key == K_q:
                self.waiting["quaff"] = True
                return (True, True)
        
        #If we've reached this point of the method, return false to say that
        #nothing important has been updated, and nothing needs to be drawn.
        return (False, False)
    #End of keyDown method
    
    
    #makeChoice method
    def makeChoice(self, key):
        """
        For when the UI is waiting for the player to make a choice.
        Upon an invalid choice, the UI will stop waiting.
        """
        #if key is in KEYCODE_DICT, it is alphabetical
        if key in KEYCODE_DICT:
            #KEYCODE_DICT gives alphabetical character
            symbol = KEYCODE_DICT[key]
            
            #Checks what the player is supposed to choose:
            if self.waiting["armour"]:
                self.world.playerWear(symbol)
            elif self.waiting["weapon"]:
                self.world.playerWield(symbol)
            elif self.waiting["food"]:
                self.world.playerEat(symbol)
            elif self.waiting["drop"]:
                self.world.playerDrop(symbol)
            elif self.waiting["quaff"]:
                self.world.playerQuaff(symbol)
            elif self.waiting["pickup"]:
                tile = self.world.getPlayerTile()
                items = tile.getItemsDictionary()
                if symbol in items:
                    self.world.pickUpItem(items[symbol])
            elif self.waiting["ranged"]:
                items = self.world.getMonsterFov()
                if symbol in items:
                    self.world.fireAtMonster(items[symbol])
            elif self.waiting["load"]:
                if symbol in self.file_list:
                    self.loadGame(self.file_list[symbol])
        
        #Sets all self.waiting values to false, we aren't waiting any more.
        for key in self.waiting:
            self.waiting[key] = False
    #end of makeChoice method
    
    
    #keyUp method
    def keyUp(self, key):
        """
        For when the player has had a movement key held down, and releases it.
        Key up events are unimportant for all controls except movement.
        """
        (up, down, left, right) = self.moving
        if key == K_LEFT or key == K_h:
            left = False
        elif key == K_RIGHT or key == K_l:
           right = False
        elif key == K_DOWN or key == K_j:
           down = False
        elif key == K_UP or key == K_k:
            up = False
        elif key == K_y:
            up = False
            left = False
        elif key == K_u:
            up = False
            right = False
        elif key == K_b:
            down = False
            left = False
        elif key == K_n:
            down = False
            right = False
        self.moving = (up, down, left, right)
    #End of keyUp method
    
    ###########################################################################
    #End of event handling code
    ###########################################################################
    
    
    #For convenience, so can do "self.displayMessage"
    displayMessage = property(lambda self: self.start_screen.displayMessage)

###############################################################################
#End of RogueWindow class
###############################################################################






###############################################################################
#Start and end screens, both of these are uncommented and quite messy, but
#these are nothing interesting and were simply built to serve a purpose.
###############################################################################

class StartScreen(pygame.Surface):
    
    def __init__(self, parent, size):
        pygame.Surface.__init__(self, size)
        self.parent = parent
        self.images = parent.images
        self.using_images = parent.using_images
        self.player_generator = parent.player_generator
        self.loading_game = False
        if self.using_images:
            thief_img = Player.Player(thief)
            thief_img = self.player_generator.getPlayerImage(thief_img, (64, 64))
            ranger_img = Player.Player(ranger)
            ranger_img = self.player_generator.getPlayerImage(ranger_img, (64, 64))
            fighter_img = Player.Player(fighter)
            fighter_img = self.player_generator.getPlayerImage(fighter_img, (64, 64))
            
            self.images = {
                "gold" : self.images["gold"].copy(),
                "wall" : self.images["wall_visible_1"].copy()
            }
            for key in self.images:
                self.images[key] = pygame.transform.scale(self.images[key], (32, 32))
            
            self.images["gold"] = pygame.transform.scale(self.images["gold"], (64, 64))
            self.images["thief"] = thief_img
            self.images["fighter"] = fighter_img
            self.images["ranger"] = ranger_img
        
        self.load_text = "Choose a file to load:"
    
    def displayMessage(self, message):
        self.load_text = message
    
    def back(self):
        self.loading_game = False
    
    def draw(self):
        self.fill(BLACK)
        
        gs = 32
        cols = 25
        rows = 20
        w = cols * gs
        h = rows * gs
        
        x = (self.get_width() - w) / 2
        y = (self.get_height() - h) / 2
        pygame.draw.rect(self, DARK_GREY, (x, y, w, h))
        
        if self.using_images:
            for i in range(x, x + w, gs):
                for j in range(y, y + h, gs):
                    self.blit(self.images["wall"], (i, j))
        
        if self.loading_game:
            self.drawLoadingScreen(gs, x, y, w, h)
        else:
            self.drawMenu(gs, x, y, w, h)
    
    def drawLoadingScreen(self, gs, x, y, w, h):
        self.parent.getFileList()
        gap = 10
        pygame.draw.rect(self, BLACK, (x + gs, y + gs, w - 2 * gs, h - 2 * gs))
        
        x = x + gs + gap
        y = y + gs + gap
        file_list = self.parent.file_list
        title = BIG_FONT.render(self.load_text, True, GOLD_COL, BLACK)
        self.blit(title, (x, y))
        
        y += TEXT_HEIGHT
        
        i = 0
        for key in file_list:
            y += TEXT_HEIGHT + gap
            text = "  " + ALPHABET[i] + ") " + file_list[key]
            text = FONT.render(text, True, GOLD_COL, BLACK)
            self.blit(text, (x, y))
            i += 1
            if i == 13:
                y -= 13 * (TEXT_HEIGHT + gap)
                x += (w - 2 * gs) / 2
        
        x = (self.get_width() - w) / 2 + gs + gap
        y = self.get_height() - (self.get_height() - h) / 2 - gs - gap - BIG_TEXT_HEIGHT
        backspace_text = BIG_FONT.render("<- Backspace to return", True, GOLD_COL, BLACK)
        self.blit(backspace_text, (x, y))
        
        self.load_text = "Choose a file to load:"
    
    def drawMenu(self, gs, x, y, w, h):
        text = [("L)", "Load game"), ("F)", "Play as fighter"),
                ("R)", "Play as ranger"), ("T)", "Play as thief")]
        if self.using_images:
            images = [self.images["gold"], self.images["fighter"],
                      self.images["ranger"], self.images["thief"]]
        
        pygame.draw.rect(self, BLACK, (x + gs, y + gs, w - 2 * gs, gs * 2))
        welcome = BIG_FONT.render("Welcome to Tomb Rover!", True, GOLD_COL, BLACK)
        self.blit(welcome, (x + 2 * gs, y + gs + (2 * gs - BIG_TEXT_HEIGHT) / 2))
        
        for i in [y + 4 * gs, y + 8 * gs, y + 12 * gs, y + 16 * gs]:
            pygame.draw.rect(self, BLACK, (x + gs, i, w - 2 * gs, gs * 3))
                
        index = 0
        for i in [y + 4 * gs, y + 8 * gs, y + 12 * gs, y + 16 * gs]:
            (symbol, description) = text[index]
            symbol = BIG_FONT.render(symbol, True, GOLD_COL, BLACK)
            description = BIG_FONT.render(description, True, GOLD_COL, BLACK)
            symbol.set_colorkey(DARK_BLUE)
            description.set_colorkey(DARK_BLUE)
            if self.using_images:
                image = images[index]
                self.blit(symbol, (x + 2 * gs, i + ((3 * gs) - BIG_TEXT_HEIGHT) / 2))
                if image != None:
                    self.blit(image, (x + 21 * gs, i + gs / 2))
            self.blit(description, (x + 192, i + ((3 * gs) - BIG_TEXT_HEIGHT) / 2))
            index += 1



class EndScreen(pygame.Surface):
    
    def __init__(self, size, parent, player, score, level, gold, dungeon_level):
        pygame.Surface.__init__(self, size)
        
        self.grid_size = self.get_height() / 30
        if (self.get_height() / 30) > (self.get_width() / 15):
            self.grid_size = self.get_width() / 15
        
        self.start_x = (self.get_width() - (15 * self.grid_size)) / 2
        self.start_y = (self.get_height() - (30 * self.grid_size)) / 2
        
        self.using_images = parent.using_images
        if self.using_images:
            player_size = (self.grid_size * 2, self.grid_size * 2)
            self.player_img = parent.player_generator.getPlayerImage(player,
                                                                     player_size)
            self.wall_img = parent.images["wall_1"].copy()
            self.wall_img = pygame.transform.scale(self.wall_img, 
                                                   (self.grid_size,
                                                    self.grid_size))
        
        self.score = score
        self.level = level
        self.gold = gold
        self.dungeon_level = dungeon_level
        self.time = time.strftime("%d %B %Y")
    
    def draw(self):
        self.fill(BLACK)
        
        for x in xrange(15):
            x = self.start_x + x * self.grid_size
            for y in xrange(10, 30):
                y = self.start_y + y * self.grid_size
                if self.using_images:
                    self.blit(self.wall_img, (x, y))
                else:
                    pygame.draw.rect(self, DARK_GREY, (x, y, self.grid_size,
                                                       self.grid_size))
        
        for y in xrange(7, 10):
            width = 15 - 2 * (10 - y)
            y = self.start_y + y * self.grid_size
            for x in xrange((15 - width) / 2, (15 + width) / 2):
                x = self.start_x + x * self.grid_size
                if self.using_images:
                    self.blit(self.wall_img, (x, y))
                else:
                    pygame.draw.rect(self, DARK_GREY, (x, y, self. grid_size,
                                                       self.grid_size))
        
        x = self.start_x + int(6.5 * self.grid_size)
        y = self.start_y + int(7.5 * self.grid_size)
        
        if self.using_images:
            self.blit(self.player_img, (x, y))
        
        died_text = "Died " + self.time + ","
        died_text = FONT.render(died_text, True, WHITE, BLACK)
        died_text.set_colorkey(BLACK)
        died_text_2 = "at level " + str(self.level) + "."
        died_text_2 = FONT.render(died_text_2, True, WHITE, BLACK)
        died_text_2.set_colorkey(BLACK)
        dungeon_level_text = "Reached dungeon level " + str(self.dungeon_level)
        dungeon_level_text = FONT.render(dungeon_level_text, True, WHITE,
                                             BLACK)
        dungeon_level_text.set_colorkey(BLACK)
        score_text = "Score: " + str(self.score)
        score_text = FONT.render(score_text, True, WHITE, BLACK)
        score_text.set_colorkey(BLACK)
        gold_text = "Gold: " + str(self.gold)
        gold_text = FONT.render(gold_text, True, WHITE, BLACK)
        gold_text.set_colorkey(BLACK)
        continue_text = "Press enter to continue"
        continue_text = FONT.render(continue_text, True, WHITE, BLACK)
        continue_text.set_colorkey(BLACK)
        
        x = (self.get_width() - died_text.get_width()) / 2
        y = self.start_y + 11 * self.grid_size
        self.blit(died_text, (x, y))
        
        x = (self.get_width() - died_text_2.get_width()) / 2
        y += TEXT_HEIGHT
        self.blit(died_text_2, (x, y))
        
        x = (self.get_width() - dungeon_level_text.get_width()) / 2
        y += 2 * TEXT_HEIGHT
        self.blit(dungeon_level_text, (x, y))
        
        x = (self.get_width() - score_text.get_width()) / 2
        y += 2 * TEXT_HEIGHT
        self.blit(score_text, (x, y))
        
        x = (self.get_width() - gold_text.get_width()) / 2
        y += 2 * TEXT_HEIGHT
        self.blit(gold_text, (x, y))
        
        x = (self.get_width() - continue_text.get_width()) / 2
        y += 3 * TEXT_HEIGHT
        self.blit(continue_text, (x, y))


###############################################################################
#End of start/end screens.
###############################################################################
        


