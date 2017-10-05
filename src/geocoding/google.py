"""
Google Maps API
"""
from .base import BaseApi

class GoogleMapsApi(BaseApi):

    @BaseApi.get
    def search(self, keyword):
        if self.response is None or 'results' not in self.response:
            raise ValueError('No given data')
        location = self.response['results'][0]['geometry']['location']
        return { str(key): val for key, val in location.items() }

    def build_get_params(self, *params):
        return { 'address' : params[0] }