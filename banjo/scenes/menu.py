""" Menu scene. """

import pygame

from ngn import Scene


class MenuScene(Scene):
    """ Banjo menu. """

    name = 'menu'

    def setup(self):
        font_name = pygame.font.get_default_font()
        self._font = pygame.font.SysFont(font_name, 40)
        self._color = (127, 127, 255)

    def render(self, gamestate, surface):
        surface.fill((0, 0, 0))
        fps = gamestate.state['ngn']['fps']
        fps_surface = self._font.render("FPS: %g" % fps, True, self._color)
        surface.blit(fps_surface, (0, 0))
