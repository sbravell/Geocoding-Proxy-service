from src.base import Base
from .api import ApiManager
from .google import GoogleMapsApi
from .bing import BingMapsApi

class Proxy(Base):
    """Geocoding proxy"""

    def run(self):
        print self.get_geocoding_data()

    def get_geocoding_data(self):
        """With multiple maps api providers, it runs based on a priority setting
        If the primary fails, then automatically retry with a second provider.
        """
        modules = self._get_api_services()
        errors = []
        for module in modules:
            try:
                data = module.search(self.options['--address'])
                return data
            except Exception as e:
                errors.append(e.message)
                continue
            break
        self._check_errors(modules, errors)

    def _get_api_services(self):
        """Get all api providers from a configuration file. ( config/config.json )

        Args:
            None

        Returns:
            modules (list)
        """
        modules = []
        for service in self.services:
            if service['name'] == 'google-maps':
                modules.append(
                    GoogleMapsApi(
                        service['endpoint'],
                        service['key']
                    )
                )
            elif service['name'] == 'bing-maps':
                modules.append(
                    BingMapsApi(
                        service['endpoint'],
                        service['key']
                    )
                )
            else:
                raise NotImplementedError('Unknown service name :' + service['name'])
        return modules

    def _check_errors(self, modules, errors):
        """Display errors if neither modules work.

        Args:
            modules (list): a list of modules
            errors  (list): a list of errors

        Returns:
            list: a list of modules
        """
        if len(errors) == 0 or len(modules) == 0:
            # no errors
            return
        if len(errors) == len(modules):
            # both modules have errors
            raise Exception("All API are not available at this moment. Please check your API keys")