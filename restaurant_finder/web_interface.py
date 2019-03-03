#!/usr/bin/env python3
"""Serve up a webpage for finding a restaurant given a preferred meal type and location."""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def landingPage():
    if request.method == 'POST':
        return redirect(url_for('landingPage'))
    elif request.method == 'GET':
        return render_template('landingpage.html')


def main():
    app.secret_key = 'a_very_secret_key'
    app.run(host='localhost', port=5000, debug=True)


if __name__ == "__main__":
    main()