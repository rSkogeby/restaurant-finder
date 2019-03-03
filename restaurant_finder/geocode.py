#!/usr/bin/env python
"""Return longitude and latitute based on location."""
import requests
import json

from instance.config import getGoogleAPIKey


def getCoordinates(location):
    """Return dictionary containing the latitude and longitude.
    
    Input: location is the location of the desired coordinates. Formatted 
    as if you were to type it into google maps.

    Output: dictionary with keys 'lat' and 'lng' for returning the
    latitude and longitude of the best match of the search string.
    """
    api_key = getGoogleAPIKey()
    cleaned_location = location
    api_call = 'https://maps.googleapis.com/maps/api/geocode/json?address={},&key={}'.format(cleaned_location,api_key)
    data = requests.get(api_call)
    coordinates=json.loads(data.content.decode())['results'][0]['geometry']['location']    
    return coordinates