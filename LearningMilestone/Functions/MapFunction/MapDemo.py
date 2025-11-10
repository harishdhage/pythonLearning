def square(x):
    return x*x

print(square(2))

num = [1,2,4,5,6]
print(list(map(square,num)))

print(list(map(lambda x:x*x,num)))
num2 = [7,2,5,1]
print(list(map(lambda x,y:x+y,num,num2)))

str_num = ['2','5','90']
int_num=list(map(int,str_num))
print('str_num : ',str_num)
print('int_num : ',int_num)

word=['mango','jojpo','kabada']
wordInUpper = list(map(str.upper,word))
print(wordInUpper)

ppl = [
    {'Name':'Kanda','Age':23,'Adress':'21cross, KRK'},
    {'Name':'Bonda','Taste':'Spicy','Price':32}
]
def get_data(ppl):
    return ppl['Name']
print(list(map(get_data,ppl)))