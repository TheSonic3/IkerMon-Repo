import pygame.font
from settings import*
from battle_module import *

class UI:

    def __init__(self, monster, item, playerMonsters, simpleSurfs, getInput, playerItems):
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        self.left = WINDOW_WIDTH/2 - 100
        self.top = WINDOW_HEIGHT/2 + 50
        self.monster = monster
        self.simpleSurfs = simpleSurfs
        self.item = item
        # control
        self.generalOptions = ['attack', 'item', 'switch', 'escape']
        self.generalIndex = {'col': 0, 'row': 0}
        self.attackIndex = {'col': 0, 'row': 0}
        self.state = 'general'
        self.rows, self.cols = 2, 2
        self.visibleMonsters = 4
        self.playerMonsters = playerMonsters
        self.availableMonsters = [monster for monster in self.playerMonsters if monster != self.monster and monster.health > 0]
        self.switchIndex = 0
        self.itemIndex = 0
        self.visibleItems = 4
        self.playerItems = playerItems
        self.availableItems = [item for item in self.playerItems if item.count > 0]
        self.getInput = getInput

    def input(self):
        keys = pygame.key.get_pressed()

        if self.state == 'general':
            self.generalIndex['row'] = (self.generalIndex['row'] + int(keys[pygame.K_s]) - int(keys[pygame.K_w])) % self.rows
            self.generalIndex['col'] = (self.generalIndex['col'] + int(keys[pygame.K_d]) - int(keys[pygame.K_a])) % self.cols
            if keys[pygame.K_SPACE]:
                self.state = self.generalOptions[self.generalIndex['col']+self.generalIndex['row'] * 2]


        elif self.state == 'attack':
            self.attackIndex['row'] = (self.attackIndex['row'] + int(keys[pygame.K_s]) - int(keys[pygame.K_w])) % self.rows
            self.attackIndex['col'] = (self.attackIndex['col'] + int(keys[pygame.K_d]) - int(keys[pygame.K_a])) % self.cols
            if keys[pygame.K_SPACE]:
                attack = self.monster.abilities[self.attackIndex['col'] + self.attackIndex['row'] * 2]
                self.getInput(self.state, attack)
                self.state = 'general'
                self.generalIndex = {'col': 0, 'row': 0}
                self.attackIndex = {'col': 0, 'row': 0}
                self.switchIndex = 0

        elif self.state == 'switch':
            self.switchIndex = (self.switchIndex + int(keys[pygame.K_s]) - int(keys[pygame.K_w])) % len(self.availableMonsters)
            if keys[pygame.K_SPACE]:
                self.getInput(self.state, self.availableMonsters[self.switchIndex])
                self.state = 'general'
                self.generalIndex = {'col': 0, 'row': 0}
                self.attackIndex = {'col': 0, 'row': 0}
                self.switchIndex = 0

        elif self.state == 'item':
            self.itemIndex = (self.itemIndex + int(keys[pygame.K_s]) - int(keys[pygame.K_w])) % len(self.availableItems)
            if keys[pygame.K_SPACE]:
                self.getInput(self.state, self.availableItems[self.itemIndex])
                self.state = 'general'
                self.generalIndex = {'col': 0, 'row': 0}
                self.attackIndex = {'col': 0, 'row': 0}
                self.switchIndex = 0

        elif self.state == 'escape':
            if keys[pygame.K_SPACE]:
                self.getInput(self.state, 'sigma')

        if keys[pygame.K_ESCAPE]:
            self.state = 'general'
            self.generalIndex = {'col': 0, 'row': 0}
            self.attackIndex = {'col': 0, 'row': 0}
            self.switchIndex = 0

    def menu(self, index, options):
        # bg
        rect = pygame.FRect(self.left + 40, self.top+60, 400, 200)
        pygame.draw.rect(self.screen, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.screen, COLORS['gray'], rect, 4, 4)

        # menu

        for col in range(self.cols):
            for row in range(self.rows):
                x = rect.left + rect.width / (self.cols * 2) + (rect.width/self.cols) * col
                y = rect.top + rect.height / (self.rows * 2) + (rect.height/self.rows) * row
                i = col + 2 * row
                color = COLORS['gray'] if col == index['col'] and row == index['row'] else COLORS['black']

                textSurf = self.font.render(options[i], True, color)
                textRect = textSurf.get_frect(center=(x, y))
                self.screen.blit(textSurf, textRect)

    def switch(self):
        rect = pygame.FRect(self.left + 40, self.top - 100 , 400, 400)
        pygame.draw.rect(self.screen, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.screen, COLORS['gray'], rect, 4, 4)

        #menu
        verticalOffset = 0 if self.switchIndex < self.visibleMonsters else -(self.switchIndex - self.visibleMonsters + 1) * rect.height/ self.visibleMonsters
        for i in range(len(self.availableMonsters)):
            x = rect.centerx
            y = rect.top + rect.height / (self.visibleMonsters*2) + rect.height / self.visibleMonsters * i + verticalOffset
            color = COLORS['gray'] if i == self.switchIndex else COLORS['black']
            name = self.availableMonsters[i].name

            simpleSurf = self.simpleSurfs[name]
            simpleRect = simpleSurf.get_frect(center=(x-100, y))

            textSurf = self.font.render(name, True, color)
            textRect = textSurf.get_frect(midleft=(x, y))
            if rect.collidepoint(textRect.center):
                self.screen.blit(textSurf, textRect)
                self.screen.blit(simpleSurf, simpleRect)

    def items(self):
        rect = pygame.FRect(self.left + 40, self.top - 100, 400, 400)
        pygame.draw.rect(self.screen, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.screen, COLORS['gray'], rect, 4, 4)

        verticalOffset = 0 if self.itemIndex < self.visibleItems else -(self.itemIndex - self.visibleItems + 1) * rect.height / self.visibleItems
        for i in range(len(self.availableItems)):
            x = rect.centerx
            y = rect.top + rect.height / (self.visibleItems * 2) + rect.height / self.visibleItems * i + verticalOffset
            color = COLORS['gray'] if i == self.itemIndex else COLORS['black']
            name = self.availableItems[i].name
            count = self.availableItems[i].count

            countSurf = self.font.render(str(f'{count}x'), True, color)
            countRect = countSurf.get_frect(center=(x-100, y))

            textSurf = self.font.render(str(name), True, color)
            textRect = textSurf.get_frect(midleft=(x, y))
            if rect.collidepoint(textRect.center):
                self.screen.blit(textSurf, textRect)
                self.screen.blit(countSurf, countRect)

    def updateItems(self):
        self.availableItems = [item for item in self.playerItems if item.count > 0]

        #menu

    def stats(self):
        rect = pygame.FRect(self.left-450, self.top-200, 250, 80)
        pygame.draw.rect(self.screen, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.screen, COLORS['gray'], rect, 4, 4)

        #data
        nameSurf = self.font.render(self.monster.name, True, COLORS['black'])
        nameRect = nameSurf.get_frect(topleft=rect.topleft + pygame.Vector2(rect.width* 0.05, 12))
        self.screen.blit(nameSurf, nameRect)

        #healthbar
        healthRect = pygame.FRect(nameRect.left, nameRect.bottom + 10, rect.width * 0.9, 20)
        pygame.draw.rect(self.screen, COLORS['gray'], healthRect)
        self.drawBar(healthRect, self.monster.health, self.monster.maxHealth)

    def drawBar(self, rect, value, maxValue):
        ratio = rect.width / maxValue
        progressRect = pygame.FRect(rect.topleft, (value * ratio, rect.height))
        pygame.draw.rect(self.screen, COLORS['red'], progressRect)

    def update(self):
        self.input()
        self.availableMonsters = [monster for monster in self.playerMonsters if monster != self.monster and monster.health > 0 ]

    def draw(self):
        match self.state:
            case 'general': self.menu(self.generalIndex, self.generalOptions)
            case 'attack': self.menu(self.attackIndex, self.monster.abilities)
            case 'switch': self.switch()
            case 'item': self.items()
        if self.state != 'switch':
            self.stats()


class opponentUI:

    def __init__(self, monster):

        self.opponent = monster
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        #bg
        rect = pygame.FRect((0, 0), (250, 80)).move_to(midleft =(500, self.opponent.rect.centery))
        pygame.draw.rect(self.screen, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.screen, COLORS['gray'], rect, 4, 4)

        nameSurf = self.font.render(self.opponent.name, True, COLORS['black'])
        nameRect = nameSurf.get_frect(topleft=rect.topleft + pygame.Vector2(rect.width * 0.05, 12))
        self.screen.blit(nameSurf, nameRect)

        #health
        healthRect = pygame.FRect(nameRect.left, nameRect.bottom + 10, rect.width * 0.9, 20)
        ratio = healthRect.width / self.opponent.maxHealth
        progressRect = pygame.FRect(healthRect.topleft, (self.opponent.health * ratio, healthRect.height))
        pygame.draw.rect(self.screen, COLORS['gray'], healthRect)
        pygame.draw.rect(self.screen, COLORS['red'], progressRect)