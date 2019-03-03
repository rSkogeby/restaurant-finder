#!/usr/bin/env python3
"""Serve up a webpage for finding a restaurant given a preferred meal type and location."""

from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.datastructures import ImmutableMultiDict

from restaurant_finder.geocode import getCoordinates
from restaurant_finder.foursquare import getRestaurant

app = Flask(__name__)


def isEmpty(inp):
    """Return true if dict is empty, false if not."""
    empty = ''
    if isinstance(inp, ImmutableMultiDict):
        for k, v in inp.items():
            if v is empty:
                continue
            return False
        return True
    else:
        for item in inp:
            if item is empty:
                continue
            return False
        return True


@app.route('/', methods=['GET','POST'])
def landingPage():
    """Return page with search restaurant functionality."""
    if request.method == 'POST':
        if isEmpty(request.form):
            return redirect(url_for('landingPage'))
        if isEmpty(request.form['restaurant_type']) is False:
            category = request.form['restaurant_type']
        if isEmpty(request.form['location']) is False:
            location = request.form['location']
        coordinates = getCoordinates(location)
        restaurant = getRestaurant(category, coordinates)
        if restaurant == None:
            flash('No restaurant found.')
        else:
            flash('{} is a {} restaurant in {}.'.format(restaurant,
                                                    category,
                                                    location))
        return redirect(url_for('landingPage'))
    elif request.method == 'GET':
        return render_template('landingpage.html')


def main():
    app.secret_key = 'a_very_secret_key'
    app.run(host='localhost', port=5000, debug=True)


if __name__ == "__main__":
    main()