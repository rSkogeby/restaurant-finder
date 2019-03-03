#!/usr/bin/env python
"""Return longitude and latitute based on location."""
import requests
import json

from instance.config import getGoogleAPIKey

def getCoordinates(location):
    api_key = getGoogleAPIKey()
    cleaned_location = location
    api_call = 'https://maps.googleapis.com/maps/api/geocode/json?address={},&key={}'.format(cleaned_location,api_key)
    data = requests.get(api_call)
    coordinates=json.loads(data.content.decode())['results'][0]['geometry']['location']    
    return coordinates