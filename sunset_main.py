"""This Application will use the sunset, sunrise api to get the time when the sun will come up and set depending upon
the user's location. This will an additional function to tell us how much daylight we have.
Will be used with requests module"""

import requests
from lat_long_parser import LatLongParser
from datetime import datetime, timedelta


class ApiCall:
    OFFSET_HOURS = 6
    FRMT_STRING = "%I:%M:%S %p"

    def __init__(self, state_name_or_id: str = None, lat: str = None, long: str = None):
        self.state = state_name_or_id
        self.lat: str = lat
        self.long: str = long
        self._api = "https://api.sunrise-sunset.org/json?"

    def raw_sunset_sunrise(self):
        lat_long = LatLongParser.frmt_lat_long(self.state)
        r = requests.get(self._api + lat_long)
        sunrise_time_obj = datetime.strptime(r.json()["results"]["sunrise"], ApiCall.FRMT_STRING)
        sunset_time_obj = datetime.strptime(r.json()["results"]["sunset"], ApiCall.FRMT_STRING)
        return sunrise_time_obj, sunset_time_obj

    def convert_raw_to_mtn(self):
        """Gets return value from raw_sunset_sunrise and performs string formatting"""
        sr, ss = self.raw_sunset_sunrise()

        sunrise_to_mtn = sr - timedelta(hours=ApiCall.OFFSET_HOURS)
        sr_frmt = sunrise_to_mtn.strftime(ApiCall.FRMT_STRING)

        sunset_to_mtn = ss - timedelta(hours=ApiCall.OFFSET_HOURS)
        ss_frmt = sunset_to_mtn.strftime(ApiCall.FRMT_STRING)

        return f"The sunrise time is {sr_frmt}, and the sunset time is {ss_frmt}"


# TODO: Need to fix the timezones, add each timezone for each state

# TODO: AZ Does not observe DST, account for this

a = ApiCall("AZ")

print(a.convert_raw_to_mtn())
