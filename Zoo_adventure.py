name = input("Type your name: ")
print("welcome", name, "to Zoo Adventure!")

answer = input("Do you love domestic animals or wild animals? Right for Wild animal, left for domestic animal ").lower()

if answer == "left":
    answer = input("Domestic section  entails numerous cuties, will you swim to your destination or walk: ")
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("not a valid option. You lose.")
        
elif answer == "right":
    answer = input("You reached the reception of the zoo and saw a Kangaroo, will you wait or go back(wait/back)? ")
    
    if answer == "back":
        print("You go back and lose.")
    elif answer == "wait":
        answer = input("You waited and noticed it was a dummy kangaroo (Yes/No)? ")
        
        if answer == "yes":
            print("you  waited and won the whole prize, Huraay!")
        elif answer == "no":
            print("You went back and You Lose!")
        else:
            print("Not a valid option. You lose.")
    else:
        print("not a valid option. You lose.")
    
else:
    print("not a valid option. You lose.")
    
print("See you soon at Zoo adventure", name, "!")
    




