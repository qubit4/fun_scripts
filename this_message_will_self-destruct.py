import time
import requests
from os import remove
from sys import argv


def countdown(count):

    while count:
        # divmod() takes two numbers and returns a tuple consisting of quotient and remainder
        mins, secs = divmod(count, 60)
        # :02d formats a decimal integer (d) to a field of minimum width 2
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        # \r overwrites the current line
        print(timeformat, end="\r")
        time.sleep(1)
        count -= 1


def get_mission():
    # content of the mission
    url = "https://www.boredapi.com/api/activity"
    response = requests.get(url)
    jsonresponse = response.json()
    mission = jsonresponse["activity"]

    # message
    message1 = ("Welcome, Jim. We haven't heard from you for some time. \n"
                "Your mission, should you choose to accept it, is: \n")

    message2 = ("As always, should you or any of your IM Force be caught or killed, \n"
                "the Secretary will disavow any knowledge of your actions. \n"
                "This message will self-destruct in 10 seconds. \n")

    print(message1)
    print(mission, "\n")
    print(message2)

    # countdown until self-destruction
    countdown(10)
    # ANSI escape sequences clearing terminal
    print("\033c")
    print("\x1bc")
    # script now self-deletes
    remove(argv[0])


get_mission()
