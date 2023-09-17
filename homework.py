score = int(input("Enter your score: "))
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60
while(score >= 0 and score <= 100):
    if score >= A_SCORE:
        print('Your grade is A.')
        break
    elif score >= B_SCORE:
        print('Your grade is B.')
        break
    elif score >= C_SCORE:
        print('Your grade is C.')
        break
    elif score >= D_SCORE:
        print('Your grade is D.')
        break
    else:
        print('Your grade is F.')
        break
