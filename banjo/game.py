""" Banjo game description. """

from ngn import Game

from .scenes.menu import MenuScene


class BanjoGame(Game):
    def __init__(self):
        super(BanjoGame, self).__init__()
        self.initial_scene = self.add_scene(MenuScene())
