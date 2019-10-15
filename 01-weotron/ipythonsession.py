# coding: utf-8
import boto3
session = boto3.Session(profile_name='kliang-strict')
s3 = session.resource ('s3')
for bucket in s3.buckets.all(): 
    print(bucket)
