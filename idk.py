# from math import *
# print("Adylbek \nis \na \nprogrammer")
# person_name = "Adylbek Rakhmanov"
# person_age = 18
# person_is_male = True
# print(person_name , "came to NAU couple of days ago.")
# print("The new student is" , person_age)
# print(person_name.upper().islower())
# print(person_name.replace("Adylbek", "Adyl"))
# num = -6
# print(abs(num))
# print(min(15, 67))
# print(floor(4.6))
# print(ceil(4.6))
# print(sqrt(16))
# print(dir("."))


# Import the 'string' module
# import string

# # Create a string containing whitespace, punctuation, digits, and letters
# chars = " " + string.punctuation + string.digits + string.ascii_letters

# # Convert the characters string into a list of individual characters
# chars = list(chars)

# # Print the list of characters
# print(chars)

# string = input("Input the string: ")

# new_str = string.split(' ')

# for i in range(len(new_str)):
#     first_letter = new_str[i][0]
#     print(first_letter)

string = input("Input the string: ")
string = string.strip()
new_str = string.split(' ')

for i in range(len(new_str)-1):
    first_letter = new_str[i][0]  
    new_str[i] = new_str[i].replace(first_letter, '')
    new_str[i] = new_str[i] + first_letter
print(new_str)

# emty = []
# print(type(emty))

# numbers = [1, 2, 3, 4, 5, 6, 7] 
# print(numbers[5:]) 






s=str(input("Kirigz : "))

tt=s.split(' ')
t2t=[]
for i in tt:
    x=""
    for j in range(1,len(i)):
        x+=i[j]
    x+=i[0]
    t2t.append(x)
print(t2t)