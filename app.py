#!/usr/bin/python
# -*- coding: utf-8 -*-
import base64
import cgi
import datetime
from google.appengine.ext import ndb
from google.appengine.api import namespace_manager
from google.appengine.api import urlfetch
from google.appengine.api import users
from google.appengine.ext.webapp import util
from google.appengine.ext import webapp
import hashlib
import jinja2
import json
import logging
#from models import mghrrt
#from models import mghwhohash
import os
import socket
import sys
reload(sys);
sys.setdefaultencoding("utf8")
import time
import urllib, urllib2
import webapp2

def datetimefilter(value, format='%Y-%m-%d %H:%M:%S'):
    """convert a datetime to a different format."""
    return value.strftime(format)

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates/')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
jinja_environment.filters['datetimefilter'] = datetimefilter

class BaseHandler(webapp2.RequestHandler):

    #@webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(
        self,
        filename,
        template_values,
        **template_args
        ):
        template = jinja_environment.get_template(filename)
        self.response.out.write(template.render(template_values))

    def str2bool(self, v, caller):
        #logging.info("value of V in %s %s", str(v),caller)
        #logging.info("value of V out %s %s %s", str(v.lower() in ("yes", "true", "True" ,"t", "1")),caller, type(v.lower() in ("yes", "true", "True" ,"t", "1")))
        return v.lower() in ("yes", "true", "True" ,"t", "1")

class formhandler(BaseHandler):

    def post(self):
        #jsonreturn = ''
        #for item in self.request.get[:-1]:
           #jsonreturn += '{"'+str(item)+'": "'+str(self.request.get(item))+'"},'
        #jsonreturn += '{"'+str(item)+'": "'+str(self.request.get(item))+'"}'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(self.request.get)

    def get(self):
        

app = webapp2.WSGIApplication(
                                     [
                                      ('/phorm',formhandler)
                                     ],
                                     debug=True)