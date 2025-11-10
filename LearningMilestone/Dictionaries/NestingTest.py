
# Dictionary = {"Key1":[List], "Key2":{DictionaryX}}

capitals = {
    "India":"Delhi",
    "Poland":"Warsaw",
    "Croatia":"Zadar"
}

cars = {
    "Tata": ["Sumo", "Nexon", "Icon"],
    "Maruti": ["Brezza", "700", "Icx", ["IManx", "Honad"]],
    "dict":capitals

}

print(cars["Tata"][1])
print(cars['Maruti'][3][1])
print(cars["dict"]["Poland"])