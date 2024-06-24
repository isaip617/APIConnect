# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Isai
# Isaip@uci.edu
# 75292336

from WebAPI import WebAPI
import urllib, json
from urllib import request,error


class LastFM(WebAPI):
    def __init__(self, artist:str = 'Kanye') -> None:
        """Initialize the Data for LastFM."""
        self.artist = artist
    
    def load_data(self):
        """Create the Url and parse data from API."""
        url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={self.artist}&api_key={self.apikey}&format=json"
        dictionary = self._download_url(url)
        if dictionary != None:
            self.toptrack = dictionary["toptracks"]["track"][0]["name"]
        else:
            print("Could not Process Data")
    
    
    def transclude(self, message:str) -> str:
        """Transform keyword @lastfm into attribute."""
        transcluded_string = message.replace("@lastfm", self.toptrack)
        return transcluded_string
