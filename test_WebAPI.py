import unittest
from WebAPI import *

class TestWebAPI(unittest.TestCase):
    def test__init__(self):
        """Initialize the Test."""
        class TestClass(WebAPI):
            """Create Test Class."""
            def __init__(self, artist:str = 'Kanye') -> None:
                """Initialize Test Class."""
                self.artist = artist
    
            def load_data(self):
                """Load data."""
                url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={self.artist}&api_key={self.apikey}&format=json"
                dictionary = self._download_url(url)
                self.toptrack = dictionary["toptracks"]["track"][0]["name"]
            
            
            def transclude(self, message:str) -> str:
                """Transform keywords into attributes."""
                transcluded_string = message.replace("@lastfm", self.toptrack)
                return transcluded_string
        tester = TestClass()
        artist = tester.artist
        self.assertEqual(artist, 'Kanye')

    def test_transclude(self):
        """Test Transclusion."""
        class TestClass(WebAPI):
            """Create Test Class."""
            def __init__(self, artist:str = 'Kanye') -> None:
                self.artist = artist
    
            def load_data(self):
                """Load data."""
                url = f"http://ws.audioscrobbler.com/2.0/?WWWWmethod=artist.gettoptracks&artist={self.artist}&api_key={self.apikey}&format=json"
                dictionary = self._download_url(url)
                self.toptrack = dictionary["toptracks"]["track"][0]["name"]
            
            def transclude(self, message:str) -> str:
                """Transform keywords into attributes."""
                transcluded_string = message.replace("@lastfm", self.toptrack)
                return transcluded_string
        lastfm = TestClass()
        lastfm.set_apikey('53d37265932dc14aa5ee8e276a4203ea')
        self.assertRaises(TypeError)

        