from settings import *
from random import sample


class monsterData:
    def getData(self, name):
        self.element = MONSTER_DATA[name]['element']
        self._health = self.maxHealth = MONSTER_DATA[name]['health']
        self.abilities = sample(list(ABILITIES_DATA.keys()), 4)
        self.name = name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = min(self.maxHealth, max(0, value))


class Monster(pygame.sprite.Sprite, monsterData):
    def __init__(self, name, surf):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_frect(bottomleft=(100, WINDOW_HEIGHT))
        self.getData(name)
        # data

    def __repr__(self):
        return f'{self.name}: {self.health}/{self.maxHealth}'


class Opponent(pygame.sprite.Sprite, monsterData):
    def __init__(self, name, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom=(WINDOW_WIDTH - 250, 300))
        self.getData(name)
