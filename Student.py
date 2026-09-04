from array import *
grade = []

row = int(input("Enter number of students: "))
col = int(input("Enter number of subjects: "))
print()
for i in range(row):
    grade.append([])
    for j in range(col):
        grade[i].append(int(input(f"Student {i+1}, Subject {j+1}: ")))

print()
for i in range(row):
    for j in range(col):
        print(grade[i][j], end=" ")

        if 90 <= grade[i][j] <= 100:
            print("Excellent")
        elif 80 <= grade[i][j] <= 89:
            print("Very Good")
        elif 75 <= grade[i][j] <= 79:
            print("Passed")
        elif 0 <= grade[i][j] < 75:
            print("Failed")
        else:
            print("Invalid grade")
