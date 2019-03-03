#!/usr/bin/env python
"""Serve up a webpage for finding a restaurant given a preferred meal type and location."""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def landingPage():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass


