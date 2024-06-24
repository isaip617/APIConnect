import unittest
from OpenWeather import *

class TestOpenWeather(unittest.TestCase):
    def test__init__(self):
        """tests attributes."""
        weather = OpenWeather()
        zip_code = weather.zip
        self.assertEqual(zip_code, '92697')
    
    def test__init__2(self):
        """tests attributes."""
        weather = OpenWeather()
        ccode = weather.ccode
        self.assertEqual(ccode, 'US')

    def test_transclude(self):
        """tests Transclusion."""
        weather = OpenWeather()
        weather.set_apikey('65874d8fe3e93a19b85142223ae67486')
        weather.load_data()
        str = "@weather today"
        new_str = weather.transclude(str)
        self.assertTrue(str != new_str)