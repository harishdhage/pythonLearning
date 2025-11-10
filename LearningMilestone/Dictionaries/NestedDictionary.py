students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}

#Adding new item
students['Bob']['Skills']="Java, Cricket, Singing"
print(students)

#Access Data
print(students['Bob']['major'])
print(students.get('Bob',{}).get('Skills','Not found'))

#Delete
'''print(students['Bob']['major'])
print(students)
'''

for stud, studInfo in students.items():
    print('Student - ',stud)
    for key,value in studInfo.items():
        print('Key - ',key,' | Value - ',value)


