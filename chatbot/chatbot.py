#######################
#
# Johnny Mai
# 2020-09-18
# Personalized chatbot v1
#
########################
import random

positiveReply = ["Wow!!", "That's Great!", "Ayyyyy.", "Poggers."]
neutralReply = ["Doing OK I guess?", "Average day huh?", "Could be better huh."]
negativeReply = ["Oh, thats too bad.", "Feels bad man.", "Damn, that sucks."]
randName = ["Terra", "Siri", "Dot", "Data", "Alexa", "Ava"]
bookList = ["Harry Potter", "The Lord of the Rings", "The Great Gatsby", "The Odyssey", "The Handmaid's Tale"]
sportList = ["soccer", "football", "badminton", "volleyball", "basketball", "tennis", "hockey", "swimming", "golf"]

print(f"Hello, my name is {random.choice(randName)} your personal chat bot! Let's get started.")
name = input("What's your name?\n>>> ")
print(f"Hello {name}! How are you today on a scale of 1-10?")

# Bot responds based on mood scale. Responds only to ints values
try:
    scale = int(input(">>> "))
    if 0 <= scale <= 3:
        print(random.choice(negativeReply))
    elif 3 < scale <= 6:
        print(random.choice(neutralReply))
    elif 6 < scale <= 10:
        print(random.choice(positiveReply))
    else:
        print("Im sorry, I don't understand.")
except ValueError:
    print("Im sorry, I don't understand.")

print("Do you like reading books?")
bookReply = input(">>> ").lower()

if bookReply == "yes" or bookReply == "yea" or bookReply == "y" or bookReply == "ye":
    print(f"{random.choice(positiveReply)} You should try reading {random.choice(bookList)}. It's one of my favourites!")
elif bookReply == "no" or bookReply == "nah" or bookReply == "nope" or bookReply == "n":
    print(f"{random.choice(negativeReply)} I would reccommend reading {random.choice(bookList)}, it's a great book even if you don't like to read.")
else:
    print("Im not sure I understand what you mean.")

print("How about other hobbies? Do you play any sports?")
sportReply = input(">>> ").lower()

if sportReply in sportList:
    print(f"Oh cool, {sportReply}! It's a shame I'm stuck inside this computer, otherwise I'd love to play with you.")
else:
    print("Im not sure I've heard of that sport before...")

print(f"Anyways... It was fun talking to you {name}! I'll see you later!")
