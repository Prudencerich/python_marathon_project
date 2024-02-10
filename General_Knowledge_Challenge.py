print("Welcome to my General knowledge quiz!")

playing = input("Are you ready to ace this? ")

if playing.lower() != "yes":
    quit()
    
print("Yay! shall we begin:)")

score = 0

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Way to go champ!")
    score += 1
else:
    print("opps! that is incorrect.")
    
answer = input("what is the capital of Nigeria? ")
if answer.lower() == "abuja":
    print("Way to go champ!")
    score += 1
else:
    print("opps! that is incorrect.")
    
answer = input("what is the capital of South Africa? ")
if answer.lower() == "pretoria":
    print("Way to go champ!")
    score += 1
else:
    print("opps! that is incorrect.")
    
answer = input("what is the capital of Ghana? ")
if answer.lower() == "accra":
    print("Way to go champ!")
    score += 1
else:
    print("opps! that is incorrect.")

answer = input("what is the capital of Russia? ")
if answer.lower() == "moscow":
    print("Way to go champ!")
    score += 1
else:
    print("opps! that is incorrect.")
    
print("you got " + str(score) + " questions correctly!")
print("you got " + str((score / 5) * 100) + "%")

    

