# -*- coding: utf-8 -*-

# @Author: Stormix - Anas Mazouni
# @Date:   2017-02-12 23:04:51
# @Email:  madadj4@gmail.com
# @Project: Pronote V3.9
# @Last modified by:   Anas Mazouni
# @Last modified time: 2017-06-04T11:46:54+01:00
# @Website: https://stormix.co

# Import Some Python Modules
import requests


class LaPosteTracker(object):
    headers = {
        "X-Okapi-Key": "XMLHttpRequest"
    }
    api = "https://api.laposte.fr/suivi/v1/"

    def __init__(self, API_KEY):
        self.headers['X-Okapi-Key'] = API_KEY

    def get(self, route):
        response = requests.get(self.api+route, headers=self.headers)
        if(response.status_code == 200):
            return response.content
        else:
            print("Api failed to responed ({}): \n {}".format(
                response.status_code, response.content))

    def post(self, route, payload):
        response = requests.post(
            self.api+route, data=payload, headers=self.headers)
        if(response.status_code == 200):
            print(response.content)
        else:
            print("Api failed to responed ({}): \n {}".format(
                response.status_code, response.content))

    def track(self, code):
        # Detect carrier code:
        return self.get(code)

#    T.track("9C00336004550")
