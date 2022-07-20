"""This Application will use the sunset, sunrise api to get the time when the sun will come up and set depending upon
the user's location. This will an additional function to tell us how much daylight we have.
Will be used with requests module"""

import requests
from lat_long_parser import LatLongParser


class ApiCall:
    def __init__(self, state_name_or_id: str = None, lat: str = None, long: str = None):
        self.state = state_name_or_id
        self.lat: str = lat
        self.long: str = long
        self._api = "https://api.sunrise-sunset.org/json?"

    def return_sunset_sunrise(self):
        lat_long = LatLongParser.frmt_lat_long(self.state)
        r = requests.get(self._api + lat_long)
        sunrise = r.json()["results"]["sunrise"]
        sunset = r.json()["results"]["sunset"]
        return r.json()


a = ApiCall("NE")

print(a.return_sunset_sunrise())
