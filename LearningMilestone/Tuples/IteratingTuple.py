nested_tuple = ((1,2,3,4),('a','b','c'),(True, False))

for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item, end=' ')
    print()