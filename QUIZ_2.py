"""I wanna make a new one"""

import csv
import os

with open("quiz_data.csv", 'r') as file:
  csvreader = csv.reader(file, delimiter='|')
  for row in csvreader:
    a = int(row[0])
  id = a + 1

check_file = os.stat("quiz_data.csv").st_size

if(check_file == 0):
    csv.register_dialect('myDialect',
                        delimiter='|',
                        quoting=csv.QUOTE_ALL)
    with open('quiz_data.csv', 'a', newline="") as file:
        writer = csv.writer(file, dialect='myDialect')
        writer.writerow([id, "Text_of_question", "A", "B", "C", "D", "correct_answer"])

class Question:
    def __init__(self, question_text, answers, correct_answer):
        self.question_text = question_text
        self.answers = answers
        self.correct_answer = correct_answer

class Quiz:
    def __init__(self, teacher):
        self.teacher = teacher
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)
        with open('innovators.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow([id, question.question_text, "A", "B", "C", "D", "correct_answer"])

    def conduct_quiz(self):
        score = 0
        for question in self.questions:
            print(question.question_text)
            for i, answer in enumerate(question.answers, start=1):
                print(f"{i}) {answer}")
            
            student_answer = int(input("Your answer is: "))
            if student_answer == question.correct_answer:
                print("Great. It's correct\n")
                score += 1
            else:
                print("Sad. It's incorrect\n")
        
        print(f"Your score is: {score}")

class Teacher:

    def __init__(self, Account_No, PIN):
        self.Account_No = Account_No
        self.PIN = PIN

    def create_question(self, question_text, answers, correct_option):
        return Question(question_text, answers, correct_answer)
    
    def autentification(self):
        acc = input("Account_No: ")
        if(acc == teacher.Account_No):
            pin = input("PIN code: ")
            if(pin == teacher.PIN):
                print("Welcome Natalya Georgievna!")
            else: 
                print("Wrong PIN, try again")
                quit()
        else: 
            print("Wrong Account_No, try again")
            quit()

teacher = Teacher("g", "1234")

quiz = Quiz(teacher)

while True:
    operations = input("Choose: 1 - Add questions, 2 - Start a quiz, 3 - Quit: ")
    
    if operations == "1":
        teacher.autentification()
        question_text = input("Write down a question: ")
        answers = [input(f"Type answers {i}: ") for i in range(1, 5)]
        correct_answer = int(input("Which answer is correct(1 - 4): "))
        question = teacher.create_question(question_text, answers, correct_answer)
        quiz.add_question(question)
    elif operations == "2":
        quiz.conduct_quiz()
    elif operations == "3":
        break
    else:
        print("Please choise only 1, 2 or 3")