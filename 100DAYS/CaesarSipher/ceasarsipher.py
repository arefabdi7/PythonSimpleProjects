from os import system
from arts import intro, goodbye
def decoder(shifter , message):
    answer = ""
    for x in message:
        shifted = ord(x) - shifter
        if shifted < 97:
             shifted = 123 - (97 - shifted)
        elif shifted < 65:
            shifted = 91 - (65 - shifted)
        answer += chr(shifted)
    return answer

def encoder(shifter , message):
    answer = ""
    for x in message:
        shifted = ord(x) + shifter
        if shifted > 122:
            shifted = 96 + (shifted - 122) # If the char is a special character, adjust accordingly.
        elif shifted > 90 and shifted < 97:
            shifted = 64 + (shifted - 90)   # If it's an uppercase letter, add 64 to bring it back into
        answer += chr(shifted)
    return answer

print (intro)
while True:
    choice = input("Would you like to encode or decode a message? (e/d): ")
    shifter = int(input("How many places would you like to shift the message?: "))%25
    match choice:
        case "e":
            message = input("Enter the message you would like to encode: ")
            print(f"Your encoded message is: {encoder(shifter, message)}")
        case "d":
            message = input("Enter the message you would like to decode: ")
            print(f"Your decoded message is: {decoder(shifter, message)}")
        case _:
            print("Invalid choice, please try again.")
            continue
    choice = input("Would you like to encode or decode another message? (y/n): ")
    system('clear')
    if choice == "y":
        continue
    else:
        print (goodbye)
        break