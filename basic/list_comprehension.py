cities = ['nagoya', 'yokohama', 'koube', 'fukuoka', 'kyoto', 'sapporo', 'kawasaki']
k_list = []

for c in cities:
    if c.startswith('k'):
        k_list.append(c)

print(k_list)
# ['koube', 'kyoto', 'kawasaki']


# リスト内包表記
k_list = [c for c in cities if c.startswith('k')]
print(k_list)
# ['koube', 'kyoto', 'kawasaki']

cities_shi = [c + '-shi' for c in cities if c.startswith('k')]
print(cities_shi)
# ['koube-shi', 'kyoto-shi', 'kawasaki-shi']

cities_shi = [c + '-shi' for c in cities]
print(cities_shi)
# ['nagoya-shi', 'yokohama-shi', 'koube-shi', 'fukuoka-shi', 'kyoto-shi', 'sapporo-shi', 'kawasaki-shi']
