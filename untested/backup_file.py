import os
import dropbox

DROPBOX_ACCESS_TOKEN = '(準備で取得したアクセストークン）'
SERVER_NAME = '(バックアップサーバ名)'

def make_dropbox_backup_folder(dbx, server):
    '''サーバのバックアップ保存フォルダを探してない場合はフォルダを作成する.'''
    try:
        is_exits = False
        for entry in dbx.files_list_folder('').entries:
            if (entry.name == server):
                is_exits = True
                break

        if (is_exits == False):
            # サーバフォルダが見つからないので作成
            dbx.files_create_folder('/' + server)

    except:
        print("Error. Make Backup Folder")
        return False

    return True

def upload_file(dbx, server, file):
    '''ファイルアップロード.'''
    name = os.path.basename(file)
    remote = '/' + server + '/' + name

    with open(file, 'rb') as f:
         dbx.files_upload(f.read(), remote)


if (__name__ == "__main__"):
    dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    if (make_dropbox_backup_folder(dbx, SERVER_NAME) == False):
        print('Error. create server folder')
    else:
        upload_file(dbx, SERVER_NAME, 'daily.tar.gz')
