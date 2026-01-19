
# Dictionary - key:value pair like map in other languages
# Keys are unique, values can be duplicate
# Mutable - can add, remove, update items
# Unordered - items do not have index
# Defined using {} or dict()

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

for itemKey in student_scores:
    if student_scores[itemKey] > 90:
        student_grades[itemKey]="Outstanding"
    elif student_scores[itemKey] > 80 and student_scores[itemKey] < 91:
        student_grades[itemKey]="Exceeds Expectations"
    elif student_scores[itemKey] > 70 and student_scores[itemKey] < 81:
        student_grades[itemKey]="Acceptable"
    elif student_scores[itemKey] < 71:
        student_grades[itemKey]="Fail"

print(student_grades)