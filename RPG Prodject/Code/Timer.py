from settings import *

class Timer:
    def __init__(self, duration, repeat=False, autostart=False, func=None):
        self.duration = duration
        self.startTime = 0
        self.active = False
        self.repeat = repeat
        self.func = func

        if autostart:
            self.activate()

    def __bool__(self):
        return self.active

    def activate(self):
        self.active = True
        self.startTime = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.startTime = 0
        if self.repeat:
            self.activate()

    def update(self):
        if self.active:
            if pygame.time.get_ticks() - self.startTime >= self.duration:
                if self.func and self.startTime != 0: self.func()
                self.deactivate()