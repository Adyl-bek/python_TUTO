a = int(input('first:'))
b = int(input('second:'))
c = int(input('third:'))
if(type(a) != int and type(b) != int and type(c) != int):
    print("Dolbaeb, vvodi chisla")
else:
    while(a>0 and b>0 and c>0):
        if(a >= b and a >= c):
            if(b>=c):
                print(f"{c}, {b}, {a}")
                break 
            elif(c>=b):
                print(f"{b}, {c}, {a}")
                break 
        if(b>=a and b>=c):
            if(a>=c):
                print(f"{c}, {a}, {b}")
                break 
            elif(c>=a):
                print(f"{a}, {c}, {b}")
                break 
        if(c>=a and c>=b):
            if(a>=b):
                print(f"{b}, {a}, {c}")
                break    
            elif(b>=a):
                print(f"{a}, {b}, {c}")
                break 
        if(a == b and b == c):
            print(f"{a}, {b}, {c}")
            break
    else:
        print("Enter positive numbers") 
