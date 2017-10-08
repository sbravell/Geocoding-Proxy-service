from flask import Flask
from app.config import get_config
from app.modules import *
import importlib

class GeocodeProxyAPI:
    """Geocoding proxy"""
    def __init__(self):
        self.services = get_config()
        self.modules = self._load_api_modules()

    def get(self, keyword):
        """With multiple maps api providers, it runs based on a priority setting
        If the primary fails, then automatically retry with a second provider.
        """
        errors = []
        for module in self.modules:
            try:
                data = module.get_geocode(keyword)
                return data
            except Exception as e:
                errors.append(e.message)
                continue
            break
        self._check_errors(errors)

    def post(self, params):
        """Not applicable for `POST` method
        """
        pass

    def _load_api_modules(self):
        """Load all api providers from a configuration file. ( config/config.json )
        And dynamically instantiate it if it's defined in app/modules directory

        Args:
            None

        Returns:
            modules (list)
        """
        modules = []

        try:
            for service in self.services:
                module_object = importlib.import_module('app.modules.{}'.format(service['name']))
                module = getattr(module_object, service['classname'])
                modules.append(module(service['endpoint'], service['key']))
        except Exception:
            raise NotImplementedError('Please implement the API first :' + service['classname'])
        return modules

    def _check_errors(self, errors):
        """Display errors if neither modules work.

        Args:
            modules (list): a list of modules
            errors  (list): a list of errors

        Returns:
            list: a list of modules
        """
        if len(errors) == 0 or len(self.modules) == 0:
            # no errors
            return
        if len(errors) == len(self.modules):
            # both modules have errors
            raise Exception("All API are not available at this moment. Please check your API keys")