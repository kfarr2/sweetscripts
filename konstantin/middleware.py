import serial
import os, sys, re
import subprocess
import tempfile
from django.shortcuts import render_to_response
from django.db import connection
from time import time
from operator import add
from django.http import HttpResponse

#TODO: make this work without breaking everything
#class ArduinoMiddleware:
#    def process_response(self, request, response):
#        pass
        #connected = False
        #TODO: uncomment these if you want to use the arduino
        #siri = serial.Serial("/dev/tty0", 9600)
        #siri.write(str(response.status_code).encode())
        #return HttpResponse(response)
