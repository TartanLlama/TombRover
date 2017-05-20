
import pygame

from Game import Map
from Static import *



#RogueCanvas class
class RogueCanvas(pygame.Surface):
    """
    A surface onto which the game world is drawn.
    """
    
    def __init__(self, parent, size):
        pygame.Surface.__init__(self, size)
        self.parent = parent
        
        self.using_images = parent.using_images
        self.images = parent.images
        self.player_generator = parent.player_generator
        self.img_size = parent.img_size
    
    def draw(self):
        game_map = self.world.getCurrentMap().getMap()
        
        if len(game_map) > 0 and len(game_map[0]) > 0:
            (width, height) = self.get_size()
            cols = len(game_map)
            rows = len(game_map[0])
            grid_size = self.getGridSize(width, height, rows, cols)
            
            #Finds the player's position in the map, there are better ways to
            #do this, but this works:
            player_found = False
            player_pos = (0, 0)
            x = 0
            for column in game_map:
                y = 0
                for square in column:
                    if not player_found \
                       and self.world.playerHere(square):
                        player_found = True
                        player_pos = ((x + 0.5) * grid_size,
                                      (y + 0.5) * grid_size)
                    y += 1
                x += 1
            
            #Create an inner canvas object to draw the entire game world on to:
            inner_canvas = InnerCanvas(self, grid_size, self.world)
            inner_canvas.draw()
            
            #Calculate the position to draw the inner canvas onto, this is to
            #support scrolling view, so that the RogueCanvas displays only the
            #part of the map which the player is in.
            (x, y) = player_pos
            x = width / 2 - x
            y = height / 2 - y
            
            self.fill(BLACK)
            self.blit(inner_canvas, (x, y))
        
            x = 10
            y = 10
            #Draw messages from the previous turn to the surface:
            for message in self.world.turn_messages:
                message = SMALL_FONT.render(message, True, WHITE, BLACK)
                message.set_colorkey(BLACK)
                self.blit(message, (x, y))
                y += int(SMALL_TEXT_HEIGHT * 1.5)
    
    def getGridSize(self, width, height, rows, cols):
        """
        Helper function to get the size of a square in the grid from the width,
        height, rows and cols.
        """
        grid_width = width/cols
        grid_height = height/rows
        if grid_width < grid_height:
            return 2 * grid_width
        else:
            return 2 * grid_height
    
    #because world is a property which gives the parent's world, world does not
    #have to be updated in this class, only in parent.
    #Same story for all other classes using this technique.
    world = property(lambda self: self.parent.world)
#End of RogueCanvas class



class InnerCanvas(pygame.Surface):
    """
    Draws the entire game world onto one surface.
    """
    
    def __init__(self, parent, square_size, world):
        pygame.Surface.__init__(self,
            (len(world.getCurrentMap().getMap()) * square_size,
            len(world.getCurrentMap().getMap()[0]) * square_size))
        self.grid_size = square_size
        self.parent = parent
        
        self.using_images = parent.using_images
        self.images = parent.images
        self.player_generator = parent.player_generator
        self.img_size = parent.img_size
        
        self.game_map = world.getCurrentMap().getMap()
        self.floor_type = world.getCurrentMap().getFloorType()
        self.wall_type = world.getCurrentMap().getWallType()
        self.world = world
    
    def draw(self):
        #Scale all images to the grid size, only if necessary:
        if self.using_images and self.grid_size != self.img_size:
            self.img_size = self.grid_size
            self.parent.img_size = self.img_size
            for key in self.images:
                self.images[key] = pygame.transform.scale(self.images[key],
                        (self.img_size, self.img_size))
            self.parent.images = self.images
        
        #draw each square in the map:
        x = 0
        for column in self.game_map:
            y = 0
            for square in column:
                self.drawSquare(x, y, square)
                y += 1
            x += 1
    
    
    def drawSquare(self, x, y, square):
        gs = self.grid_size
        #Turning x and y from grid position to pixel position:
        x = x * gs
        y = y * gs
        
        state = square.getState()
        bg_image = pygame.Surface((gs, gs))
        
        #Draw the square's background:
        
        #an undiscovered square:
        if not square.visited or state == Map.Blocked:
            bg_image.fill(BLACK)
        
        #A wall square
        elif state == Map.Wall:
            if square.isInFov():
                if self.using_images:
                    if self.wall_type == 0:
                        bg_image.blit(self.images["wall_visible_1"], (0, 0))
                    else:
                        bg_image.blit(self.images["wall_visible_2"], (0, 0))
                else:
                    bg_image.fill(BROWN)
            else:
                if self.using_images:
                    if self.wall_type == 0:
                        bg_image.blit(self.images["wall_1"], (0, 0))
                    else:
                        bg_image.blit(self.images["wall_2"], (0, 0))
                else:
                    bg_image.fill(DARK_BROWN)
        #A floor square:
        elif state == Map.Floor:
            if square.isInFov():
                if self.using_images:
                    if self.floor_type == 0:
                        bg_image.blit(self.images["floor_visible_1"], (0, 0))
                    else:
                        bg_image.blit(self.images["floor_visible_2"], (0, 0))
                else:
                    bg_image.fill(LIGHT_BLUE)
            else:
                if self.using_images:
                    if self.floor_type == 0:
                        bg_image.blit(self.images["floor_1"], (0, 0))
                    else:
                        bg_image.blit(self.images["floor_2"], (0, 0))
                else:
                    bg_image.fill(DARK_BLUE)
        
        #super-imposing image of player/objects onto background:
        #This only draws the most important item in the square.
        
        #r is the radius of the circle to draw if we are not using images:
        r = gs / 2
        
        #If the player is in the square, draw the player:
        if self.world.playerHere(square):
            if self.using_images:
                player_img = self.player_generator.getPlayerImage(self.world.player,
                                                                  (gs, gs))
                bg_image.blit(player_img, (0, 0))
            else:
                pygame.draw.circle(bg_image, BLUE, (r, r), r)
        #If there is a monster in the square:
        elif square.character != None:
            img_string = getImageString(square.character)
            if square.isInFov():
                if self.using_images and img_string != None:
                    bg_image.blit(self.images[img_string], (0, 0))
                else:
                    pygame.draw.circle(bg_image, RED, (r, r), r)
        #If there are stairs in the square:
        elif square.containsStairs() and square.visited:
            img_string = getImageString(square.stairs, square.isInFov())
            if self.using_images and img_string != None:
                bg_image.blit(self.images[img_string], (0, 0))
            else:
                if square.isInFov():
                    bg_image.fill(ORANGE)
                else:
                    bg_image.fill(DARK_ORANGE)
        #If there are one or more items in the square, draw the first item in
        #the list.
        elif len(square.items) >= 1 and square.isInFov():
            obj = square.items[0]
            img_string = getImageString(obj)
            if self.using_images and img_string != None:
                bg_image.blit(self.images[img_string], (0, 0))
            elif member(obj, GOLD):
                pygame.draw.circle(bg_image, YELLOW, (r, r), r)
            else:
                pygame.draw.circle(bg_image, WHITE, (r, r), r)
        self.blit(bg_image, (x, y))
