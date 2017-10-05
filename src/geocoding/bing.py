"""
Bing Maps API
"""
from .base import BaseApi

class BingMapsApi(BaseApi):

    @BaseApi.get
    def search(self, keyword):
        if self.response is None or 'resourceSets' not in self.response:
            raise ValueError('No data given')
        location = self.response['resourceSets'][0]['resources'][0]['point']['coordinates']
        return { 'lat' : location[0], 'lng' : location[1] } if len(location) > 1 else None

    def build_get_params(self, *params):
        return { 'q' : params[0] }