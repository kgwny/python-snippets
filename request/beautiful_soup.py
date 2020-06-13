import bs4
import requests

# need bs4 module
res = requests.get('https://www.google.com/')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(soup.body)
