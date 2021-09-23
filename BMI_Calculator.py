print()
print("This is a Python file to practice IF/ELSE statements and WHILE loop statements")
answer = input("Would you like to learn more about this program? (Y or N): ")
print()
if answer.lower() != "y":
    if answer.lower() == "n":
        print("You seem like a nice individual. Have a great day!")
    else:
        print("What you have entered is ridiculous and I hope you have a great day. Get well soon.")
else:
    print("Excellent! I am super new to playing with Python! Can you tell?")
    print("I have always wanted to feel more confident in my programming skills, so")
    print("I decided to try and master the most common program out there: Python.")
    print()
print("I think this feels like a good place to put a crazy While loop!")
answer = input("Shall we continue? (Y or N): ")
print()
while answer.lower() == "y":
    if answer.lower() != "y":
        if answer.lower() == "n":
            print("That's okay! We can push on ahead.")
            break
        else:
            print("I assume that you do not want to be here. Goodbye.")
            break
    else:
        print("Excellent! Let's try this again!")
        answer = input("Continue loop? (Y or N): ")
        print()

print()
print("We have no escaped that dreaded loop! What should we do next?")
