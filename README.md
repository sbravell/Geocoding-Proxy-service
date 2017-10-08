# Geocoding Proxy Service
   Provide RESTful Interface to find a longitude and latitude by an address

# Supporting Geocoding services
- [Google Maps Services](https://developers.google.com/maps/)
- [Bing Maps Services](https://www.bingmapsportal.com/)

# Not supporting Geocoding service
- [deprecated] : [Yahoo BOSS Geo Services](https://developer.yahoo.com/boss/geo/)

# How to run the server
* Supports both Python 2.7 and 3.*
* Install dependencies
```
sudo pip install --upgrade pip
pip install virtualenv
virtualenv python
source python/bin/activate
```
* Run requirement packages
 * Required packages : `requests`, 'flask'
```
pip install -e .
```
* Configuration
  * config/config.json
  * With a priority value, it can be a primary or secondary.
```json
{
  "services" : [
    {
        "name"     : "google",
        "classname": "GoogleMapsApi",
        "endpoint" : "https://maps.googleapis.com/maps/api/geocode/json}",
        "key"      : "[Your Google Maps API Key]",
        "priority" : 1
    },
    {
        "name"     : "bing",
        "classname": "BingMapsApi",
        "endpoint" : "https://dev.virtualearth.net/REST/v1/Locations",
        "key"      : "[Your Bing Maps API Key]",
        "priority" : 0.9
    }
  ]
}
```
* Run RESTful API Interface
```
Usage:
  geocoding_proxy
```

# RESTful Interface
* `[GET /api/v1.0/geocode/<address>]`
  * Response Body - `application/json`
  ```json
  {
      "status" : 200,
      "lng" : 0.0000,
      "lat" : 0.0000
  }
  ```
* `[GET /api/v1.0/geocode?address=<address>]`
  * Response Body - `application/json`
  ```json
    {
        "status" : 200,
        "lng" : 0.0000,
        "lat" : 0.0000
    }
  ```
* POST/PUT/DELETE/PATCH methods not supporting

# How to extend your API Module
* Simply create a new module in `app/modules` from `BaseApi`
 * name : [service:name].py
```python
from .base import BaseApi
class YourMapsApi(BaseApi):
    def get_geocode(self, keyword):
        response = self.get({'params' : keyword})
        # please write the response handling
        # and then return it
```
* Register your module in `app/config/config.json`
```json
...
    {
        "name"     : "[service:name]",
        "classname": "[YourMapsApi]",
        "endpoint" : "[your api endpoint]",
        "key"      : "[Your Maps API Key]",
        "priority" : 1
    }
...
```


