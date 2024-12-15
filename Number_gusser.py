import random
trying = 5
top_of_range = input("Type a number: ")

# Validate user input for top_of_range
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('Please type a number larger than zero next time')
        quit()
else:
    print("Please type a valid number next time")
    quit()

# Generate a random number from 1 to top_of_range
random_number = random.randint(1, top_of_range)
# Uncomment the line below if you want to see the generated number for testing purposes
# print("Random number:", random_number)

# Loop until the user guesses correctly
while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a valid number next time.")
        continue
    if trying==1:
        quit()
    if user_guess == random_number:
        print("You got it!")
        print("You got it on your "+str(trying) + " chance!")
        break  # Exit the loop if the guess is correct
    elif user_guess < random_number:
        print("Your guess is too low, try again!")
        trying -= 1
        print("You only have "+str(trying) + " chance left!")
    else:
        print("Your guess is too high, try again!")
        trying -= 1
        print("You only have "+str(trying) + " chance left!")

    
