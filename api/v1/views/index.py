#!/usr/bin/python3
""" Index objects that handles all default RestFul API actions"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    pass
