### api practice

import requests

while True:

    boredom_status = input("are you bored? yes or no or i don't know \n")

    if boredom_status == "yes":

        print("bored api")
        api_url1 = "https://www.boredapi.com/api/activity"
        response1 = requests.get(api_url1)
        print(response1.json())


    elif boredom_status == "no":

        print("weather api")
        api_url2 = "http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json"
        response2 = requests.get(api_url2)
        print(response2.json())

    elif boredom_status == "i don't know":
        break


print("so what do you know?")