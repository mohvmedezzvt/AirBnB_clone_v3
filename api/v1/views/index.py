#!/usr/bin/python3
""" Index objects that handles all default RestFul API actions"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route("/status", methods=["GET"])
def status():
    """ Return status """
    return jsonify({"status": "OK"})
