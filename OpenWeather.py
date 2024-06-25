from WebAPI import WebAPI
from urllib import request,error

class OpenWeather(WebAPI):
    
    def __init__(self, zip:str = "92697", country_code:str = 'US') -> None:
        """Initialize the Data for OpenWeather."""
        self.zip = zip
        self.ccode = country_code
        

    def load_data(self):
        """Create the Url and parse data from API."""
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zip},{self.ccode}&appid={self.apikey}"
        dictionary = self._download_url(url)
        if dictionary != None:
            self.longitude = dictionary['coord']['lon']
            self.latitude = dictionary['coord']['lat']
            self.temperature = dictionary['main']['temp']
            self.high_temperature = dictionary['main']['temp_max']
            self.low_temperature = dictionary['main']['temp_min']
            self.description = dictionary['weather'][0]['description']
            self.humidity = dictionary['main']['humidity']
            self.city = dictionary['name']
            self.sunset = dictionary['sys']['sunset']
        else:
            print("Could not Process Data")
    
    
    def transclude(self, message:str) -> str:
        """Transform keywords into attributes."""
        transcluded_string = message.replace("@weather", self.description)
        return transcluded_string


