"""
Geocoding Proxy

Usage:
  geocoding_proxy --address=<address> [-h] [--version]

Options:
  -a <address> --address=<address>  Show both a longitude and latitude by an address
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  geocoding_proxy -a "425 Market St #8, San Francisco, CA"
"""
from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION

def main():
    """
    Read all options of commands with docopt
    http://docopt.org/
    """
    options = docopt(__doc__, version=VERSION)
    _command_run(options)

def _command_run(options):
    import geocoding
    module = getattr(geocoding, 'proxy')
    commands = getmembers(module, isclass)
    command = [command[1] for command in commands if command[0] == 'Proxy'][0]
    command = command(options)
    command.run()