import boto3

# S3オブジェクトを取得
s3 = boto3.resource('s3') 

# ファイルのアップロード
bucket = s3.Bucket('バケット名')
bucket.upload_file('UPするファイルのpath', '保存先S3のpath')