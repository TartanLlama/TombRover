
import pygame

from Game import Map
from Static import *


#MiniMap class
class Sidebar(pygame.Surface):
    """
    SideBar class: an information display for the player to be drawn on one
    side of the screen.
    """
    
    #Constructor
    def __init__(self, parent, height):
        pygame.Surface.__init__(self, (SIDEBAR_WIDTH, height))
        
        self.using_images = parent.using_images
        self.images = parent.images
        self.img_size = parent.img_size
        
        self.parent = parent
        self.mini_map = MiniMap(self)
        self.mini_map_pos = (BORDER_SIZE, BORDER_SIZE)
        self.data_area = DataArea(self, height - SIDEBAR_WIDTH - 2 * BORDER_SIZE)
        self.data_area_pos = (BORDER_SIZE, SIDEBAR_WIDTH + BORDER_SIZE)
        
        if self.using_images:
            border_tile_1 = self.images["wall_visible_1"].copy()
            border_tile_2 = self.images["wall_visible_2"].copy()
            self.border_tile_1 = \
                pygame.transform.scale(border_tile_1,
                                       (BORDER_SIZE, BORDER_SIZE))
            self.border_tile_2 = \
                pygame.transform.scale(border_tile_2,
                                       (BORDER_SIZE, BORDER_SIZE))
    #End of Constructor
    
    def scroll(self, up=True):
        """
        Used to scroll through the sidebar's list display.
        """
        #set list depending on what it happening in the world:
        if self.parent.waiting["pickup"]:
            list = self.data_area.square_listing
        elif self.parent.waiting["load"]:
            list = self.data_area.file_list
        else:
            list = self.data_area.inventory
        
        if up:
            list.scrollUp()
        else:
            list.scrollDown()
    
    def draw(self):
        self.mini_map.draw()
        self.data_area.draw()
        
        if self.using_images:
            self.drawBorders()
        else:
            self.fill(DARK_GREY)
        
        self.blit(self.mini_map, self.mini_map_pos)
        self.blit(self.data_area, self.data_area_pos)
    
    def drawBorders(self):
        """
        Helper function used to draw borders around sidebar elements data area,
        and mini-map.
        """
        minimap_height = self.mini_map.get_height() + BORDER_SIZE * 2
        for x in xrange(0, self.get_width(), BORDER_SIZE):
            self.blit(self.border_tile_1, (x, 0))
            self.blit(self.border_tile_1, (x, minimap_height - BORDER_SIZE))
        for y in xrange(0, self.get_width(), BORDER_SIZE):
            self.blit(self.border_tile_1, (0, y))
            self.blit(self.border_tile_1, (self.get_width() - BORDER_SIZE, y))
        
        for x in xrange(0, self.get_width(), BORDER_SIZE):
            self.blit(self.border_tile_2, (x, minimap_height))
            self.blit(self.border_tile_2, (x, self.get_height() - BORDER_SIZE))
        for y in xrange(minimap_height, self.get_height(), BORDER_SIZE):
            self.blit(self.border_tile_2, (0, y))
            self.blit(self.border_tile_2, (self.get_width() - BORDER_SIZE, y))
    
    world = property(lambda self: self.parent.world)
    displayMessage = property(lambda self: self.data_area.displayMessage)
#End of MiniMap class



#DataArea class
class DataArea(pygame.Surface):
    """
    DataArea class - purpose is to serve as an area for miscellaneous pieces of
    data.
    """
    
    def __init__(self, parent, height):
        pygame.Surface.__init__(self, (SIDEBAR_WIDTH - 2*BORDER_SIZE, height))
        
        self.using_images = parent.using_images
        self.images = parent.images
        self.img_size = parent.img_size
        self.parent = parent
        
        #function to get the player's health is world.getPlayerHp, function to
        #get experience is world.getPlayerExperience.
        self.health_bar = ProgressBar(self.world.getPlayerHp,
                                      DARK_GREEN, DARK_RED, YELLOW, "Health: ")
        self.xp_bar = ProgressBar(self.world.getPlayerExperience,
                                  DARK_GREEN, BLACK, WHITE, "Xp: ")
        
        
        #Uses higher order functions to allow ItemList class to be highly
        #flexible
        self.inventory = ItemList(self, 
                                  (lambda : self.world.getPlayerInv()),
                                  (lambda :
                                      str(len(self.world.getPlayerInv()))
                                      + "/"
                                      + str(self.world.getMaxInv())),
                                  (lambda : self.world.getMaxInv()))
        self.square_listing = ItemList(self,
                                       (lambda :
                                           self.world.getPlayerTile().
                                               getItemsDictionary()),
                                       (lambda :
                                           str(len(self.world.getPlayerTile().
                                                      getItemsDictionary()))
                                           + " items in tile"),
                                       (lambda : 26))
        self.monster_list = ItemList(self,
                                     (lambda : self.world.getMonsterFov()),
                                     (lambda :
                                         str(len(self.world.getMonsterFov()))
                                         + " monsters in range"),
                                     (lambda : 26))
        self.file_list = ItemList(self,
                                  (lambda: parent.parent.file_list),
                                  (lambda : str(len(parent.parent.file_list))
                                            + " files"),
                                  (lambda : 26))
        
        bs = BORDER_SIZE
        th = TEXT_HEIGHT
        
        self.health_bar_pos = (bs, bs)
        self.level_pos = (bs, 2 * bs + self.health_bar.get_height())
        self.xp_bar_pos = (bs, 3 * bs + self.health_bar.get_height() + th)
        self.gold_pos = (bs, 4 * bs + self.health_bar.get_height() + 2 * th)
        self.gold_text_pos = (bs * 2 + 32, 4 * bs + self.health_bar.get_height() + 2 * th + (32 - th) / 2)
        self.dungeon_level_pos = (bs, 5 * bs + self.health_bar.get_height() + 2 * th + 32)
        self.message_pos = (bs, 6 * bs + self.health_bar.get_height() + 3 * th + 32)
        self.list_pos = (bs, 7 * bs + self.health_bar.get_height() + 4 * th + 32)
        
        self.displaying_message = False
        self.message = ""
        
        if self.using_images:
            gold = self.images["gold"].copy()
            gold = pygame.transform.scale(gold, (32, 32))
            self.gold_img = gold
    
    def displayMessage(self, message):
        self.displaying_message = True
        self.message = message
    
    def draw(self):
        self.fill(BEIGE)
        
        self.health_bar.draw()
        self.blit(self.health_bar, self.health_bar_pos)
        
        level = "Level " + str(self.world.getPlayerLevel())
        level = FONT.render(level, True, BLACK, BEIGE)
        self.blit(level, self.level_pos)
        
        self.xp_bar.draw()
        self.blit(self.xp_bar, self.xp_bar_pos)
        
        
        if self.using_images:
            self.blit(self.gold_img, self.gold_pos)
        gold = str(self.world.getPlayerGold()) + " gold."
        gold = FONT.render(gold, True, BLACK, BEIGE)
        self.blit(gold, self.gold_text_pos)
        
        dungeon_level = "Dungeon Level: " + str(self.world.current_map + 1)
        dungeon_level = FONT.render(dungeon_level, True, BLACK, BEIGE)
        self.blit(dungeon_level, self.dungeon_level_pos)
        
        
        #Dictionary to say if we are waiting for the player to make a choice
        waiting = self.parent.parent.waiting
        
        if waiting["pickup"]:
            text = "Items in square:"
        elif waiting["ranged"]:
            text = "Attack which monster?"
        elif waiting["armour"]:
            text = "Choose armour:"
        elif waiting["weapon"]:
            text = "Choose weapon:"
        elif waiting["drop"]:
            text = "Drop which item?"
        elif waiting["food"]:
            text = "Choose food:"
        elif waiting["quaff"]:
            text = "Choose potion:"
        elif waiting["load"]:
            text = "Choose file:"
        elif self.displaying_message:
            text = self.message
            self.displaying_message = False
        else:
            text = "Inventory:"
        text = FONT.render(text, True, BLACK, BEIGE)
        self.blit(text, self.message_pos)
        
        if waiting["pickup"]:
            list = self.square_listing
        elif waiting["ranged"]:
            list = self.monster_list
        elif waiting["load"]:
            list = self.file_list
        else:
            list = self.inventory
        list.draw()
        self.blit(list, self.list_pos)
    
    world = property(lambda self: self.parent.world)
#End of DataArea class



#Inventory class
class ItemList(pygame.Surface):
    
    def __init__(self, parent, getList, stringFunction, maxFunction):
        pygame.Surface.__init__(self, (SIDEBAR_WIDTH - 4 * BORDER_SIZE,
                                       7 * SMALL_TEXT_HEIGHT + 4))
        
        self.using_images = parent.using_images
        if self.using_images:
            #on construction, copy and scale all images to fit in the item list
            keys = [key for key in parent.images]
            images = [pygame.transform.scale(
                          parent.images[key],
                          (SMALL_TEXT_HEIGHT - 2, SMALL_TEXT_HEIGHT - 2))
                      for key in parent.images]
            self.images = {}
            for key, image in zip(keys, images):
                self.images[key] = image
            self.img_size = SMALL_TEXT_HEIGHT - 2
        
        #functions to get various pieces of data:
        self.getList = getList
        self.stringFunction = stringFunction
        self.maxFunction = maxFunction
        
        self.parent = parent
        self.position = 0
    
    def scrollUp(self):
        if self.position > 0:
            self.position -= 1
    
    def scrollDown(self):
        max = self.maxFunction()
        if self.position < max - 5:
            self.position += 1
    
    def draw(self):
        self.fill(BLACK)
        
        #list of items to display:
        item_list = self.getList()
        #number of items:
        items = len(item_list)
        #maximum number of items:
        space = self.maxFunction()
        
        if self.position == 0:
            minus_colour = GREY
        else:
            minus_colour = WHITE
        if self.position + 5 >= space - 1:
            plus_colour = GREY
        else:
            plus_colour = WHITE
        plus = SMALL_FONT.render("+ " + self.stringFunction() + " +",
                                 True, plus_colour, BLACK)
        minus = SMALL_FONT.render("- " + self.stringFunction() + " -",
                                  True, minus_colour, BLACK)
        (x, y, w, h) = plus.get_rect()
        x = (self.get_width() - w) / 2
        y = 2 + (SMALL_TEXT_HEIGHT - h) / 2
        self.blit(minus, (x, y))
        self.blit(plus, (x, self.get_height() - (y + h)))
        
        i = self.position
        symbol = ALPHABET[i]
        colour = WHITE
        for y in range(2 + SMALL_TEXT_HEIGHT,
                       self.get_height() - 2 - SMALL_TEXT_HEIGHT,
                       SMALL_TEXT_HEIGHT):
            #drawing the background for this rectangle.
            pygame.draw.rect(self, colour, (2, y, self.get_width()-4,
                             SMALL_TEXT_HEIGHT))
                             
            if i < space:
                symbol = ALPHABET[i]
                if symbol in item_list:
                    obj = item_list[symbol]
                    try:
                        #Most objects this class is used for have a getName
                        #attribute, however this allows flexibility.
                        name = obj.getName()
                    except AttributeError:
                        name = str(obj)
                    try:
                        #uses exception handling in case this is an object
                        #without this attribute.
                        equipped = obj.equipped * "*"
                    except AttributeError:
                        equipped = ""
                    text = symbol + ") " + name + equipped
                    try:
                        #Try to draw the image to the screen, if the object
                        #does not have an image to draw, handle the error
                        #by ignoring it.
                        if self.using_images:
                            img = getImageString(obj)
                            if img in self.images:
                                img = self.images[img]
                                self.blit(img, (self.get_width() - 4
                                                - SMALL_TEXT_HEIGHT, y + 2))
                    except AttributeError:
                        pass
                else:
                    text = symbol + ") Empty"
                text = SMALL_FONT.render(text, True, BLACK, colour)
                text.set_colorkey(colour)
                self.blit(text, (2, y))
                i += 1
            if colour == WHITE:
                colour = BEIGE
            else:
                colour = WHITE
    
    
    world = property(lambda self: self.parent.world)
#End of Inventory class


#ProgressBar class
class ProgressBar(pygame.Surface):
    """
    ProgressBar class - a bar displaying a percentage.
    """
    
    def __init__(self, function, colour_1, colour_2, text_colour, message):
        pygame.Surface.__init__(self, (SIDEBAR_WIDTH - 4 * BORDER_SIZE,
                                       TEXT_HEIGHT))
        self.function = function
        self.colour_1 = colour_1
        self.colour_2 = colour_2
        self.text_colour = text_colour
        (r, g, b, a) = self.text_colour
        self.text_antialiase = (r / 2, g / 2, b / 2, a)
        self.message = message
        self.border = 2
    
    def draw(self):
        b = self.border
        
        self.fill(BLACK)
        try:
            #use exception handling to behave differently when the function
            #returns different types of values. This is to support an xp
            #progress bar as well as a health bar.
            (current, max) = self.function()
            value = current
            out_of = max
        except ValueError:
            (previous, current, max) = self.function()
            value = current
            out_of = max
            max = max - previous
            current = current - previous
        length = self.get_width() - b * 2
        
        length_per_point = float(length) / max
        pygame.draw.rect(self, self.colour_2,
                         (b, b, int(length_per_point * max),
                          TEXT_HEIGHT - 2 * b))
        pygame.draw.rect(self, self.colour_1,
                         (b, b, int(length_per_point * current),
                          TEXT_HEIGHT - 2 * b))
        
        text = self.message + str(value) + "/" + str(out_of)
        text = FONT.render(text, True, self.text_colour, self.text_antialiase)
        text.set_colorkey(self.text_antialiase)
        (x, y, w, h) = text.get_rect()
        x = (self.get_width() - w) / 2
        y = (self.get_height() - h) / 2
        
        self.blit(text, (x, y, w, h))
#End of ProgressBar class


#MiniMap class
class MiniMap(pygame.Surface):
    """
    MiniMap - draws a strategy game style mini-map.
    This works in a very similar (albeit simpler) way to the RogueCanvas
    class.
    """
    
    #Constructor
    def __init__(self, parent):
        pygame.Surface.__init__(self, (SIDEBAR_WIDTH - 2 * BORDER_SIZE,
                                       SIDEBAR_WIDTH - 2 * BORDER_SIZE))
        self.parent = parent
    #End of Constructor
    
    def draw(self):
        self.fill(BLACK)
        game_map = self.world.getCurrentMap().getMap()
        
        if len(game_map) > 0 and len(game_map[0]) > 0:
            if len(game_map) > len(game_map[0]):
                self.square_size = self.get_width() / len(game_map)
            else:
                self.square_size = self.get_height() / len(game_map[0])
            self.start_x = (self.get_width() - self.square_size *
                            len(game_map)) / 2
            self.start_y = self.start_x
            x = 0
            for column in game_map:
                y = 0
                for square in column:
                    self.drawSquare(x, y, square)
                    y += 1
                x += 1
    
    def drawSquare(self, x, y, square):
        gs = self.square_size
        x = self.start_x + x * gs
        y = self.start_y + y * gs
        
        state = square.getState()
        bg_image = pygame.Surface((gs, gs))
        
        if not square.visited or state == Map.Blocked:
            bg_image.fill(BLACK)
        elif state == Map.Wall:
            if square.isInFov():
                bg_image.fill(BROWN)
            else:
                bg_image.fill(DARK_BROWN)
        elif state == Map.Floor:
            if square.isInFov():
                bg_image.fill(LIGHT_BLUE)
            else:
                bg_image.fill(DARK_BLUE)
        
        r = gs / 2
        #super-imposing circle for player/objects onto background
        if self.world.playerHere(square):
            pygame.draw.circle(bg_image, BLUE, (r, r), r)
        elif square.character != None:
            if square.isInFov() and member(square.character, MONSTER):
                pygame.draw.circle(bg_image, RED, (r, r), r)
        elif square.containsStairs() and square.visited:
            pygame.draw.circle(bg_image, GREEN, (r, r), r)
        elif len(square.items) >= 1 and square.isInFov():
            obj = square.items[0]
            if member(obj, ITEM):
                if member(obj, GOLD):
                    pygame.draw.circle(bg_image, YELLOW, (r, r), r)
                else:
                    pygame.draw.circle(bg_image, WHITE, (r, r), r)
        
        self.blit(bg_image, (x, y))
    
    world = property(lambda self: self.parent.world)
#End of MiniMap class
