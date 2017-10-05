# Geocoding Proxy Service
   Find a longitude and latitude by an address

# Supporting Geocoding services
- [Google Maps Services](https://developers.google.com/maps/)
- [Bing Maps Services](https://www.bingmapsportal.com/)

# Not supporting Geocoding service
- [deprecated] : [Yahoo BOSS Geo Services](https://developer.yahoo.com/boss/geo/)

# How to run this script
* Install dependencies
```
sudo pip install --upgrade pip
pip install virtualenv
virtualenv python
source python/bin/activate
```
* Run requirement packages
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
        "name"     : "google-maps",
        "endpoint" : "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}",
        "key"      : "[Your Google Maps API Key]",
        "priority" : 1
    },
    {
        "name"     : "bing-maps",
        "endpoint" : "https://dev.virtualearth.net/REST/v1/Locations?q={}&key={}",
        "key"      : "[Your Bing Maps API Key]",
        "priority" : 0.9
    }
  ]
}
```
* Run this script
```
Usage:
  geocoding_proxy --address=<address> [-h] [--version]

Options:
  -a <address> --address=<address>  Show both a longitude and latitude by an address
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  geocoding_proxy -a "425 Market St #8, San Francisco, CA"
```