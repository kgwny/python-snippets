import copy
import secrets

# トークン生成
token0 = secrets.token_hex()
print(token0)

token1 = secrets.token_hex()
token2 = copy.deepcopy(token1)
token3 = secrets.token_hex()

print(secrets.compare_digest(token1, token2))
print(secrets.compare_digest(token2, token3))

# 一時URLを生成するとき
url = 'https://example.com/reset=' + secrets.token_urlsafe()
print(url)
