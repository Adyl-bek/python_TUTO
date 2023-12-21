# l = [3,4,2]
# l1 = [5,6,1]


# l_num = 0
# l.reverse()
# for i in range(len(l)):
#     l_num += l[i] * (10**(len(l) - 1 - i))

# l_num1 = 0
# l1.reverse()
# for j in range(len(l1)):
#     l_num1 += l1[j] * (10**(len(l1) - 1 - j))

# res = l_num1 + l_num

# new_l = []

# result = ''
# result = str(res)

# for k in result:
#     new_l.append(k)


# new_l.reverse()
# print(new_l)
x = 1534236469
def reverse(self, x: int) -> int:
    if x >= -2**31 and x <= 2**31-1:
        if x == 0:
            return 0
        elif x < 0:
            x *= (-1)
            l = []
            s = ''
            s = str(x)
            for i in s:
                l.append(int(i))  
            l.reverse()
            init = 0
            for i in range(len(l)):
                init += l[i] * (10 ** (len(l) - 1 - i))
            return init * (-1)
        else:
            l1 = []
            s1 = ''
            s1 = str(x)
            for i in s1:
                l1.append(int(i))  
            l1.reverse()
            init1 = 0
            for i in range(len(l1)):
                init1 += l1[i] * (10 ** (len(l1) - 1 - i))
            return init1
    else:
        return 0 
