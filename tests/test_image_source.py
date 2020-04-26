import unittest


class LoremFlickrTest(unittest.TestCase):
    def setUp(self) -> None:
        from lgtm.image_source import _LoremFlickr
        self.lf = _LoremFlickr("dog")

    def test_build_url(self) -> None:
        expected = "https://loremflickr.com/800/600/cat"
        actual = self.lf._build_url("cat")
        self.assertEqual(expected, actual)

    def tearDown(self) -> None:
        del self.lf
