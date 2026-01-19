evn = lambda num:num%2==0
print(evn(22))

#Lambda to square each item in the list
#lambda arguments: expression
lst = [1,2,3,4,5]
sqr_lst = list(map(lambda x:x**2,lst))
print(sqr_lst)