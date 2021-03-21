import argparse

# usage: argparse_test.py [-h] id name term
# argparse_test.py: error: the following arguments are required: id, name, term

parser = argparse.ArgumentParser(
    description='how to use this program',
    formatter_class=argparse.RawTextHelpFormatter
)
parser.add_argument('id', help='id')
parser.add_argument('name', help='name')
parser.add_argument('term', help='term')
args = parser.parse_args()

print('id = ' + args.id)
print('name = ' + args.name)
print('term = ' + args.term)
