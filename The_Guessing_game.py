import random

number_range = input("Choose a number: ")

if number_range.isdigit():
    number_range = int(number_range)
    
    if number_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
        
else:
    print("Please type a number next time.")
    quit()
    
random_number = random.randint(0, number_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("way to go, champ!")
        break
    elif user_guess > random_number:
            print("you were above the number!") 
    else:     
        print("you were below the number!")  
print("You got it in", guesses, "guesses")
    

