from art import gavel,welcome,shrek
from os import system


participant = {}
print (gavel)
print (welcome)
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    choice = input("Are there another bidder?: (y/n)")
    participant[name]= bid
    system('clear')
    if choice == "n":
         break
sortedParticipant = sorted(participant.items(),key=lambda x:x[1],reverse=True)
name = sortedParticipant[0][0]
print (shrek)
print("\n\n\nThe winner of mighty shrek is " + name + " with a bid of $" + str(dict(sortedParticipant)[name]))
