from settings import *
from support import *
from Timer import Timer
from monster import *
from random import randint, choice
from ui import *
from Item import items


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Ikermon')
        self.clock = pygame.time.Clock()
        self.running = True
        self.importAssets()
        self.playerActive = True
        # groups
        self.allSprites = pygame.sprite.Group()

        # data

        playerMonstersList = ['ArthurKorea', 'Spalacidae', 'MattBush', 'Bat', 'Jorell', 'SigmaMan']
        self.playerMonsters = [Monster(name, self.backSurfs[name]) for name in playerMonstersList]
        self.monster = self.playerMonsters[0]
        self.allSprites.add(self.monster)
        opponentName = choice(list(MONSTER_DATA.keys()))
        self.opponent = Opponent(opponentName, self.frontSurfs[opponentName], self.allSprites)
        playerItemsList = ['TicTac', 'Cleanser', 'ikerSecretSauce']
        self.playerItems = [items(name) for name in playerItemsList]
        self.item = self.playerItems[0]

        
        # ui
        self.ui = UI(self.monster, self.item, self.playerMonsters, self.simpleSurfs, self.getInput, self.playerItems)
        self.opponentUI = opponentUI(self.opponent)

        # timers
        self.timers = {'player end': Timer(1000, func=self.opponentTurn), 'opponent end': Timer(1000, func=self.playerTurn)}

    def getInput(self, state, data):

        if state == 'attack':
            self.applyAttack(self.opponent, data)


        if state == 'switch':
            self.monster.kill()
            self.monster = data
            self.allSprites.add(self.monster)
            self.ui.monster = self.monster


        self.playerActive = False
        self.timers['player end'].activate()

    def applyAttack(self, target, attack):

        print(attack)
        target.health -= 20

    def opponentTurn(self):
        if self.opponent.health <= 0:
            self.playerActive = True
            self.opponent.kill()
            monsterName = choice(list(MONSTER_DATA.keys()))
            self.opponent = Opponent(monsterName, self.frontSurfs[monsterName], self.allSprites)
            self.opponentUI.opponent = self.opponent
            pass
        else:
            attack = choice(self.opponent.abilities)
            self.applyAttack(self.monster, attack)
            self.timers['opponent end'].activate()

    def playerTurn(self):
        self.playerActive = True
        if self.monster.health <= 0:
            availableMonsters = [monster for monster in self.playerMonsters if monster.health > 0]
            if availableMonsters:
                self.monster.kill()
                self.monster = availableMonsters[0]
                self.allSprites.add(self.monster)
                self.ui.monster = self.monster
            else:
                # add swapping to platformer here
                self.running = False
    def updateTimers(self):
        for timer in self.timers.values():
            timer.update()

    def importAssets(self):
        self.backSurfs = folderImporter('../Graphics', 'back')
        self.bgSurfs = folderImporter('../Graphics', 'other')
        self.frontSurfs = folderImporter('../Graphics', 'front')
        self.simpleSurfs = folderImporter('../Graphics', 'simple')

    def drawMonsterFloor(self):
        for sprite in self.allSprites:
            if isinstance(sprite, monsterData):
                floorRect = self.bgSurfs['floor'].get_frect(center=sprite.rect.midbottom + pygame.Vector2(0, -10))
                self.screen.blit(self.bgSurfs['floor'], floorRect)

    def run(self):
        while self.running:
            # dt
            dt = self.clock.tick() / 1000
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.updateTimers()
            self.allSprites.update(dt)
            if self.playerActive:
                self.ui.update()

            # draw
            self.screen.blit(self.bgSurfs['bg'], (0, 0))
            self.drawMonsterFloor()
            self.allSprites.draw(self.screen)
            self.ui.draw()
            self.opponentUI.draw()
            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
