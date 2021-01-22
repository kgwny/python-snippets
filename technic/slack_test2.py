import requests

TOKEN = 'slack token'
CHANNEL = 'slack channel id'
files = {'file': open("****.csv", 'rb')}

param = {
    'token': TOKEN,
    'channels': CHANNEL,
    'filename': 'DLファイル名',
    'initial_comment': '投稿コメント',
    'title': '添付ファイルの名前'
 }

# file upload
requests.post(
    'https://slack.com/api/files.upload', 
    params=param, 
    files=files,
)
