#Data serialization from Json
import json
data = {
    'Name':'Harish',
    'Class':21,
    'score':63,
    'section':'D'
}

json_str=json.dumps(data)
print(type(json_str),' | ',json_str)
print(type(data),' | ',data)
parse_json = json.loads(json_str)
print(type(parse_json),' | ',parse_json)
