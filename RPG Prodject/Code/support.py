from settings import *


def folderImporter(*path):
    surfs = {}
    for folderPath, _, fileNames in walk(join(*path)):
        for fileName in fileNames:
            fullPath = join(folderPath, fileName)
            surfs[fileName.split('.')[0]] = pygame.image.load(fullPath).convert_alpha()
    return surfs




