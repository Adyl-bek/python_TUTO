# import csv
# with open('quiz_data.csv', 'w', "|") as file:
#             writer = csv.writer(file)
#             writer.writerows([["No", "Text_of_question", "A", "B", "C", "D", "correct_answer"],
#                              [1, "test", "a", "b", "c", "d", 1]])

import csv

# csv.register_dialect('myDialect',
#                      delimiter='|',
#                      quoting=csv.QUOTE_ALL)
# with open('quiz_data.csv', 'a', newline="") as file:
#     writer = csv.writer(file, dialect='myDialect')
#     writer.writerow([input("enter number"), "Text_of_question", "A", "B", "C", "D", "correct_answer"])


with open("quiz_data.csv", 'r') as file:
  csvreader = csv.reader(file, delimiter='|')
  for row in csvreader:
    a = row
  id = int(a[0]) + 1

csv.register_dialect('myDialect',
                     delimiter='|',
                     quoting=csv.QUOTE_ALL)
with open('quiz_data.csv', 'a', newline="") as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerow([id, "Text_of_question", "A", "B", "C", "D", "correct_answer"])