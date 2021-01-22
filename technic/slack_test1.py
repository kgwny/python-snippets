import requests

TOKEN = 'slack token'
CHANNEL = 'slack channel id'

url = "https://slack.com/api/chat.postMessage"

headers = {"Authorization" : "Bearer " + TOKEN}

data  = {
    'token': TOKEN,
    'channel': CHANNEL,
    'text': 'hello',
    'icon_emoji': ':ghost:'
}

# post message
requests.post(url , headers=headers, data=data)
