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
    try:
        image_name = url.split('//')[1].split('/')[0] + '.png'
    except IndexError as e:
        image_name = url.split('//')[1].split('/')[0] + '.png'
        
    #image_path = os.path.join(str(image_name))
    return image_name 
