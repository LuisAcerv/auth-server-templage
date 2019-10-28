# main.py

#!/usr/bin/env python3
import json, sys, os
import importlib
import logging

import falcon

class HandleCORS(object):
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', '*')
        resp.set_header('Access-Control-Allow-Headers', '*')
        resp.set_header('Access-Control-Max-Age', 1728000)  # 20 days
        if req.method == 'OPTIONS':
            raise HTTPStatus(falcon.HTTP_200, body='\n')


""" Process the GET requests
"""
class ProcessGetResource(object):
    def on_get(self, req, res, module, method):
        # Add modules path
        sys.path.insert(0, f'{os.getcwd()}/app/modules')

        # Import request module
        mod = None
        f = None
        try:
            mod = importlib.import_module(module)
        except:
            res.status = falcon.HTTP_400
            res.content_type = 'application/json'
            res.body = json.dumps({ 'message': 'Module not found', 'code': 400 })
        try:
            if mod is not None:
                try:
                    f = getattr(mod, str(method))
                except:
                    res.status = falcon.HTTP_400
                    res.content_type = 'application/json'
                    res.body = json.dumps({ 'message': 'Method not found', 'code': 400 })
                if f is not None:
                    res.status = falcon.HTTP_200
                    res.content_type = 'application/json'
                    res.body = (f())
        except ValueError as e:
            res.status = falcon.HTTP_500
            res.body = 'Internal server error'

    def on_post(self, req, res, module, method):
        # Add modules path
        sys.path.insert(0, f'{os.getcwd()}/app/modules')

        # Import request module
        mod = None
        f = None
        try:
            mod = importlib.import_module(module)
        except:
            res.status = falcon.HTTP_404
            res.content_type = 'application/json'
            res.body = json.dumps({ 'message': 'Module not found', 'code': 404 })
        try:
            if mod is not None:
                try:
                    f = getattr(mod, str(method))
                except:
                    res.status = falcon.HTTP_404
                    res.content_type = 'application/json'
                    res.body = json.dumps({ 'message': 'Method not found', 'code': 404 })
                if f is not None:
                    res.status = falcon.HTTP_200
                    res.content_type = 'application/json'
                    res.body = (f(req.stream))
        except ValueError as e:
            res.status = falcon.HTTP_500
            res.body = 'Internal server error'
 


# Create the Falcon application object
app = falcon.API(middleware=[HandleCORS()])

# Instantiate the ProcessGetResource class
get_resource = ProcessGetResource()

# Routes
app.add_route('/api/v1/{module}/{method}', get_resource)