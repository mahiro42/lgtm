from abc import ABCMeta, abstractmethod
from io import BytesIO
from pathlib import Path
import requests
from typing import IO


class LoadImage(metaclass=ABCMeta):
    def __init__(self, src: str) -> None:
        self._src = src

    @abstractmethod
    def get_image(self) -> IO[bytes]:
        raise NotImplementedError


class LocalImage(LoadImage):
    """Load a image from local file"""

    def __init__(self, path: str) -> None:
        super().__init__(path)

    def get_image(self) -> IO[bytes]:
        return open(self._src, "rb")


class RemoteImage(LoadImage):
    """Load a image via URL"""

    def __init__(self, url: str) -> None:
        self._src = url

    def get_image(self) -> IO[bytes]:
        data = requests.get(self._src)
        return BytesIO(data.content)


class _LoremFlickr(RemoteImage):
    """Load a image by keyword search"""
    LOREM_FLICKR_URL = "https://loremflickr.com"
    WIDTH, HEIGHT = 800, 600

    def __init__(self, keyword: str) -> None:
        super().__init__(self._build_url(keyword))

    def _build_url(self, keyword: str) -> str:
        return (f"{self.LOREM_FLICKR_URL}/"
                f"{self.WIDTH}/{self.HEIGHT}/{keyword}")


KeywordImage = _LoremFlickr


def ImageSource(keyword: str) -> LoadImage:
    """Return the most appropriate class for the given keyword"""
    if keyword.startswith(("http://", "https://")):
        return RemoteImage(keyword)
    if Path(keyword).exists():
        return LocalImage(keyword)
    return KeywordImage(keyword)


def get_image(keyword: str) -> IO[bytes]:
    """Return file object of the image"""
    return ImageSource(keyword).get_image()
