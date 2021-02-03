import requests
from bs4 import BeautifulSoup

urlName = 'https://business.nikkei.com'
url = requests.get(urlName)
soup = BeautifulSoup(url.content, 'html.parser')

elements = soup.find_all('span')

for element in elements: 
    try:
        string = element.get('class').pop(0)
        print(string)

        if string in 'category':
            print(element.string)
            title = element.find_next_sibling('h3')
            print(title.text.replace('\n', ''))
            r = element.find_previous('a')
            print(urlName + r.get('href'), '\n')
    except:
        pass
