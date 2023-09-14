# # print("Hello world!")
# # user = input("name: ")
# # print("Hello "+ user)
# # print(f'Hello {user}')
# a = 1
# b = 5
# # print(f"A+B={a+b}")
# if ( a > 3):
#     print("ERROR")
# else:
#     print("ACCEPTED")
# a, b = 0, 0
# a = input("ВВЕДИТЕ 1 ЧИСЛО: ")
# b = input("ВВЕДИТЕ 2 ЧИСЛО: ")
# # while(type(a) != int and type(b) != int):
# #         print("ПОЖАЛУЙСТА ВВЕДИТЕ ЧИСЛО")
# while(type(a) != int):
#     a = input("ВВЕДИТЕ 1 ЧИСЛО ЕЩЁ РАЗ: ") #str
#     if(type(int(a)) == int):
#         a = int(a)
# while(type(b) != int):
#     b = input("ВВЕДИТЕ 2 ЧИСЛО ЕЩЁ РАЗ: ")
#     if(type(b) == int):
#         b = int(b)
# print(f"СУММА = {a+b}")

# a = 4
# b = 8
# print(a + b)


from math import pow

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Operations: ")
print("If the operation you want is \"addition\" type +")
print("If the operation you want is \"subtraction\" type -")
print("If the operation you want is \"multiplication\" type *")
print("If the operation you want is \"division\" type /")
print("If the operation you want is \"exponentiation\" type ^")

z = input()
def main():
    if(z == "+"):
        print(f"The sum is {add(a, b)}")
    if(z == "-"):
        print(f"The dif is {sub(a, b)}")
    if(z == "*"):
        print(f"The comp is {mul(a, b)}")
    if(z == "/"):
        print(f"The res is {div(a, b)}")
    if(z == "^"):
        print(f"The pow is {exp(a, b)}")

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

def exp(a, b):
    return pow(a, b)
main()


# a = input("Enter first number: ")
# b = input("Enter second number: ")
# if(type(a) == float and type(b) == float):
#     print("Operations: ")
#     print("If the operation you want is \"addition\" type 1")
#     print("If the operation you want is \"subtraction\" type 2")
#     print("If the operation you want is \"multiplication\" type 3")
#     print("If the operation you want is \"division\" type 4")
#     print("If the operation you want is \"exponentiation\" type 5")

#     z = int(input())

#     if(z == 1):
#         print(f"The sum is {float(a) + float(b)}")
#     if(z == 2):
#         print(f"The dif is {float(a) - float(b)}")
#     if(z == 3):
#         print(f"The comp is {float(a) * float(b)}")
#     if(z == 4):
#         print(f"The res is {float(a) / float(b)}")
#     if(z == 5):
#         print(f"The pow is {pow(float(a) , float(b))}")
# else :
#     print("Try again")
#     a = input("Enter first number: ")
#     b = input("Enter second number: ")
#     print("Operations: ")
#     print("If the operation you want is \"addition\" type 1")
#     print("If the operation you want is \"subtraction\" type 2")
#     print("If the operation you want is \"multiplication\" type 3")
#     print("If the operation you want is \"division\" type 4")
#     print("If the operation you want is \"exponentiation\" type 5")

#     z = int(input())

#     if(z == 1):
#         print(f"The sum is {float(a) + float(b)}")
#     if(z == 2):
#         print(f"The dif is {float(a) - float(b)}")
#     if(z == 3):
#         print(f"The comp is {float(a) * float(b)}")
#     if(z == 4):
#         print(f"The res is {float(a) / float(b)}")
#     if(z == 5):
#         print(f"The pow is {pow(float(a) , float(b))}")

