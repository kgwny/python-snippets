
def get_fruits(basket, fruit):
    """A variation is to use 'if fruit in basket:'"""
    try:
        return basket[fruit]
    except KeyError:
        return set()

def get_fruits_short(basket, fruit):
    # dict.get(key[, default])はkeyが辞書にあればvalueを返す/keyが規定外だとdefault値を返す
    return basket.get(fruit, set())


basket = {'apple': 'りんご', 'banana': 'ばなな'}

print('key: apple - result =', get_fruits(basket, 'apple'))
print('key: melon - result =', get_fruits(basket, 'melon'))

print('key: apple - short result =', get_fruits_short(basket, 'apple'))
print('key: melon - short result =', get_fruits_short(basket, 'melon'))
