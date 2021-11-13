### another api practice


import requests

while True:
    
    joke = input("do you want to hear a joke? \n yes or no \n")

    if joke == "yes".lower():

        print("joke api")
        url = "https://v2.jokeapi.dev/joke/Any"
        response = requests.get(url)
        print(response.json())
        continue

    elif joke == "no".lower():
        break

    else:
        joke = input("do you want to hear a joke? \n yes or no \n")
        continue

print("no problem, I tell you one anyways")
print(response.json())
