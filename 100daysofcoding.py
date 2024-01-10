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
    
