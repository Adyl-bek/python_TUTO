# f = open("sales.txt", "w")
# n = int(input("For how many daysdo you have sales? "))
# for i in range(n):
#     s = input(f"Enter the sales for day #{i+1}: ")
#     f.write(f"{s}\n")
# f.close()
"""

"""
# def average(file_name):
#   total = 0
#   count = 0
#   try:
#     with open(file_name, "r") as f:
#       for i in f:
#         try:
#           number = float(i)
#           total += number
#           count += 1
#         except ValueError:
#           pass
#   except IOError:
#     print("Error opening file:", file_name)

#   return total / count

# ave = average("numbers.txt")
# print(f"The average of the numbers: {ave}")
"""

"""
# f = open("USPopulation.txt", "r")
# year_population = f.readlines()
# f.close()
# year_population = [int(i) for i in year_population]
# change = [year_population[i + 1] - year_population[i] for i in range(len(year_population) - 1)]
# summ = 0
# for i in change:
#     summ += i
# average = summ / len(change)
# max_increase = change[0]
# min_increase = change[0]
# max_year = 1950
# min_year = 1950
# for i in range(1, len(change)):
#     if(change[i] > max_increase):
#         max_increase = change[i]
#         max_year = 1950 + i + 1
#     if(change[i] < min_increase):
#         min_increase = change[i]
#         min_year = 1950 + i + 1
# print(average)
# print(max_year)
# print(min_year)
"""

"""
# def morse(string):
#     morse = {
#         ' ': ' ', ',': '--..--', '.': '.-.-.-', '?': '..--..',
#         '0': '-----', '1': '.----', '2': '..---', '3': '...--',
#         '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#         '8': '---..', '9': '----.', 'A': '.-', 'B': '-...', 
#         'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
#         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
#         'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
#         'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
#         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 
#         'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
#     }
    
#     return ' '.join(morse[i] for i in string.upper() if i in morse)

# string = input("Enter text: ")
# print(morse(string))
"""

"""
# number = int(input("Enter a series of single-digit numbers: "))
# num = 0
# while(number != 0):
#     num += number % 10
#     number //= 10
# print(num)
"""

"""
# month = {
#     '01' : 'January', '02' : 'February', '03' : 'March', '04' : 'April', 
#     '05' : 'May', '06' : 'June', '07' : 'July', '08' : 'August', 
#     '09' : 'September', '10' : 'October', '11' : 'November', '12' : 'December'
# }
# date = input("Enter the date like this 'mm/dd/yyyy': ")
# data = date.split('/')
# print(f"{month[data[0]]} {data[1]}, {data[2]}")
    
#Coding Assignment 4
"""

"""
# class Employee:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number

#     def get_name(self):
#         return self.name
#     def set_name(self, name_1):
#         self.name = name_1 

#     def get_number(self):
#         return self.number
#     def set_number(self, number_1):
#         self.number = number_1  
    
# class ProductionWorker(Employee):
#     def __init__(self, name, number, shift_number = 0, hourly_pay_rate = 0):
#         Employee.__init__(self, name, number)
#         self.shift_number = shift_number
#         self.hourly_pay_rate = hourly_pay_rate

#     def get_hourly_pay_rate(self):
#         return self.hourly_pay_rate
#     def set_hourly_pay_rate(self, salary):
#         self.hourly_pay_rate = salary 
   
#     def get_shift_number(self):
#         if self.shift_number == 1:
#             return 'Day shift'
#         elif self.shift_number == 2:
#             return 'Night shift'
#         else:
#             return 'Invalid shift number, please input 1 or 2'
#     def set_shift_number(self, shift):
#             self.shift_number = shift

# name = input("Enter employee name: ")
# number = input("Enter employee number: ")
# shift_number = int(input("Enter shift number (1 for day, 2 for night): "))
# hourly_pay_rate = float(input("Enter hourly pay rate: "))

# employee = ProductionWorker(name, number, shift_number, hourly_pay_rate)

# print("Name:", employee.get_name())
# print("Employee Number:", employee.get_number())
# print("Shift:", employee.get_shift_number())
# print("Hourly Pay Rate:", employee.get_hourly_pay_rate())
"""

"""
# class Beverage:
#     def __init__(self, bev_name):
#         self.__bev_name = bev_name

# class Cola(Beverage):
#     def __init__(self):
#         super().__init__('cola')

# coka = Cola()
"""

"""
# def rais(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a * rais(a, b - 1)

# print(rais(5, 2))
"""

"""
# def unique_combination(string):

#     def comb(beg, last):
#         if not last:
#             needed_list.append(beg)
#             return
#         for i in range(len(last)):
#             comb(beg + last[i], last[:i] + last[i+1:])

#     needed_list = []
#     comb('', string)
#     needed_list.sort()  
#     return needed_list

# input_string = input("Enter string: ")
# print(unique_combination(input_string))
"""

"""