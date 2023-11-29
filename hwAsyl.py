def read_scores(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        i = 0
        while i < len(lines):
            name = lines[i].strip()
            i += 1

            if i < len(lines):  
                try:
                    score = int(lines[i])
                    if 0 <= score <= 100:
                        yield name, score
                except ValueError:
                    pass

            i += 1

    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return


def write_scores(file_name, min_score, max_score, avg_score):
    try:
        with open(file_name, 'a') as file:
            file.write(f"Minimum score: {min_score}\n")
            file.write(f"Maximum score: {max_score}\n")
            file.write(f"Average score: {avg_score}\n")
    except FileNotFoundError:
        print(f"File {file_name} not found.")


def calculate_stats(scores):
    total = 0
    min_score = float('inf')
    max_score = float('-inf')
    valid_count = 0

    for name, score in scores:
        total += score
        min_score = min(min_score, score)
        max_score = max(max_score, score)
        valid_count += 1

    if valid_count == 0:
        return 0, 0, 0  

    average = total / valid_count

    return min_score, max_score, average



file_name = "scores.original.txt"
user_input = input("Enter the name of the student to display their score: ")

scores = read_scores(file_name)

student_score = None
for name, score in scores:
    if name == user_input:
        student_score = score
        print(f"{name}'s score is: {score}")
        break

if student_score is None:
    print(f"No valid score found for {user_input}.")

scores = read_scores(file_name)  
min_score, avg_score, max_score = calculate_stats(scores)
write_scores(file_name, min_score, avg_score, max_score)



