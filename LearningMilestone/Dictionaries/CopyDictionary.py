import copy

print("----- Demonstrating shallow copy -----")
original_dict = {"name": "Alice", "age": 25, "skills": ["Python", "Data Science"]}
shallow_copy = original_dict.copy() # This will do shallow copy, means it copies references of nested objects

# Any operation on shallow_copy that modifies mutable objects will reflect in original_dict
shallow_copy["age"] = 26
shallow_copy["skills"].append("Machine Learning")

# Displaying same results
print("Original dictionary:", original_dict)
print("Shallow copy:       ", shallow_copy)

shallow_dictcopy = dict(original_dict) # Another way to do shallow copy
shallow_dictcopy['skills'].append('Cobol')
print("Original dictionary:", original_dict)
print("Shallow dict copy:  ", shallow_dictcopy)

print("----- Demonstrating copy by reference and deep copy -----")
copyDict = original_dict # This will do deep copy by reference, both point to same object
copyDict['age']=251
print("Original dictionary:", original_dict)
print("Shallow copyDict:   ", shallow_copy)

deepCopyDict = copy.deepcopy(original_dict) # This will do deep copy, creates new object with copied values
deepCopyDict['age']=30
deepCopyDict['skills'].append('Java')
deepCopyDict['skills'].pop(1)
print("Original dictionary: ", original_dict)
print("Shallow deepCopyDict:", deepCopyDict)
