while True:
    print("What is your name?")
    name = input()
    if name != "Joe":
    	continue
    if name == "Joe":
    	print("What is your password")
    	password = input()
    	if password == "swordfish":
    		break

print("access granted")




