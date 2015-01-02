from PIL import Image
import re, sys, os
import subprocess
import urllib
from io import StringIO
from django.shortcuts import get_object_or_404
from django.conf import settings
from celery import shared_task

@shared_task
def get_screenshot(url):
    result = subprocess.call([
        settings.PHANTOMJS_BINARY,
        settings.CAPTURE_SCRIPT_PATH,
        url,
    ])
    image_name = url.split('www.')[1].split('.com')[0] + '.png'
    image_path = settings.ROOT('img/', str(image_name))
    img = Image.open(image_path)
    return img 
