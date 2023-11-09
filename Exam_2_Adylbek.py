def code(number):
    my_dict = {
        "A" : '2', 'B' : '2', 'C' : '2',
        "D" : '3', 'E' : '3', 'F' : '3',
        "G" : '4', 'H' : '4', 'I' : '4',
        "J" : '5', 'K' : '5', 'L' : '5',
        "M" : '6', 'N' : '6', 'O' : '6',
        "P" : '7', 'Q' : '7', 'R' : '7', 'S' : '7',
        "T" : '8', 'U' : '8', 'V' : '8',
        "W" : '9', 'X' : '9', 'Y' : '9', 'Z' : '9',
        '1' : '1', '2' : '2', '3' : '3', '4' : '4', '5' : '5', '6' : '6', '7' : '7', '8' : '8', '9' : '9'
    }
    return ''.join(my_dict[i] for i in number if i in my_dict)
phone = input('Please enter a phome number in the format XXX-XXX-XXXX: ').upper()
num = phone.split('-')
n1 = code(num[0])
n2 = code(num[1])
n3 = code(num[2])
print(f'{n1}-{n2}-{n3}')