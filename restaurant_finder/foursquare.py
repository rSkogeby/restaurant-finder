#!/usr/bin/env python
"""Return restaurant based on meal type and coordinates."""
import requests
import json

from config import getFoursquareVersion

from instance.config import getFoursquareClientId
from instance.config import getFoursquareClientSecret


def getRestaurant(category, coordinates):
    """Return restaurant suggestion.
    
    Input: requested category of food, e.g. Pizza, Pasta, Seafood, etc. and
    the coordinates in the general vicinity of where you would like to eat.

    Output: string with the name of the restaurant that is the best match
    for your criteria.
    """
    client_id = getFoursquareClientId()
    client_secret = getFoursquareClientSecret()
    version = getFoursquareVersion()
    cleaned_category = category
    formatted_coordinates = '{},{}'.format(coordinates['lat'],coordinates['lng'])
    api_call = '''https://api.foursquare.com/v2/venues/search?ll=
        {}&categoryId={}&client_id={}&client_secret={}&v={}'''.\
            format(formatted_coordinates, cleaned_category,
                   client_id, client_secret, version)
    data = requests.get(api_call)
    venue_name=json.loads(data.content.decode())['response']['venues'][0]['name']
    return venue_name
