import os
import random

print("Welcome to Higher or Lower!")

# Before the previous results are read in, check the file
# actually exists. Otherwise, you'll get an error.
if os.path.exists("scores.txt"):
  
  with open("scores.txt","r") as file:

    # Read in the file as a single string
    scores = file.read()

    # The file is very simple - 'p' refers to a program win, 'u' is a user win
    programWins = scores.count("p")
    userWins = scores.count("u")

    print("You have won",userWins,"times and I have won",programWins,"times.")

else:
  # If the file doesn't already exist, create a new one
  # The line below opens a file in write mode and then immediately closes it
  open("scores.txt", "w").close()

print("I'm thinking of a number between 1 and 100...")

number = random.randint(1,100)
guess = 0
score = 0

# Keep looping until the user guesses correctly
while guess != number:
  
  guess = int(input("Make a guess: "))
  score += 1

  if guess < number:
    print("Higher")

  elif guess > number:
    print("Lower")

else:
  # The loop ends when the user guesses correctly
  print("Well done! It was" ,number)

# You could use any structure which works, but here a single letter is used to denote a win
# Be sure to open as append to avoid overwriting the whole file
with open("scores.txt","a") as file:

  if score > 6:
    print("I win! You scored",score)
    file.write("p")
  else:
    print("You won, well done. You scored",score)
    file.write("u")

