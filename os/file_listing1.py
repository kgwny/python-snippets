import glob

# ls = glob.glob('./*.ipynb')
# ls = glob.glob('./*.txt')
# ls = glob.glob('../**/*.py', recursive=True)

ls = glob.glob('./*.py')

for f in ls:
    print(f)
