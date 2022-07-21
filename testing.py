import datetime
import requests

from delorean import Delorean

MY_LAT = 41.867599
MY_LONG = -103.664169

_api_directive_str = "%Y-%m-%dT%H:%M:%S%z"

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}

request = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sr_txt = (request.json()["results"]["sunrise"])
ss_txt = (request.json()["results"]["sunset"])
sr_dt_instance = datetime.datetime.strptime(sr_txt, )
ss_dt_instance = datetime.datetime.strptime(ss_txt, "%Y-%m-%dT%H:%M:%S%z")


sr_new = Delorean(sr_dt_instance)
sr_convert = sr_new.shift("US/Mountain")

print(sr_convert)

