import random

listx = list() # Here list() is class object
print('listx type - ',type(listx))
listA=["aaple", 'mango','banana', 'berry']
print("List A - ",listA)
listA.sort()
print("Sorted List A - ",listA)
listA.sort(reverse=True)
print("Sorted List A in desc - ",listA)
print('sort using sorted - ',sorted(listA)) #sorted() return the sorted list, but not sort the original list
listB=[1,4,True,'Sun',546.124]
print(listA)
print(listA[0])
print(listA[-2]) #Printing 2nd index counting from last
print("List B Original - ",listB)
listB[-1]=33.98 # updating value
print("List B after updating last index - ",listB)
listB.append('last one') #Adding ele at last index
print(listB)
listB.insert(3,"Ball") #Insert item to list at index 3
print("After insert - ",listB)
listA.extend(listB) #Added another list element to listA
print("Before pop - ",listA)
listA.pop(-3) #Remove 3rd index counting from last
print("After pop - ",listA)
listA.pop() #last item get popped
print("After pop without index - ",listA)
print("Get index of item - ",listA.index("Ball"))
listA.insert(-8,"Ball")
print("Get count of element repeated - ",listA.count("Ball"))
#print("Sort element - ",listA.sort()) - Not allowed to perform sort if list contains multiple typed elements

#list[start:end:step] - start index is inclusive, end index is exclusive
print("From index 2 to 5 - ", listA[2:5])
print("From index 3 - ", listA[2:])
print("From index 3 to last-1 index - ", listA[2:-1])
print("From -5 to -1 : ",listA[-5:-1])
listA.reverse()
print("Reverse list with reverse() - ", listA)
print("Reverse list - ", listA[::-1])
print("Get alternative element from list - ", listA[::2])
print(random.choice(listA))
randomNum = random.randint(1, 5)
print(listA[randomNum])
listC=[listA,listB]
print(listC)
print(listC[0][1]) #here listC[list seq][item from list]
print("Reverse listC - ",listC[::-1]) #Reverse the list
print("Get alternative from listC - ",listC[0:1:2]) #Gives the alternative list from listC
