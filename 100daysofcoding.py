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