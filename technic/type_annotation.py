from datetime import date
from urllib.request import urlopen
from urllib.parse import urlencode
import json

URL = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json"

def request_count_of_submitted_docs(date_):
    query = urlencode({"date": date_})
    resp = json.load(urlopen(f"{URL}?{query}"))
    return resp["metadata"]["resultset"]["count"]

print(request_count_of_submitted_docs(date(2020, 11, 20)))
# 504

# 型アノテーションの例
def request_count_of_submitted_docs(date_: date) -> int:
    query: str = urlencode({"date": date_})
    resp: dict = json.load(urlopen(f"{URL}?{query}"))
    return resp["metadata"]["resultset"]["count"]

print(request_count_of_submitted_docs(date(2020, 11, 20)))
# 504
