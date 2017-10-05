"""Packaging settings."""
from setuptools import Command, find_packages, setup
from src import __version__

setup(
    name = 'Geocoding Proxy',
    version = __version__,
    description = 'A command line tool that returns a longitude and latitude from mutiple geocoding services',
    author = 'Leo Shin',
    author_email = 'leo@sh1n.com',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt', 'requests'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'geocoding_proxy=src.geocoding_proxy:main',
        ],
    }
)