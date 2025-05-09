print("Helcone to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


secret_number = 42

max_attempts = 5

attempts = 0


while attempts < max_attempts:
    attempts = attempts + 1
    print ("Attempt " + str(attempts) + " of " + str(max_attempts))


    guess = int(input ("Enter your guess: "))


    if guess == secret_number:
        print ("Congratulations! You guessed the number!")
        break

    elif guess < secret_number:
        print ("Too low! Try again.")

    else:
        print ("Too high! Try again.")
