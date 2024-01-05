#!/usr/bin/python3
""" Index objects that handles all default RestFul API actions"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """ Return status """
    return jsonify({"status": "OK"})
