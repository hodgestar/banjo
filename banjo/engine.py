""" Banjo game loop. """

from __future__ import absolute_import

import pygame
import pygame.locals


class Engine(object):
    """ Banjo's game engine. """

    # TODO: replace with wiring's dependency injection
    DEFAULTS = {
        'screen_size': (800, 600),
        'window_name': 'Banjo Hero',
        'max_fps': 60,
    }

    def __init__(self, **opts):
        for name, default in self.DEFAULTS.items():
            setattr(self, name, opts.get(name, default))

    def setup(self):
        pygame.display.init()
        pygame.font.init()
        pygame.display.set_mode(
            self.screen_size, pygame.locals.SWSURFACE)
        pygame.display.set_caption(self.window_name)

    def teardown(self):
        pass

    def run(self):
        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            for ev in events:
                if ev.type == pygame.locals.QUIT:
                    return
                elif ev.type == pygame.locals.KEYDOWN:
                    if ev.key == pygame.locals.K_ESCAPE:
                        return
            # TODO: construct scene
            # TODO: render scene
            #    scene is a list of renderable events
            #    event types:
            #        render on surface
            #        play sound
            #        emit pygame event
            #    surface = pygame.display.get_surface()
            pygame.display.flip()
            fps = 1000.0 / clock.tick(self.max_fps)
