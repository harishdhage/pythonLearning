def square(x):
    return x*x

print(square(2))

num = [1,2,4,5,6]
# Map function applies the function to each item of the iterable (like list) and returns a map object (which is an iterator)
# map(function, iterable)
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

# --- Additional concise examples: building a dict from transformed data ---
keys = ['apple', 'banana', 'cherry']
values = list(map(len, keys))  # map transforms each key to its length
fruit_lengths = dict(zip(keys, values))
print('\nkeys:', keys)
print('values (from map):', values)
print('dict from zip:', fruit_lengths)

# Example: using map to transform then creating a lookup dict
users = ['alice', 'bob', 'carol']
ids = list(map(lambda n: n.upper(), users))
user_map = dict(zip(users, ids))
print('\nusers:', users)
print('ids (from map):', ids)
print('user_map (dict):', user_map)

# Guidance comment:
# - Use `map()` to transform iterables lazily (memory-efficient).
# - Use `dict` when you need key->value lookup, updates, or membership tests.