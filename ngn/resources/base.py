""" Base class for resources. """

from ..update_events import UpdateEvent


class Resource(object):
    """ Base class for resources. """
    name = "__undefined__"

    def setup(self):
        pass

    def teardown(self):
        pass

    def apply_event(self, ev):
        """ Apply an update event. """
        handler = getattr(self, 'apply_%s_event' % ev.ev_type)
        handler(**ev.kw)


class ResourceEvent(UpdateEvent):
    """ Base class for resource update events. """

    def __init__(self, ev_type, **kw):
        self.ev_type = ev_type
        self.kw = kw
