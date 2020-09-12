import requests

response = requests.get('https://www.google.com/')
print(response.text)

# google.comの内容をhtmlファイルへ出力する
with open('./tmp/google.html', 'w') as file:
    file.write(response.text)
