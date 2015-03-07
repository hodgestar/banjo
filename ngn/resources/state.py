""" A resource for holding game state. """

from .base import Resource, ResourceEvent


class StateResource(Resource):
    """ A resource for holding game state. """
    name = 'state'

    def __init__(self):
        self.state = {}
        self.state['ngn'] = {
            'fps': 0.0,
        }

    def apply_set_event(self, **kw):
        self.state.update(kw)


class StateUpdate(ResourceEvent):
    """ Base class for state events. """
    resource = 'state'
