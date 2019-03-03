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
    category_id = '4d4b7105d754a06374d81259' # Default is FQ category 'Food'
    if cleaned_category.lower() == 'pizza':
        category_id = '4bf58dd8d48988d1ca941735'
    elif cleaned_category.lower() == 'sushi':
        category_id = '4bf58dd8d48988d1d2941735'
    elif cleaned_category.lower() == 'seafood':
        category_id = '4bf58dd8d48988d1ce941735'
    elif cleaned_category.lower() == 'tacos':
        category_id = '4bf58dd8d48988d151941735'
    elif cleaned_category.lower() == 'tapas':
        category_id = '4bf58dd8d48988d1db931735'
    elif cleaned_category.lower() == 'falafel':
        category_id = '4bf58dd8d48988d10b941735'
    elif cleaned_category.lower() == 'spaghetti':
        category_id = '4bf58dd8d48988d110941735'
    elif cleaned_category.lower() == 'cappucino':
        category_id = '4bf58dd8d48988d1e0931735'
    elif cleaned_category.lower() == 'steak':
        category_id = '4bf58dd8d48988d1cc941735'
    elif cleaned_category.lower() == 'gyros':
        category_id = '4bf58dd8d48988d10e941735'
    formatted_coordinates = '{},{}'.format(coordinates['lat'],coordinates['lng'])
    api_data_call = '''https://api.foursquare.com/v2/venues/search?ll=
        {}&categoryId={}&client_id={}&client_secret={}&v={}'''.\
            format(formatted_coordinates, category_id,
                   client_id, client_secret, version)
    data = requests.get(api_data_call)
    venue=json.loads(data.content.decode()).get('response').get('venues')
    if venue == None:
        return None
    venue_name = venue[0]['name']
    venue_id = venue[0]['id']
    venue_photo = ''
    venue_address = ', '.join(venue[0]['location']['formattedAddress'])
    venue_info = {'name': venue_name, 'address': venue_address,
                  'image': venue_photo}
    # Get venue photo
    api_photo_call = 'https://api.foursquare.com/v2/venues/{}/photos?client_id={}&client_secret={}&v={}'.\
        format(
            venue_id, client_id, client_secret, version
        )
    data = requests.get(api_photo_call)
    photo=json.loads(data.content)

    if photo.get('meta').get('code') != 200:
        return venue_info
    photo = photo.get('response').get('photos').get('items')
    if photo == []:
        return venue_info
    prefix = photo[0]['prefix']
    suffix = photo[0]['suffix']
    size = '200x200'
    venue_photo = ''.join([prefix, size, suffix])
    venue_info['image'] = venue_photo
    return venue_info
