"""
Bing Maps API
"""
from .base import BaseApi

class BingMapsApi(BaseApi):

    def get_geocode(self, keyword):
        response = self.get({'q' : keyword})
        if response is None or 'resourceSets' not in response:
            raise ValueError('No data given')
        location = self.response['resourceSets'][0]['resources'][0]['point']['coordinates']
        return { 'lat' : location[0], 'lng' : location[1] } if len(location) > 1 else None