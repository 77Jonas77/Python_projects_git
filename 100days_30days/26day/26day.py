import random
import pandas

ex = [1, 2, 3]
new_numbers = [item + 1 for item in ex]
# + poprawki w dniu 25


names = ['alex', 'bob', 'charlie']

student_scores = {student: random.randint(1, 100) for student in names}

passed_students = {student: score for student, score in student_scores.items()
                   if score >= 60}

# looping through rows of a DF
#
# student_data_frame = pandas.DataFrame(passed_students)
# for (index, row) in student_data_frame.iterrows():
#     print(index, row)

