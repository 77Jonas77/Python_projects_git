import requests

LAT = 52.229675
LONG = 21.012230

response = requests.get(
    url="http://api.open-notify.org/iss-now.json")

iss_lat = response.json().get("iss_position").get("latitude")
iss_long = response.json().get("iss_position").get("longitude")

if abs(LAT - iss_lat) <= 5 and abs(LONG - iss_long) <= 5:
    print("Nice iss is over your location...")
