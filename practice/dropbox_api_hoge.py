import dropbox
ACCESS_TOKEN = 'ABCDEFG12345HIJKLMN678OPQRSTU90'

local_path = 'fox.jpg'
path = '/images/' + local_path  #dropbox直下に「images」フォルダを作成

# ファイルをDropboxにアップロード
f = open(file_from, 'rb')
dbx.files_upload(f.read(),path )
f.close()


# ファイル名取得
#for entry in dbx.files_list_folder('/images/').entries:
#    print(entry.name)

# 共有リンク作成       
setting = dropbox.sharing.SharedLinkSettings(requested_visibility=dropbox.sharing.RequestedVisibility.public)
link = dbx.sharing_create_shared_link_with_settings(path=path, settings=setting)

# 共有リンク取得
links = dbx.sharing_list_shared_links(path=path, direct_only=True).links
if links is not None:
    for link in links:
        url = link.url 
        url = url.replace('www.dropbox','dl.dropboxusercontent').replace('?dl=0','')
        print(url)
