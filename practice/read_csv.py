import sys

# 要素数チェック
def check_element_count(target_list):
    for element in target_list:
        if len(element) != 2:
            print('element count check error:', element)
            sys.exit(0)

# リスト要素の重複チェック
# def has_duplicate(target_list):
#    return len(target_list) != len(set(target_list))

# 入れ子リスト要素の重複チェック
def has_duplicate(target_list):
    tmp = []
    unique_list = [target for target in target_list if target not in tmp and not tmp.append(target)]
    return len(target_list) != len(unique_list)

def read_file(target_file):
    return [line.strip().split(',') for line in open(target_file, 'r')]

def main():
    target_file = sys.argv[1]
    content = read_file(target_file)
    print(content)
    print(type(content))

    check_element_count(content)

    if has_duplicate(content):
        print("duplicate error detected.")

if __name__ == "__main__":
    main()

# $ python3 read_csv.py ./tmp/test.csv

# input csv file format
# 12345,100
# 23456,200
# 34567,300
# 67890,400
