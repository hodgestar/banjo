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

  * SE_i+1 = S_i.update(G_i, PE_i+1)
  * G_i+1 = SE_i+1.apply_state_events(G_i)
  * M_i+1 = SE_i+1.apply_music_events(M_i)
  * S_i+1 = SE_i+1.get_next_state()
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

    def event_loop(self, game):
        clock = pygame.time.Clock()
        scene = game.scenes.current_scene
        fps = 0
        while True:
            pygame_events = pygame.event.get()
            update_events = scene.update(game.state, pygame_events)
            update_events.apply_events(game)
            scene = game.scenes.current_scene

            if scene is None:
                break

            surface = pygame.display.get_surface()
            scene.render(game.state, surface)

            pygame.display.flip()
            msecs = clock.tick(self.max_fps)
            fps = 1000.0 / msecs
            game.state.state['ngn']['fps'] = fps

    def run(self, game):
        self.setup()
        game.setup()
        try:
            self.event_loop(game)
        finally:
            game.teardown()
            self.teardown()
