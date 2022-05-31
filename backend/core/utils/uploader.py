import requests
import traceback

from django.core.files import File

from sentry_sdk import capture_exception

from django.conf import settings


def upload_file(file_obj: File) -> dict:
    """
    :param `file_obj` is file/image object, eg: from `request.FILES['file']`
    :return dict of {'action': <boolean>, 'url': <string>, 'message': <string>}
    """
    url = getattr(settings, 'UPLOADER_SERVICE_URL')
    token = getattr(settings, 'UPLOADER_SERVICE_TOKEN')

    try:
        files = {'file': file_obj}
        headers = {'Authorization': 'Bearer %s' % token}
        response = requests.post(url, files=files, headers=headers)
        return response.json()
    except Exception as err:
        capture_exception(err)
        return dict()
