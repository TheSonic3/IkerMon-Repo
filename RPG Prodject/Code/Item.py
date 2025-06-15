from settings import *

class items:
    def __init__(self, name):
        self.name = name
        self.count = ITEM_DATA[name]['amount']


