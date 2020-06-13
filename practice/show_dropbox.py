import dropbox

# brew cask install dropbox
# pip install dropbox

dbx = dropbox.Dropbox(ACCESS_TOKEN)
target_dir = ''
res = dbx.files_list_folder(target_dir, recursive=True)

# 結果配列
#res.entries

# 続きの有無
#res.has_more

# has_more = Trueの場合、
# files_list_folder_continue
# res.cursor

# 指定ディレクトリ以下すべてを再帰的に取得
def __get_files_recursive(res):
    for entry in res.entries:
        print(entry.path_display)

    if (res.has_more):
        res2 = dbx.files_list_folder_continue(res.cursor)
        __get_files_recursive(res2)

res = dbx.files_list_folder(target_dir, recursive=True)
__get_files_recursive(res)

# ファイルのみ取得
for entry in res.entries:
    ins = type(entry)
    if ins is not dropbox.files.FileMetadata:
        continue

    print(entry.path_display)

import dropbox

class MyDropbox():
    DB_ACCESS_TOKEN = 'XXXXXXXXXX'
    DB_ROOT_DIR = '/指定フォルダ'

    def __init__(self):
        self.dbx = dropbox.Dropbox(self.DB_ACCESS_TOKEN)

    def viewFiles(self):
        res = self.dbx.files_list_folder(self.DB_ROOT_DIR, recursive=True)

        self.__get_files_recursive(res)

    def __get_files_recursive(self, res):
        for entry in res.entries:
            ins = type(entry)
            if ins is not dropbox.files.FileMetadata: #ファイル以外（＝フォルダ）はスキップ
                continue

            link = self.__get_shared_link(entry.path_lower)
            if bool(link):
                print(entry.path_display)
                print(link)

        if res.has_more:
            res2 = self.dbx.files_list_folder_continue(res.cursor)
            self.__get_files_recursive(res2)

    def __get_shared_link(self, path):
        links = self.dbx.sharing_list_shared_links(path=path, direct_only=True).links

        if links is not None:
            for link in links:
                return link.url #1件目

        return self.__create_shared_link(path)

    def __create_shared_link(self, path):
        setting = dropbox.sharing.SharedLinkSettings(requested_visibility=dropbox.sharing.RequestedVisibility.public)
        link = self.dbx.sharing_create_shared_link_with_settings(path=path, settings=setting)

        return link.url
