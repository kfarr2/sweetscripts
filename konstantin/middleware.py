import serial
import os, sys, re
import subprocess
import tempfile
from django.shortcuts import render_to_response
from django.db import connection
from time import time
from operator import add
from django.http import HttpResponse


class ArduinoMiddleware:
    def process_response(self, request, response):
        connected = False
        siri = serial.Serial("/dev/tty0", 9600)
        siri.write(str(response.status_code).encode())
        return HttpResponse(response)
