"""
@author: Vishwesh Malur Somashekar
Python Script to implement guess the number game
"""
import random
#function to check if guessed number and random number are matching
def checkGuessNumber(guessNumber, randomNumber):
    if guessNumber == randomNumber:
        return 0
    elif guessNumber < randomNumber:
        return -1
    elif guessNumber > randomNumber:
        return 1
    
        

#input user name
name = input('Hello! What is your name? ')
print("Well,",name,", I am thinking of a number between 1 and 20")
#generate random number from 1 to 20
randomNumber = random.randint(1, 20)
i=0
#while condition to check six valid and invalid guesses from user
while(i<6):
    try:
        guessNumber = int(input("Take a guess: "))
        #if block to check if guessed input is from 1 to 20
        if(guessNumber>0 and guessNumber<21):
            #call the function to compare the guess
            result = checkGuessNumber(guessNumber, randomNumber)
            if result == 0:
                print("Good job,",name,"! You guessed my number in " ,i+1, " guesses!")
                break
            elif result == -1:
                print("Your guess is too low.")
            elif result == 1:
                print("Your guess is too high.")
                #to check for invalid input outside given range
        else:
            print("Please Enter the number which between 1 and 20")
    #except block to check for input other than integer
    except Exception:
        print("Please enter a valid number")
    i+=1
#print the correct random number if user is unable to guess
if i > 5:
        print("The number I was thinking of was " + str(randomNumber))