def get_top_scores(my_list):
    top_students = []
    my_list.sort(key = lambda x:x[1])
    highest_score = my_list[-1][1]

    for score in my_list:
        if score[1] == highest_score:
            top_students.append(score[0])
    return top_students

amount = int(input())

students = []
for people in range(amount):
    name, score = input().split()
    students.append((name, int(score)))

print(get_top_scores(students))
