from math import sqrt

def interface():
    print("\nWelcome to the Interactive Calculator:")
    print("1. Addiction\n2. Substarction\n3. Multiplication\n4. Division\n5. Square Root\n6. Quit")

def add(a, b):
    print(f"Result: {first_num} + {second_num} = {a + b}")

def sub(a, b):
    print(f"Result: {first_num} - {second_num} = {a - b}")

def mul(a, b):
    print(f"Result: {first_num} * {second_num} = {a * b}")

def div(a, b):
    if(b != 0):
        print(f"Result: {first_num} / {second_num} = {a / b}")
    else:
        print("Error")

def sqr():
    chs = int(input("Enter a number: "))
    if(chs >= 0):
        print(f"Result: Square root of {chs} = {sqrt(chs)}")
    else:
        print("Error")
    
def ext():
    print("Goodbye!")
    quit()
    
# interface()        
# choice = int(input("Enter your choice (1/2/3/4/5/6): "))
# choice = 1

while(1):  
    interface()
    choice = float(input("Enter your choice (1/2/3/4/5/6): "))
    if(choice != 5 and choice != 6):
        first_num = float(input("Enter the first number: "))
        second_num = float(input("Enter the second number: "))
        if(choice == 1):
            add(first_num, second_num)
        elif(choice == 2):
            sub(first_num, second_num)
        elif(choice == 3):
            mul(first_num, second_num)
        elif(choice == 4):
            div(first_num, second_num)
        # interface()
        # choice = int(input("Enter your choice (1/2/3/4/5/6): "))
        # first_num = int(input("Enter the first number: "))
        # second_num = int(input("Enter the second number: "))
    elif(choice == 5):
            sqr()
            interface()
            choice = float(input("Enter your choice (1/2/3/4/5/6): "))
            first_num = float(input("Enter the first number: "))
            second_num = float(input("Enter the second number: "))
    else:
        ext()