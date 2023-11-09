room = {
    'CS101' : '3004', 'CS102' : '4501', 'CS103' : '6755', 'NT110' : '1244', 'CM241' : '1411'
}

teachers = {
    'CS101' : 'Haynes', 'CS102' : 'Alvarado', 'CS103' : 'Rich', 'NT110' : 'Burke', 'CM241' : 'Lee'
}

time = {
    'CS101' : '8:00 am', 'CS102' : '9:00 am', 'CS103' : '10:00 am', 'NT110' : '11:00 am', 'CM241' : '1:00 pm'
}
user = input("Enter a course number: ")

if(user in room and user in teachers and user in time):
    print(f"The course's room number is {room[user]}")
    print(f"The course's instructor is {teachers[user]}")
    print(f"The course's meeting time is {time[user]}")
else:
    print('Invalid course number, try again')