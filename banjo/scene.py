""" A generic game scene. """


class Scenes(object):
    """ A set of scenes in a game. """
    def __init__(self):
        self._scenes = {}

    def add_scene(self, name, scene):
        self._scenes[name] = scene

    def get_scene(self, name):
        return self._scenes[name]


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
        scene_events = SceneEvents(self)
        return scene_events

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


class SceneEvents(object):
    """ A list of events generated by a scene update. """

    def __init__(self, scene):
        self.scene = scene
        self.music_events = []
        self.games_events = []
        self.next_scene_name = None
        self.quit_game = False

    def set_next_scene(self, scene_name):
        self.next_scene_name = scene_name

    def set_quit_game(self, end=True):
        self.quit_game = end

    def add_music_event(self, *args, **kw):
        self.music_events.append(MusicEvent(*args, **kw))

    def add_game_event(self, *args, **kw):
        self.game_events.append(GameEvent(*args, **kw))

    def apply_state_events(self, gamestate):
        return gamestate

    def apply_music_events(self, music):
        return music

    def get_next_scene(self, scenes):
        if self.next_scene_name is None:
            return self.scene
        return scenes[self.next_scene_name]


class MusicEvent(object):
    pass


class GameEvent(object):
    pass
