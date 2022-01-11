# how to find the most repeated character in a given text

print("this application shows the most repeated character in a given text")


def char_freq():

    text = input("enter the text: ")
    print("the text is: {}".format(text))

    char_frequency = {}

    for char in text:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    char_frequency_sorted = sorted(char_frequency.items(),
                                   key=lambda kv: kv[1], reverse=True)

    print("the most repeated character is: {}".format(
        char_frequency_sorted[0]))
    print("the complete result for all characters is this: {}".format(
        char_frequency_sorted))


while True:
    char_freq()
