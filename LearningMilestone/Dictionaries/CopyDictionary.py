import copy

original_dict = {"name": "Alice", "age": 25, "skills": ["Python", "Data Science"]}
shallow_copy = original_dict.copy()

# Modifying the shallow copy
shallow_copy["age"] = 26
shallow_copy["skills"].append("Machine Learning")

print("Original dictionary:", original_dict)
print("Shallow copy:       ", shallow_copy)

shallow_dictcopy = dict(original_dict)
shallow_dictcopy['skills'].append('Cobol')
print("Original dictionary:", original_dict)
print("Shallow dict copy:  ", shallow_dictcopy)

copyDict = original_dict # This will do deep copy
copyDict['age']=251
print("Original dictionary:", original_dict)
print("Shallow copyDict:   ", shallow_copy)

deepCopyDict = copy.deepcopy(original_dict)
deepCopyDict['skills'].append('Java')
deepCopyDict['skills'].pop(1)
print("Original dictionary: ", original_dict)
print("Shallow deepCopyDict:", deepCopyDict)
