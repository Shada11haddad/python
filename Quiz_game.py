print("Welcome to My Computer Quiz!")
score = 0

Playing = input("Do you want to play? ")
if Playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

# Question 1
answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("What is software? ")

if answer.lower() == "instructions that tell the hardware what to do":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("The computer's main circuit board is called a ________. ")

if answer.lower() == "motherboard":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("What is Wi-Fi? ")

if answer.lower() == "a type of wireless network":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Final Score
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
