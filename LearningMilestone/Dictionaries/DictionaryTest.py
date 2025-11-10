
test_dict = {}
print(type(test_dict))

test_dict1 = dict()
print(type(test_dict1))

colors = {
    "Apple":"Red",
    "Mango":"Yellow",
    "Coco":"Green",
    "Coco":"Pale green"
}

colors["Code"]=123

print(colors)
print(colors["Coco"])
print(len(colors))

for x in colors:
    print(x)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for item in student_scores:
    if student_scores[item] > 90:
        student_grades[item]="Outstanding"
    elif student_scores[item] > 80 and student_scores[item] < 91:
        student_grades[item]="Exceeds Expectations"
    elif student_scores[item] > 70 and student_scores[item] < 81:
        student_grades[item]="Acceptable"
    elif student_scores[item] < 71:
        student_grades[item]="Fail"

print(student_grades)