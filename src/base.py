"""
Base class for command line
"""
from config import get_config

class Base:
    """A base command."""
    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        self.services = get_config()

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself')

