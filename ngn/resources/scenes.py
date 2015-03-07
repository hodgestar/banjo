""" A resource for holding the scenes that make up a game. """

from .base import Resource, ResourceEvent


class ScenesResource(Resource):
    """ A resource for holding the scenes that make up a game. """
    name = 'scenes'

    def __init__(self):
        self.current_scene = None
        self.scenes = {}

    def add(self, scene):
        self.scenes[scene.name] = scene

    def apply_scene_change_event(self, scene):
        if scene is None:
            self.current_scene = None
        else:
            self.current_scene = self.scenes[scene]


class ScenesUpdate(ResourceEvent):
    """ Base class for scenes events. """
    resource = 'scenes'


class SceneChange(ScenesUpdate):
    def __init__(self, scene):
        super(SceneChange, self).__init__('scene_change', scene=scene)
