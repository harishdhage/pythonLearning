varA = [1,3,2,6,4]

#Shallow copy example
varB = varA.copy()
varB.append(7)
print("Original List varA - ", varA)
print("Shallow Copied List varB - ", varB)
#Deep copy example
import copy
varC = copy.deepcopy(varA)
varC.remove(3)
print("Original List varA - ", varA)
print("Deep Copied List varC - ", varC)
#Modifying nested list to show difference between shallow and deep copy
nestedListA = [1, 2, [3, 4], 5]
shallowCopyNested = nestedListA.copy()
deepCopyNested = copy.deepcopy(nestedListA)
shallowCopyNested[2].append(6) # Modifying nested list in shallow copy will reflect in original list
deepCopyNested[2].append(7)
print("Original Nested List nestedListA - ", nestedListA)
print("Shallow Copied Nested List shallowCopyNested - ", shallowCopyNested)
print("Deep Copied Nested List deepCopyNested - ", deepCopyNested)