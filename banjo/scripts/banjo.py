""" Launch Banjo Hero. """

from __future__ import absolute_import

import click
from banjo.engine import Engine
from banjo.gamestate import GameState
from banjo.scene import Scene


@click.command()
def cli():
    """ Banjo Hero in Pygame. """
    engine = Engine()
    scene = Scene()
    gamestate = GameState()
    engine.setup()
    try:
        engine.run(scene, gamestate)
    finally:
        engine.teardown()


if __name__ == "__main__":
    cli()
