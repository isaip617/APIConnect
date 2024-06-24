# webapi.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Isai
# Isaip@uci.edu
# 75292336

import urllib, json
from urllib import request,error
from abc import ABC, abstractmethod

class WebAPI(ABC):
  """parent class to LastFM and OpenWeather"""

  def _download_url(self, url: str) -> dict:
    """Uses url to grab info from API key and unwraps the json wrapped info."""
    response = None
    r_obj = None
    try:
        response = urllib.request.urlopen(url)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        if e.code == 401:
          print("Invalid API Key. Request Failed")
        elif e.code == 403:
            print('Invalif API Key. Request Failed')
        elif e.code == 404:
            print('Invalif API Key. Request Failed')
        elif e.code == 503:
            print('Coudld Not Connect to Server')
    except urllib.error.URLError as e:
       ResponseData = e.reason
       print(ResponseData)
    finally:
        if response != None:
            response.close()
        return r_obj

  def set_apikey(self, apikey:str) -> None:
    """sets the api key."""
    self.apikey = apikey


  @abstractmethod
  def load_data(self):
    """Loads the data."""
    pass

  @abstractmethod
  def transclude(self, message:str) -> str:
    """transforms the keywords into attributes."""
    pass