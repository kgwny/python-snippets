dictionary = {
    'animal': ['dog','cat','human'],
    'clothes': ['shirts','pants','outer']
}

for key, array in dictionary.items():
    if 'cat' in array:
        print(key)
