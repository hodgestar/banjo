""" Launch Banjo Hero. """

from __future__ import absolute_import

import click
from ngn import Engine
from banjo.game import BanjoGame


@click.command()
def cli():
    """ Banjo Hero in Pygame. """
    engine = Engine()
    game = BanjoGame()
    engine.run(game)


if __name__ == "__main__":
    cli()
