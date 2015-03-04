""" Banjo game loop.

A game loop may be seen as a function ``f: W_i -> W_i+1`` that updates the
World (W_i) from time t_i to time t_i+1.

The World at t_i may be broken down into:

  * a screen to display images on (D_i)
  * speakers to play music via (M_i)
  * the game state (G_i)
  * the current scene within the game (S_i)

Given a set of Pygame events PE_i+1 that have occurred between t_i and t_i+1
we define ``f`` using:

  * S_i+1, SE_i+1 = S_i.update(G_i, PE_i+1)
  * G_i+1 = G_i.apply_state_events(SE_i+1)
  * M_i+1 = M_i.apply_music_events(SE_i+1)
  * D_i+1 = S_i+1.render(G_i+1)

where SE_i+1 is a list of scene events generated in the transition from S_i
to S_i+1.
"""

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

    def run(self, scene, gamestate):
        clock = pygame.time.Clock()
        while True:
            pygame_events = pygame.event.get()
            scene, scene_events = scene.update(gamestate, pygame_events)
            gamestate = gamestate.apply_events(scene_events)
            # music = music.apply_events(scene_events)
            surface = pygame.display.get_surface()
            scene.render(gamestate, surface)

            # TODO: replace this with a scene event
            for ev in pygame_events:
                if ev.type == pygame.locals.QUIT:
                    return
                elif ev.type == pygame.locals.KEYDOWN:
                    if ev.key == pygame.locals.K_ESCAPE:
                        return

            pygame.display.flip()
            # TODO: store fps on the gamestate
            fps = 1000.0 / clock.tick(self.max_fps)
