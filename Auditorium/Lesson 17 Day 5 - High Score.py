student_scores = input().split()
for i in range(len(student_scores)):
    student_scores[i] = int(student_scores[i])

highest_score = student_scores[0]
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
