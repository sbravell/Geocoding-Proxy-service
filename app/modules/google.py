"""
Google Maps API
"""
from .base import BaseApi

class GoogleMapsApi(BaseApi):

    def get_geocode(self, keyword):
        response = self.get({'address' : keyword})
        if response is None or 'results' not in response:
            raise ValueError('No given data')
        location = response['results'][0]['geometry']['location']
        return { str(key): val for key, val in location.items() }