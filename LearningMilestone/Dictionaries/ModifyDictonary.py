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
del  student_scores['Hermione'] # Remove key from dictionary
print(student_scores)
student_scores.setdefault('Honda',98) # Add new key if not exists
print(student_scores)
print(student_scores.popitem()) # Remove last inserted key
print(student_scores)
student_scores.update({'Mango':23}) # Add new key using update()
print(student_scores)