import argparse

parser = argparse.ArgumentParser(
    description='how to use hoge.py',
    formatter_class=argparse.RawTextHelpFormatter
)
parser.add_argument('id', help='id')
parser.add_argument('name', help='name')
parser.add_argument('term', help='term')
args = parser.parse_args()
