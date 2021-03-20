import binascii
import os

# ランダムな文字列を生成する

random = binascii.hexlify(os.urandom(10))
print(type(random))
print(random)

# bytes型からstr型へ変換
random = random.decode('utf-8')
print(type(random))
print(random)
