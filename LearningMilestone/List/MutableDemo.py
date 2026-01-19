myList = [1, 3, 5, 7, 9]
print("Original List:", myList)
print("ID of Original List:", id(myList))
myList[2] = 99  # Modifying the list at index 2
print("Modified List:", myList)
print("ID of Modified List:", id(myList))  # ID should remain the same