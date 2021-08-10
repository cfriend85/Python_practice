import math
def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            grades[i] = grades[i]
        elif math.ceil(grades[i]/5)*5 - grades[i] < 3:
            grades[i] = math.ceil(grades[i]/5) * 5
    return grades