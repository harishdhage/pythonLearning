student_info = {
   "name": "Alice",
   "age": 22,
   "major": "Computer Science",
   "graduation_year": 2023
}

for key in student_info.keys():
    print(key)

for value in student_info.values():
    print(value)

for key,value in student_info.items():
    print(key,' : ',value)