"""
Base abstract class for API
"""
import json
import requests
import inspect

class BaseApi:
    def __init__(self, endpoint, key):
        self.key = key
        self.endpoint = endpoint


    def _request(func):
        """Decorator for all RESTful method

        Args:
            func (function) : a function to be perform after this decorator

        Returns:
            function
        """
        def _process(self, *args):
            if len(args) == 0:
                return func(self, *args)
            # create a payload with a given key and args
            payload = { 'key' : self.key }
            if type(args[0]) == dict:
                payload.update(args[0])

            request_call = getattr(requests, func.__name__)
            response_data = None
            try:
                response = request_call(self.endpoint, params=payload, timeout=1.0)
                if response.status_code == 200:
                    response_data = response.json()
                    if 'status' in response_data and response_data.status != 'OK':
                        raise Exception(response_data.error_messsage)
                else:
                    raise Exception('API Response error. ' + response.status_code)
            except Exception:
                raise
            finally:
                return func(self, args[0], response_data)
        return _process

    @_request
    def get(self, params=None, response=None):
        return response

    @_request
    def post(self, params=None, response=None):
        return response

    @_request
    def put(self, params=None, response=None):
        return response

    @_request
    def delete(self, params=None, response=None):
        return response

    @_request
    def patch(self, params=None, response=None):
        return response

    def get_geocode(self, keyword):
        raise NotImplementedError('You must implement the get_geocode() method')

    def post_geocode(self, obj):
        raise NotImplementedError('You must implement the post_geocode() method')


