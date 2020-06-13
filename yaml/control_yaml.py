import yaml

# @see
# https://yaml.org/

yaml_text = '''
meta:
  title: yaml title
  description: yaml description
'''

yaml_dict = yaml.safe_load(yaml_text)

print(type(yaml_dict))
# <class 'dict'>

print(yaml_dict['meta']['description'])
# yaml description
