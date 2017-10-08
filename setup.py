"""Packaging settings."""
from setuptools import Command, find_packages, setup
from app import __version__

setup(
    name = 'Geocoding Proxy with a RESTful API Interface',
    version = __version__,
    description = 'A longitude and latitude from mutiple geocoding services',
    author = 'Leo Shin',
    author_email = 'leo@sh1n.com',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['requests', 'flask'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'geocoding_proxy=app.main:main',
        ],
    }
)