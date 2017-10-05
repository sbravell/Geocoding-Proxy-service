"""
Base abstract class for API
"""
import json
import requests

class BaseApi:
    def __init__(self, endpoint, key):
        self.key = key
        self.response = None
        self.endpoint = endpoint

    @classmethod
    def get(self, f):
        """Decorator for GET method

        Args:
            f (function) : a function to be perform after this decorator

        Returns:
            function
        """
        def _get(self, *args, **kwargs):
            if len(args) == 0:
                return f(self, args)
            # create a payload with a given key and args
            payload = { 'key' : self.key }
            payload.update(self.build_get_params(args))

            try:
                response = requests.get(self.endpoint, params=payload, timeout=1.0)
                if response.status_code == 200:
                    self.response = response.json()
                    if self.response.status != 'OK':
                        raise Exception('API Response error. ' + self.response.error_message)
                else:
                    raise Exception('API Response error. ' + response.status_code)
            except Exception:
                raise
            finally:
                return f(self, args)
        return _get

    def build_get_params(self, *params):
        raise NotImplementedError('You must implement the build_params() method')

    def search(self, keyword):
        raise NotImplementedError('You must implement the search() method')