# About weather(based on location)

> This project retrieves current weather conditions for a specified location using the OpenWeatherMap API. It provides information such as the current temperature in Kelvin, Celsius, and Fahrenheit, the weather description (e.g., sunny, cloudy, rainy), humidity, and wind speed.


### About the code:

- The codebase is break down in two file `weathercondition.py` and `main.py`.

`weathercondition.py` Retrieve and display the weather information using the info_about_weather function.
and `main.py` contains basic code.

### Implemantation of `weathercondition.py`

- requests is imported and used to send a GET request to the OpenWeatherMap API in order to retrieve weather information for a specified location.

- The code defines a class Weathercondition that is used to retrieve weather information for a given location using the OpenWeatherMap API.


```

import requests

class Weathercondition:

# Initializes a new instance of the class with the provided place parameter.
    def __init__(self, place):

        """The __init__ method initializes a new instance of the class
        with a place parameter representing the location for which weather information is to be retrieved.
        It constructs the API request URL using a base URL (base_url),
        an API key (api_key), and the provided place.
        It sends a GET request to the API using requests.get(),
        retrieves the response in JSON format, and stores it in the response attribute of the class instance.
        """

        try:
            self.place = place

            base_url = "https://api.openweathermap.org/data/2.5/weather?"

            api_key = "77ad31e7533acafbb84df531bd681311"

            place_url = base_url + "appid=" + api_key + "&q=" + self.place
            self.response = requests.get(place_url).json()

        except:
            return None

# convert temperature from kelvin to celsius
    def kelvin_to_celsius(self, kelvin):

        celsius = kelvin - 273.15
        return celsius

# convert temperature from kelvin to farenheit
    def kelvin_to_farenheit(self, kelvin):

        celsius = kelvin - 273.15
        farenheit = celsius * (9 / 5) + 32
        return farenheit

# Returns a dictionary containing various weather information such as temperature, wind speed, humidity, and weather description.
    def info_about_weather(self):

        """This method checks if the API response indicates a valid city ("cod" value is not "404").
        If the city is valid, it extracts various weather-related data from the JSON response,
        such as temperature, feels-like temperature, wind speed, humidity, and weather description.
        """

        if self.response["cod"] == "404":
            return "No city Found"
        else:
            try:
                temp_kelvin = self.response["main"]["temp"]
                temp_in_celsius = self.kelvin_to_celsius(temp_kelvin)
                temp_in_farenheit = self.kelvin_to_farenheit(temp_kelvin)
                feels_like_kelvin = self.response["main"]["feels_like"]
                feels_like_in_celsius = (self.kelvin_to_celsius(feels_like_kelvin),)
                feels_like_in_farenheit = (self.kelvin_to_farenheit(feels_like_kelvin),)
                wind_speed = self.response["wind"]["speed"]
                humidity = self.response["main"]["humidity"]
                description = self.response["weather"][0]["description"]

                weather_info = {
                    "temp_kelvin": temp_kelvin,
                    "temp_in_celsius": temp_in_celsius,
                    "temp_in_farenheit": temp_in_farenheit,
                    "feels_like_kelvin": feels_like_kelvin,
                    "feels_like_in_celsius": feels_like_in_celsius,
                    "feels_like_in_farenheit": feels_like_in_farenheit,
                    "wind_speed": wind_speed,
                    "humidity": humidity,
                    "description": description,
                }
                return weather_info
            except:
                None

```
### Here's the implementation of 'main.py'
```
    from weathercondition import Weathercondition

    place = Weathercondition("delhi")
    weather_info = place.info_about_weather()
    print(weather_info)

```