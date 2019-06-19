import boto3
from os import listdir
from os.path import isfile, join

# Configuration
s3_bucket_name = "prabhat00-public"
s3_bucket_folder = "d-tools/"
backup_folder = "c:\\projects\\d-tools\\backup"

# Initialize S3
s3 = boto3.resource('s3')

# Get the file list in backup folder
files = listdir(backup_folder)

# Upload the files
for file in files:
    print("Uploading: ", file , " to: ", "s3://", s3_bucket_name + "/" + s3_bucket_folder)
    data = open(backup_folder + "\\" + file, 'rb')
    upload_location = s3_bucket_folder + file
    s3.Bucket(s3_bucket_name).put_object(Key=upload_location, Body=data)


