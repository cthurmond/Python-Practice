import random

number = 0

def startGame():

    global number
    number = random.randint(0, 100)

    print ("Welcome to my guessing game.")
    print ("I have thought of a number between 0 and 100.")
    print ("It is your job to guess it.")
    playGame()

def playGame():

    userGuess = int(raw_input("Enter your guess: "))
    if userGuess == number:
        print ("Congratulations! You have guessed correctly.")
        play_again = raw_input("Would you like to play again? y/n: ")
        
        if play_again.lower() == "y":
            startGame()
    
    elif userGuess < number:
        print ("Too low!")
        playGame()
    
    else:
        print ("Too high!")
        playGame()

startGame()