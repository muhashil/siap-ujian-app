from typing import Any, Union

from PIL import Image
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
from django.db.models.fields.files import (ImageFieldFile, FieldFile)


def get_host(request=None):
    HOST = ''
    if request:
        if settings.USE_SSL:
            HOST = 'https://%s' % request.get_host()
        else:
            HOST = 'http://%s' % request.get_host()
    return HOST



def get_image_url(image_url, request=None, default_image='static/images/no-image.jpg'):
    """
    :param `image_url` is image field or image url itself.
    :param `request` is request from view, default is None.
    :param `default_image` is default path image if `image_url` doesn't exist.

    return image url which following these conditions:
        - return no image when `image_url` is doesn't exist.
        - return origin image url if it scrapped product.
        - return image url local path when it saved at storage.

    [without request]
        - 'https://foobar.amazon.com/foobar/baz.png'
        or
        - '/media/uploads/2018/12/01/foobar.png'

    [with request]
        - 'https://foobar.amazon.com/foobar/baz.png'
        or
        - 'http://127.0.0.1:8000/media/uploads/2018/12/01/foobar.png'
    """

    HOST = settings.BASE_DOMAIN_FOR_UPLOADS or get_host(request)

    if not image_url:
        return '%s/%s' % (HOST, default_image)

    # whenever `image_url` saved from scrapped image url
    if str(image_url)[:4] == 'http':
        return str(image_url)
    elif str(image_url)[:2] == '//':
        return 'http:'+str(image_url)
    elif str(image_url)[:7] == 'uploads':
        return '%s%s%s' % (HOST, settings.MEDIA_URL, image_url)
    elif str(image_url)[:9] == 'resources':
        return '%s%s%s' % (HOST, settings.STATIC_URL, image_url)
    elif str(image_url)[:6] == 'static':
        return '%s/%s' % (HOST, image_url)

    # return '%s%s' % (HOST, image_url)
    if isinstance(image_url, ImageFieldFile) or isinstance(image_url, FieldFile):
        return '%s%s' % (HOST, image_url.url)

    return '%s%s' % (HOST, image_url)
