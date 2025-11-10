lst=[]
for num in range(10):
    lst.append(num**2)
print(lst)

#Above operation for loop is done in single line code with List Comprehension
ls=[x**2 for x in range(10)]
print(ls)

#Even nums
lst1=[]
for num in range(10):
    if num%2==0:
        lst1.append(num)
print("Even num - ",lst1)

#Same above for loop is done single line code with List Comprehension with Condition
#new_list = [<expression> for <item in iterable> if <condition>]
even_num = [num for num in range(10) if num%2==0]
print("Even num - ",even_num)