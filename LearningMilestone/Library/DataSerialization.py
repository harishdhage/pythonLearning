#Data serialization from Json
import json
data = {
    'Name':'Harish',
    'Class':21,
    'score':63,
    'section':'D'
}
print(type(data),' | ',data)
json_str=json.dumps(data) #Converts python object (dictionary) to json string
print(type(json_str),' | ',json_str) 
parse_json = json.loads(json_str) #Parsing json string to python object (dictionary)
print(type(parse_json),' | ',parse_json)
