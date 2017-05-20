from Object import Object
from Constants import *

class Item(Object):
    def __init__(self, x, y, type = ITEM, name = "", gettable = True):
        super(Item, self).__init__(x, y, type)
        self.name = name
        self.gettable = gettable
        self.equipped = False
        
    def getName(self):
        return self.name
        
    def getDescription(self):
        return self.description
        
    def setName(self, name):
        self.name = name
        
    def setDescription(self, description):
        self.description = description
        
    def isGettable(self):
        return self.gettable
