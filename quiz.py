"""QUIZ with 3(at this moment) questions by using classes"""

# class User():
#     def __init__(self, name, score) -> None:
#         self.name = name
#         self.score = score

class Human():
    def __init__(self, name):
        self.name = name

class Teacher(Human):
    def __init__(self, name,  Account, PIN):
        super().__init__(name)
        self.acc = Account
        self.pin = PIN

    def autentification(self):
        occ = input("If you are Teacher print T\n\nIf you are Student print S\n")
        if(occ == "T"):
            a = input("Account_No: ")
            if(a == self.acc):
                p = input("PIN: ")
                if(p == self.pin):
                    print("Welcome" + self.name)
                else:
                    print("Wrong PIN")
            else:
                print("Wrong Account_No")
        else:
            print("Welcome student")
    
    def add_questions():
        input("The text of question: ")
        input("The variety of answers: ")
        input("The correct answer: ")

class Student(Human):
    def __init__(self):
        pass

User = {
    "Name" : "Player",
    "Score" : 0
}

class Question():

    def __init__(self, question_number, question_text, corr_answer, all_answers) -> None:
        self.que_number = question_number
        self.que_text = question_text
        self.correct = corr_answer
        self.answers = all_answers

    def result(self) -> None:
        """Adds 1 point to player's score if he answers correctly"""
        print(self.que_number, "" + self.que_text)
        print(self.answers)
        answer = input("Your answer is: ")
        if(answer == self.correct):
            print("")
            print("It's correct")
            User["Score"] += 1
            print(User["Name"] + " your score is", User["Score"])
            print("--------------------")
        else:
            print("")
            print("Correct answer was on number " + self.correct + ", not on number", answer)
            print(User["Name"] + " your score is", User["Score"])
            print("--------------------")

    # def new_method(self):
    #     return 1

user_1 = Teacher("Olga Vasielevna", "Teach228", "8520")

print("***Welcome to QUIZ***")
user_1.autentification()



question_1 = Question("1.", "How many months of the year has 28 days?", "1", "1) 12\n2) 1\n3) 11\n4) None")
question_2 = Question("2.", "57+23=0\n10+12=1\n85+69=4\n78+89=?", "3", "1) 0\n2) 167\n3) 5\n4) 3")
question_3 = Question("3.", "Which planet in our solar system is known as the 'Red Planet'?", "4", "1) Mercury\n2) Saturn\n3) Sun\n4) Mars")

question_1.result()
question_2.result()
question_3.result()



















# print(question_1.que_number, "" + question_1.que_text)
# print(question_1.answers)
# question_1.result()
# print(User["Name"] + " your current score is", User["Score"])
# print("--------------------")

# print(question_2.que_number, "" + question_2.que_text)
# print(question_2.answers)
# question_2.result()
# print(User["Name"] + " your current score is", User["Score"])
# print("--------------------")

# print(question_3.que_number, "" + question_3.que_text)
# print(question_3.answers)
# question_3.result()
# print(User["Name"] + " your current score is", User["Score"])
# print("--------------------")

# if(User["Score"] == 3):
#     print("CONGRATS. YOU ARE THE SMARTEST")
# elif(User["Score"] == 2):
#     print("Not Bad")
# elif(User["Score"] == 1):
#     print("You can better")
# else:
#     print("It's pretty bad, maybe try again(")


# print(question_1.que_number, "" + question_1.que_text)
# print("")
# print(question_1.answers)
        