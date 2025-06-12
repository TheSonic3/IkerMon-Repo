import pygame
from os.path import join
from os import walk
from pytmx.util_pygame import load_pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
FRAMERATE = 60
ANIMATION_SPEED = 6
BGCOLOR = 'light blue'

COLORS = {
    'black': '#000000',
    'red': '#ee1a0f',
    'gray': 'gray',
    'white': '#ffffff',

}

MONSTER_DATA = {
    'ArthurKorea': {'element': 'fire', 'health': 90, 'armour': 4},
    'Chrome': {'element': 'water', 'health': 90, 'armour': 2},
    'MattBush': {'element': 'plant', 'health': 90, 'armour': 4},
    'SigmaMan': {'element': 'normal', 'health': 90, 'armour': 6},
    'Spalacidae': {'element': 'plant', 'health': 90, 'armour': 10},
    'Bat': {'element': 'flying', 'health': 90, 'armour': 4},
    'Jorell': {'element': 'black', 'health': 90, 'armour': 6},
}

ABILITIES_DATA = {
    'scratch': {'damage': 20, 'element': 'normal', 'animation': 'scratch'},
    'spark': {'damage': 35, 'element': 'fire', 'animation': 'fire'},
    'nuke': {'damage': 50, 'element': 'fire', 'animation': 'explosion'},
    'splash': {'damage': 30, 'element': 'water', 'animation': 'splash'},
    'shards': {'damage': 50, 'element': 'water', 'animation': 'ice'},
    'spiral': {'damage': 40, 'element': 'plant', 'animation': 'green'}
}

ELEMENT_DATA = {
    'fire': {'water': 0.5, 'plant': 2, 'fire': 1, 'normal': 1, 'flying': 1, 'black': 0.5},
    'water': {'water': 1, 'plant': 0.5, 'fire': 2, 'normal': 1, 'flying': 0.5, 'black': 2},
    'plant': {'water': 2, 'plant': 1, 'fire': 0.5, 'normal': 1, 'flying': 1, 'black': 1},
    'normal': {'water': 1, 'plant': 1, 'fire': 1, 'normal': 1, 'flying': 1, 'black': 0.5},
    'flying': {'water': 1, 'plant': 2, 'fire': 0.5, 'normal': 1, 'flying': 1, 'black': 1},
    'black': {'water': 0.5, 'plant': 1, 'fire': 2, 'normal': 2, 'flying': 1, 'black': 1},
}

ITEM_DATA = {
    'TicTac': {'amount': 5, 'max': 99, 'heal': 15, 'cleanse': 0},
    'ikerSecretSauce': {'amount': 3, 'max': 99, 'heal': 50, 'cleanse': 1},
    'Cleanser': {'amount': 5, 'max': 99, 'heal': 0, 'cleanse': 1},

}