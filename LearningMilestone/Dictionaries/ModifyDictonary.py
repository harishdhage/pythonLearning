student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_scores['Ron'] = 43 # Update key value
print(student_scores)
student_scores['Baba'] = 53 # Added new key
print(student_scores)
student_scores.pop('Draco') # Remove key from dictionary
print(student_scores)
del  student_scores['Hermione']
print(student_scores)
student_scores.setdefault('Honda',98)
print(student_scores)
print(student_scores.popitem())
print(student_scores)
student_scores.update({'Mango':23})
print(student_scores)