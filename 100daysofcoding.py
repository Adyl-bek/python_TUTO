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