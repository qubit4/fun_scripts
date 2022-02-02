import time
import requests


def countdown(count):

    while count:
        mins, secs = divmod(count, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        count -= 1


def get_mission():
    # content of mission
    url = "https://www.boredapi.com/api/activity"
    response = requests.get(url)
    jsonresponse = response.json()
    mission = jsonresponse["activity"]

    # message
    multiline_message1 = ("Welcome, Jim. We haven't heard from you for some time. \n"
                          "Your mission, should you choose to accept it, is: \n")

    multiline_message2 = ("As always, should you or any of your IM Force be caught or killed, \n"
                          "the Secretary will disavow any knowledge of your actions. \n"
                          "This message will self-destruct in 10 seconds. \n")

    print(multiline_message1)
    print(mission, "\n")
    print(multiline_message2)

    # countdown and clearance of message
    countdown(10)
    # ANSI escape sequence clearing terminal
    print("\033c")
    print("\x1bc")
    quit()


get_mission()
