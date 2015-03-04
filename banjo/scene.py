""" A generic game scene. """


class Scene(object):
    """ A generic game scene.

    A scene should be immutable once created.
    """

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
        return self, []

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
