num_of_guesses = 1
secret = "1234"

# Read in user's guess
user_guess = input("Please enter password: ")

while user_guess != secret and num_of_guesses < 5:
    print("Incorrect.")
    user_guess = input("Please enter password: ")
    num_of_guesses += 1

if user_guess == secret:
    print("Correct")    
else:
    print("Incorrect. Game over.")
