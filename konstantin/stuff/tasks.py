import subprocess
from django.conf import settings
from celery import shared_task

@shared_task
def get_screenshot(url):
    result = subprocess.call([
        settings.PHANTOMJS_BINARY,
        settings.CAPTURE_SCRIPT_PATH,
        url,
    ])
    print(result)
    return result
