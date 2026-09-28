import random

print("welcome to miffy's world")

memories = []
activities = ["watch drama", "sing a song", "play game", "cook something", "draw something"]

while True:
    print("1.talk to miffy")
    print("2.tell miffy about ur day")
    print("3.random activity")
    print("4.view memories")
    print("5.exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user = input("enter:")
        if user == "hello":
            print("miffy:hi")
        elif user == "i'm tired":
            print("miffy:want me to play a song")
        else:
            print("hmm miffy's charge out, i dont wanna talk, goodnight")

    if choice == "2":
        print("miffy:how was ur day?")
        user = input("enter:")
        memories.append(user)

        if user == "good" or user == "great":
            print("yeah miffy's day was great too")
        elif user == "sad" or user == "boring":
            print("miffy:wanna play a game to boost happiness?")
        else:
            print("miffy too young to say something")

    if choice == "3":
        print(random.choice(activities))

    if choice == "4":
        if memories:
            for memory in memories:
                print(memory)
        else:
            print("Miffy: no memories yet! 🐰")

    if choice == "5":
        print("miffy:see u later hooman")
        break
