import unittest
from LastFM import *

class TestLastFM(unittest.TestCase):
    def test__init__(self):
        """tests attributes."""
        lastfm = LastFM()
        artist = lastfm.artist
        self.assertEqual(artist, 'Kanye')
    
    def test__init__2(self):
        """tests attributes."""
        lastfm = LastFM('Kendrick')
        artist = lastfm.artist
        self.assertEqual(artist, 'Kendrick')

    def test_transclude(self):
        """tests Transclusion."""
        lastfm = LastFM()
        lastfm.set_apikey('53d37265932dc14aa5ee8e276a4203ea')
        lastfm.load_data()
        str = "@lastfm for today"
        new_str = lastfm.transclude(str)
        self.assertTrue(str != new_str)