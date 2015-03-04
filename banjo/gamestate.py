""" A holder for game state. """


class GameState(object):
    def apply_events(self, events):
        """ Update the game state by applying a list of scene events.

        :param events:
            The list of scene events.

        :returns:
            The new game state.
        """
        return self
