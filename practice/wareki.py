# 西暦を入力
year = int(input())

year_list  = [1868, 1912, 1926, 1989, 2019, 9999]
wareki_list = ['明治', '大正', '昭和', '平成', '令和', '']

i = 0

# 西暦から和暦へ変換
while year_list[i] <= year:
    wareki_year = year - year_list[i] + 1
    wareki_name = wareki_list[i]
    i += 1
    print(str(year) + '年は' + wareki_name + str(wareki_year) + '年')
