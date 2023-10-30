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
    