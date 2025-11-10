prime = [primeNum for primeNum in range(1,101) if primeNum>1 for i in range(2,primeNum) if primeNum%i==0]
print(prime)

lst1 = [1,2,3,4,5]
lst2=['a','b','c','d']
pair = [[i,j] for i in lst1 for j in lst2]
print("Pair list - ",pair)