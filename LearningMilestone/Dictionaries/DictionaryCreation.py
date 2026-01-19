# Dictionary key should unique and immutable type
# Values can be duplicate and mutable type
# Key types - string, number, tuple but not list, dict, set
# Value types - list, dict, set, string, number, tuple
d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)

'''
#Not allowed list as disctionary key as its mutable element
d3 = {"Fruit":["Mango","Banana"], ["Rose", "Lotus"]:'Flower'} 
print(d3)
'''
