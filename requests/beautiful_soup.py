import bs4
import requests

res = requests.get("https://www.google.com/")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
print(soup.body)
