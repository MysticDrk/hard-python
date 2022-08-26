
import datetime
import json
import requests


user_input = input("Hello, insert a province: ")
lat = ""
lon="" 

with open("lezione5\data\province.json", "r") as f:
    provinces_dict= json.load(f)
 
province = user_input.capitalize();

if province not in provinces_dict:
  raise Exception("Please insert a valid province")



lat = str(provinces_dict[province]["lat"])
lon = str(provinces_dict[province]["lon"])

# https://api.open-meteo.com/v1/forecast?latitude=45.04&longitude=07.42&hourly=temperature_2m&hourly=apparent_temperature

url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m&hourly=apparent_temperature".format(lat,lon)


response_json = requests.get(url).json()


now = int(datetime.datetime.now().strftime("%H"))

real_temp = response_json["hourly"]["temperature_2m"][now]

app_temp = response_json["hourly"]["apparent_temperature"][now]


print("Temperature in {} at time {} is {} C° and is felt as {} C°.".format(province, now, real_temp, app_temp))