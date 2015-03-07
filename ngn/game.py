""" A class describing a game. """

from .resources.scenes import ScenesResource
from .resources.state import StateResource


class Game(object):

    initial_scene = None

    def __init__(self):
        self.resources = {}
        self.scenes = self.add_resource(ScenesResource())
        self.state = self.add_resource(StateResource())

    def add_resource(self, resource):
        self.resources[resource.name] = resource
        return resource

    def add_scene(self, scene):
        self.scenes.add(scene)
        return scene

    def setup(self):
        if self.initial_scene is not None:
            self.scenes.current_scene = self.initial_scene
        for resource in self.resources.itervalues():
            resource.setup()
        for scene in self.scenes.scenes.itervalues():
            scene.setup()

    def teardown(self):
        for resource in self.resources.itervalues():
            resource.teardown()
        for scene in self.scenes.scenes.itervalues():
            scene.teardown()
