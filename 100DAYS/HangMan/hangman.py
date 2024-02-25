import random
import os
from hangman_art import art,intro,lose,win

# Open the file and read the lines
wording = open("/home/aref/Desktop/Codes/Python/HangMan/words.txt","r").read().splitlines()
word = random.choice(wording).lower()
lives = 6
sample =""
for i in range(0, len(word)):
    sample +="_ "
print (intro)
while lives > 0 and sample.replace(" ","") != word: 
    print(art[7-lives-1])
    print(sample)   
    guess = input("\nEnter your guess : ")
    os.system('clear')
    if guess in word:
        print("Correct!")
        for i in range(0, len(word)):
            if word[i] == guess:
                sample = sample[:i*2] + guess + sample[i*2+1:]
    else:
        lives -= 1
        print("Wrong! You chose", guess, "and you have", lives, "lives left")
os.system('clear')
if lives == 0:
    print(lose)
    print("You lost! The word was", word)
else: 
    print(win)
    print("You won! The word was", word)