text = "question_no,text,a,b,c,d,correct"
print(text)
print(text.split(","))


#read csv file and name it "file"

# text = ""
# file = ""
# for letter in file.lines:
#     Question()

#open file in python
with open("quiz_data.csv") as file:
    lines = file.readlines() #lines = array of lines
    for line in lines:
        line_array = line.split(",")
        print(line_array)
# print(lines)
    
