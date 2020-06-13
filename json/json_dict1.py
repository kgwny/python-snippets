import json

# @see
# https://www.json.org/

json_text = '''
{
    "foo":"hoge",
    "bar":"ika",
    "baz":"tako"    
}
'''

json_dict = json.loads(json_text)

print(type(json_dict))
#<class 'dict'>

print(json_dict)
#json_dict:{'foo': 'hoge', 'bar': 'ika', 'baz': 'tako'}

print(type(json_dict["foo"]))
#<class 'str'>

print(json_dict["foo"])
#hoge

json_str = json.dumps(json_dict)

print(type(json_str))
#<class 'str'>

print(json_str)
#{"foo": "hoge", "bar": "ika", "baz": "tako"}

