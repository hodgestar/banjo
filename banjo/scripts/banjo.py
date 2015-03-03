""" Launch Banjo Hero. """

from __future__ import absolute_import

import click
from banjo.engine import Engine


@click.command()
def cli():
    """ Banjo Hero in Pygame. """
    engine = Engine()
    engine.setup()
    try:
        engine.run()
    finally:
        engine.teardown()


if __name__ == "__main__":
    cli()
