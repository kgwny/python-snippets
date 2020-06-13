import requests

TARGET_URL = 'https://slack.com/api/channels.history'
CHANNEL_ID = ''
TOKEN = ''

def fetch_text():
    payload = {
        'channel': CHANNEL_ID,
        'token': TOKEN
    }
    response = requests.get(TARGET_URL, params=payload)
    json_data = response.json()
    msgs = json_data['messages']
    print(msgs)
    print([msg['text'] for msg in msgs])
    return [msg['text'] for msg in msgs]

if __name__ == '__main__':
    fetch_text()
