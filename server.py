#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:59:48 2017

@author: iamorlando
"""

from flask import Flask, Response, request


from ballot_api import get_representatives

app = Flask(__name__)


@app.route("/representatives", methods=['POST'])
def representatives():
    data = request.get_json()
    address = data['address']
    levels = data['levels']
    key = data['key']
    response = Response(get_representatives(address,
                        levels,key))
    response.headers = {'Content-Type': 'application/json'}
    return response

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
