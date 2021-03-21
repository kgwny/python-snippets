import argparse

# usage: argparse_example1.py [-h] [--arg3 ARG3] [-a ARG4] arg1 arg2
# argparse_example1.py: error: the following arguments are required: arg1, arg2

# make parser
parser = argparse.ArgumentParser(description='description of this program')

# definition of argument
# 必須
parser.add_argument('arg1', help='description of arg1')
# 必須
parser.add_argument('arg2', help='description of arg2')
# 任意
parser.add_argument('-a3')
# 任意
parser.add_argument('-a4', '--arg4')

args = parser.parse_args()

print('arg1 = ' + args.arg1)
print('arg2 = ' + args.arg2)
print('arg3 = ' + args.arg3)
print('arg4 = ' + args.arg4)
