import boto3

# S3オブジェクトを取得
s3 = boto3.resource('s3')

# ファイルのダウンロード
bucket = s3.Bucket('バケット名')
bucket.download_file('S3のバケット以下のpath', '保存先のpath')
