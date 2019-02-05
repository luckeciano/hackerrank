students = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score])
students = sorted(students, key = lambda x: (x[1], x[0]))
#print(students)
for i in range (1, len(students)):
    if (students[i][1] == students[0][1]):
        continue
    else:
        for j in range(i, len(students)):
            if students[j][1] == students[i][1]:
                print(students[j][0])
        break

