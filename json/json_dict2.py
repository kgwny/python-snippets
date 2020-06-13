import json

json_text = '{"menu1":{"name": "hamburger","price": 110,"cal": 256},"menu2":{"name": "Big Macd","price": 390,"cal": 525},"menu3":{"name": "teriyaki macd","price": 340,"cal": 478}}'

json_dict = json.loads(json_text)

print('menu1の情報：{}'.format(json_dict['menu1']))
# menu1の情報：{'name': 'hamburger', 'price': 110, 'cal': 256}

print('menu2のcal情報:{}'.format(json_dict['menu2']['cal']))
# menu2のcal情報:525

print('menu3のprice情報：{}'.format(json_dict['menu3']['price']))
# menu3のprice情報：340

print(json_dict)
# {'menu1': {'name': 'hamburger', 'price': 110, 'cal': 256}, 'menu2': {'name': 'Big Macd', 'price': 390, 'cal': 525}, 'menu3': {'name': 'teriyaki macd', 'price': 340, 'cal': 478}}
