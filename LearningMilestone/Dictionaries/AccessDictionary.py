student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

print(student_scores['Ron'])
#print(student_scores['Don']) #Throws error, if no matching key is found
print(student_scores.get('Draco'))
print(student_scores.get('Don')) #Returns None if no matching key is found
print(student_scores.get('Don','Not available, enter correct key!!!')) #Returns default value as specified, if no matching key is found

print('values() - ', student_scores.values())
print('keys() - ', student_scores.keys())
print('items() - ', student_scores.items())
