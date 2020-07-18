import zipfile

filepath = './sample.zip'

# 'r':ZIPファイル読み込み/'a':ZIPファイルへの追加/'w':新しいZIPファイルの作成
zip = zipfile.ZipFile(filepath, 'w', zipfile.ZIP_DEFLATED)

zip.write('./hoge.txt', 'hogehoge.txt')
