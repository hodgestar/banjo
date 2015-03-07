""" A generic game scene. """

import pygame.locals

from .update_events import UpdateEvents
from .resources.scenes import SceneChange


class Scene(object):
    """ A generic game scene.

    A scene should be immutable once created.
    """

    def setup(self):
        pass

    def teardown(self):
        pass

    def _check_for_quit(self, ev, scene_events):
        if ((ev.type == pygame.locals.QUIT) or
            (ev.type == pygame.locals.KEYDOWN and
             ev.key == pygame.locals.K_ESCAPE)):
            scene_events.add_event(SceneChange(None))
            return True
        return False

    def update(self, gamestate, pygame_events):
        """ Update the gamestate based on recent pygame events.

        :param gamestate:
            The current gamestate.

        :param pygame_events:
            A list of recent pygame events.

        :returns:
            The new scene and a list of scene events,
            (new_scene, scene_events).
        """
        scene_events = UpdateEvents()
        for ev in pygame_events:
            if not self.handle_event(ev, gamestate, scene_events):
                break
        return scene_events

    def handle_event(self, ev, gamestate, scene_events):
        if self._check_for_quit(ev, scene_events):
            return False
        return True

    def render(self, gamestate, surface):
        """ Render the gamestate to the surface.

        :param gamestate:
            The current gamestate.

        :param surface:
            The surface to render to.

        :returns:
            None.
        """
        pass
