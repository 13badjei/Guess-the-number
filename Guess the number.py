 #!/bin/python3

# Don't worry about this line for now!
from random import randint as dice

# Notice how I space the code out into different sections to make it easier
# for me to read and remember what I'm doing in each section. The computer
# doesn't care and it makes my life easier.

# Here are some variables that let me change the game's rules easily.
# This saves me from changing any other code (and maybe breaking it!)
# if I want to change the number of guesses, or the numbers involved.
number_of_guesses = 5
lowest_number = 1
highest_number = 9

# Greet the player and teach them the rules
print("Hello and welcome to my number guessing game")
# I am using my variables in these print statements so they will change
# automatically if I change the rules later.
print("You will get "+str(number_of_guesses)+" guesses to pick a number")
print("The number will be between "+str(lowest_number)+" and "+str(highest_number))

# Now I am picking the secret number. See how I use the variables here again
# to make the rules of the game easy to change?
secret_number = dice(lowest_number,highest_number)

# Main game
# We're going to use guesses_left to record the number of guesses
# the player has left, subtracting one from it every time we go through
# the while loop
guesses_left = number_of_guesses

# Check if the player has any guesses left
while(guesses_left > 0):
  # Ask the player for their guess
  guess = input("Please guess a number:")
  # Turn their guess into an integer, so we can compare it
  guess = int(guess)
  # Check if their guess is bigger than the secret number
  if(guess > secret_number):
    # If it is bigger, tell the player
    print("Your guess is bigger than the number I'm thinking of.")
    # Remove one of the player's guesses
    guesses_left = guesses_left - 1
    # Remind the player how many guesses they have left
    print("You have "+str(guesses_left)+" guesses left")
  # Else, check if their guess is smaller than the secret number
  elif(guess < secret_number):
    # If it is smaller, tell the player
    print("Your guess is smaller than the number I'm thinking of.")
    # Remove one of the player's guesses
    guesses_left = guesses_left - 1
    # Remind the player how many guesses they have left
    print("You have "+str(guesses_left)+" guesses left")
  # Else, if it's not bigger, and it's not smaller, it is the same, right?
  else:
    # Tell the player they've won
    print("That's it! I was thinking of "+str(secret_number)+"!")
    print("***YOU WIN***")
    # Now, break the loop so the game doesn't keep playing.
    # We do this by making the condition (guesses_left > 0) false.
    # We use -1 (one number below 0) so we don't confuse this with running out of guesses
    guesses_left = -1
  
  #Now, if the player has used up their last guess, tell them they've lost the game
  if(guesses_left == 0):
    print("You're out of guesses. Game over!")