import random
print("Welcome to the number guessing game!")
while True: #Create loop for 'Would you like to play again'
    rng = random.randrange(0,50)
    print("Guess from 0 to 50.")
    numGuess = 0
    while numGuess <= 5:
        guess = input()
        guess = int(guess)
        #Doesn't reduce guesses if user guesses number out of range.
        if guess > 50:
            print("Please guess within the range.")
            continue
        elif guess < 0:
            print("Please guess within the range.")
            continue
        guessLeft = (4 - numGuess)
        numGuess = numGuess + 1
        if guess > rng:
            print("Your number is too high!")
        elif guess < rng:
            print("Your number is too low!")
        elif guess == rng:
            print("You guessed it!")
            break
        if guessLeft == 0:
            print("You lose! The number was " + str(rng))
            break
        elif guessLeft == 1:
            print("You have 1 guess left.")
        else:
            print("You have " + str(guessLeft) + " guesses left.")
    print("Would you like to play again?")
    while True:
        playAgain = input()
        if playAgain.lower() == "yes":
            print("Let's play again!")
            break
        elif playAgain.lower() == "no":
            print("Thanks for playing!")
            exit()
        else:
            print("Please answer with yes or no.")
    
    