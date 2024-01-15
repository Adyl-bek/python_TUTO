"""Day_2 / 10.04.2023"""
# num = int(input())
# res = int((num/10)) + (num%10)
# print(res)

# height = input()
# weight = input()

# bmi = int(weight) / float(height) ** 2  
# print(int(bmi)) 

# print((10//4))

"""PROJECT: tip calculator"""
# print('Welcome to the tip calculator')
# bill = float(input('What was the total bill? $'))
# tips = int(input('What percentage tip would you like ti give? 10, 12, or 15? '))
# people = int(input('How many people to split the bill? '))
# res = bill * ((100 + tips) / 100) / people
# print(f'Each person should pay: ${round(res, 2)}')
# print(f'Each person should pay: ${"{:.2f}".format(res)}')

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N

# money = 0

# if(size == 'S'):
#     money = 15
# elif(size == 'M'):
#     money = 20
# elif(size == 'L'):
#     money = 25

# if(size == 'S' and add_pepperoni == 'Y'):
#     money += 2
# elif(size == 'M' or size == 'L' and add_pepperoni == 'Y'):
#     money += 3
# if(extra_cheese == 'Y'):
#     money += 1

# print(f'Your final bill is: ${money}.')

"""PROJECT TREASURE ISLAND"""
# print()
# print('*******************************************************************************')
# print('          |                   |                  |                     |')
# print(' _________|________________.=""_;=.______________|_____________________|_______')
# print('|                   |  ,-"_,=""     `"=.|                  |')
# print('|___________________|__"=._o`"-._        `"=.______________|___________________')
# print('          |                `"=._o`"=._      _`"=._                     |')
# print(' _________|_____________________:=._o "=._."_.-="\'"=.__________________|_______')
# print('|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |')
# print('|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". \'__|___________________')
# print('          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |')
# print(' _________|___________| ;`-.o`"=._; ." ` \'`."\` . "-._ /_______________|_______')
# print('|                   | |o;    `"-.o`"=._``  \'` " ,__.--o;   |')
# print('|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________')
# print('____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____')
# print('/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_')
# print('____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____')
# print('/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_')
# print('____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____')
# print('/______/______/______/______/______/______/______/______/______/______/_____ /')
# print('*******************************************************************************')
# print()
# print('Welcome to Treasure Island.')
# print('Your mission is to find the treasure.')
# side = input("You're at a cross road. Where do you want to go? " + "Type " + '"left" ' + "or " + '"right"\n').lower()
# if(side == 'left'):
#   lake = input("You've come to a lake. There is an island in the middle of the lake. Type " + '"wait" ' + "to wait for a boat. Type " + '"swim"' + " to swim across.\n").lower()
#   if(lake == 'wait'):
#     door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
#     if(door == 'red'):
#       print("It's a room full of fire. Game Over.")
#       quit
#     elif(door == 'blue'):
#       print("You enter a room of beasts. Game Over.")
#       quit
#     elif(door == 'yellow'):
#       print("You found the treasure! You Win!")
#     else:
#       print("You chose a door that doesn't exist. Game Over.")
#   else:
#     print('You get attacked by an angry trout. Game Over.')
#     quit
# else:
#   print('You fell into a hole. Game Over.')
#   quit
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

#Write your code below this line 👇

# import random

# random_number = random.randint(1,3)

# choice = int(input('Choose 1 for Rock, 2 for Paper, 3 for Scissors\n'))

# if(choice == 1):
#   print("Your choise")
#   print(rock)
# elif(choice == 2):
#   print("Your choise")
#   print(paper)
# elif(choice == 3):
#   print("Your choise")
#   print(scissors)
# else:
#   print('Invalid choice')
# if(random_number == 1):
#   print("Computer's choise")
#   print(rock)
# elif(random_number == 2):
#   print("Computer's choise")
#   print(paper)
# elif(random_number == 3):
#   print("Computer's choise")
#   print(scissors)
# else:
#   print('Invalid choice')
# if(choice == 1 and random_number == 1 or choice == 2 and random_number == 2 or choice == 3 and random_number == 3):
#   print('Draw')
# elif(choice == 1 and random_number == 2 or choice == 2 and random_number == 3 or choice == 3 and random_number == 1):
#   print('You lost')
# elif(choice == 1 and random_number == 3 or choice == 2 and random_number == 1 or choice == 3 and random_number == 2):
#   print('You won')

#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# a = []
# for i in range(nr_letters):
#     x = random.randint(0, len(letters))
#     a.append(letters[x])
# for j in range(nr_symbols):
#     y = random.randint(0, len(symbols))
#     a.append(symbols[y])
# for z in range(nr_numbers):
#     d = random.randint(0, len(numbers))
#     a.append(numbers[z])
# random.shuffle(a)
# password = ''
# for i in a:
#     password += i
# print(password)
"""

"""     
# import random
# from hangman_words import word_list 
# from hangman_art import stages
# from hangman_art import logo
# print(logo)
# lives = 6
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# print(f'Pssst, the solution is {chosen_word}.')
# display = []
# for _ in range(word_length):
#     display += "_"
# while '_' in display:
#     if lives == 0:
#         print("You've lost.")
#         print(f"{' '.join(display)}")
#         print(stages[lives])
#         break
#     else:
#         guess = input("Guess a letter: ").lower()
#         if guess in display:
#                 print(f"You've already guessed {guess}")
#                 pass
#         for position in range(word_length):
#             letter = chosen_word[position]
#             if letter == guess:
#                 display[position] = letter
#             elif guess not in chosen_word:
#                 print(f"You guessed {guess}. It's not in the word. You lose a life.")
#                 lives -= 1
#                 break
#         print(f"{' '.join(display)}")
#         print(stages[lives])
# else: 
#     print("You've won")
"""

"""
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
       end_text += char    
  print(f"Here's the {cipher_direction}d result: {end_text}")

should_it_stop = False
while not should_it_stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    print('Do you wanna restart caesar safer? \nIf yes enter "yes", if no - "no"')
    answer = input()
    if answer == 'yes':
        should_it_stop = False
    else:
        should_it_stop = True
        print('See you!')

#That's fully mine code 
# def ceaser(text, shift, direction):
#     cyfer = []
#     cyfer_index = []
#     for i in text:
#         cyfer.append(i)
#     for m in cyfer:
#         cyfer_index.append(alphabet.index(m))
#     new_cyfer_index = []
#     cyfer_text = []
#     if direction == "encode":
#         for j in cyfer_index:
#             if j + shift <= 25:
#                 new_cyfer_index.append(j + shift)
#             else:
#                 new_cyfer_index.append(j + shift - 26)
#         for k in new_cyfer_index:
#             cyfer_text.append(alphabet[k])
#         cyfer_str = ""
#         for v in cyfer_text:
#             cyfer_str += v
#         print(f"The encoded text is: {cyfer_str}")
#     elif direction == "decode":
#         for j in cyfer_index:
#             if j - shift >= 0:
#                 new_cyfer_index.append(j - shift)
#             else:
#                 new_cyfer_index.append(j - shift + 26)
#         for k in new_cyfer_index:
#             cyfer_text.append(alphabet[k])
#         cyfer_str = ""
#         for v in cyfer_text:
#             cyfer_str += v
#         print(f"The decoded text is: {cyfer_str}")

# ceaser(text, shift, direction)


