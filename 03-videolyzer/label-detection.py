# coding: utf-8
import boto3
session = boto3.Session(profile_name='kliang-strict')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='kliang-videolyzer', CreateBucketConfiguration={'LocationConstraint': session.region_name})
pathname = '~/Downloads/Pexels Videos 1460853.mp4'
path = Path(pathname).expanduser().resolve()
from pathlib import Path
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path),str(path.name))
rk_client = session.client('rekognition')
print(path.name)
response = rk_client.start_label_detection(Video={'S3Object': { 'Bucket': bucket.name, 'Name': path.name}})
response
job_id = response['JobId']
print(job_id)
result = rk_client.get_lable_detection(JobId=job_id)
result = rk_client.get_label_detection(JobId=job_id)
result
type(result)
result.keys()
result['JobStatus']
result['ResponseMedtadata']
result['ResponseMetadata']
result['Labels']
