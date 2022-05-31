import requests
from typing import Optional

from django.conf import settings
from django.core.files import File
from django.core.files.storage import Storage, FileSystemStorage

from backend.core.utils.uploader import upload_file


class CustomRemoteStorage(Storage):
    def __init__(self) -> None:
        super().__init__()

    def _open(self, name, mode='rb') -> File:
        response = requests.get(name)
        return File(open(response.content))


    def _save(self, name, content: File):
        # save content to file management microservice
        response = upload_file(content)
        if response.get('action'):
            name = response.get('url')

        return name

    def url(self, name: Optional[str]) -> str:
        return name

    def exists(self, name: str) -> bool:
        return False

    def get_valid_name(self, name: str) -> str:
        return super().get_valid_name(name)

    def get_alternative_name(self, file_root: str, file_ext: str) -> str:
        return super().get_alternative_name(file_root, file_ext)

    def get_available_name(self, name: str, max_length: Optional[int] = ...) -> str:
        return super().get_available_name(name, max_length)
