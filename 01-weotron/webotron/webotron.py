# coding: utf-8
import boto3
session = boto3.Session(profile_name='kliang-strict')
s3 = session.resource ('s3')

import click
from botocore.exceptions import ClientError

@click.group()
def cli():
    "webotron deploys websites to AWS"
    pass

@cli.command('list_bucket_objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List bucket objects"
    for obj in s3.Bucket(bucket).objects.all(): 
        print(obj)


@cli.command('list_buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket): 
    "Create and configure S3 bucket" 
    s3_bucket = None
    try: 
        s3_bucket = s3.create_bucket(
            Bucket=bucket, 
            CreateBucketConfiguration={'LocationConstraint': session.region_name}
        )
    except ClientError as err: 
        if err.response['Error']['Code'] == 'BucketAlreadyOwnedByYou': 
            s3_bucket = s3.Bucket(bucket)
            print("Bucket {} already exists".format(bucket))
        else: 
            raise err

    policy = """
    {
      "Version":"2012-10-17",
      "Statement":[{
      "Sid":"PublicReadGetObject",
      "Effect":"Allow",
      "Principal": "*",
          "Action":["s3:GetObject"],
          "Resource":["arn:aws:s3:::%s/*"
          ]
        }
      ]
    }
    """ % s3_bucket.name
    pol = s3_bucket.Policy()
    pol.put(Policy=policy.strip())
    ws = s3_bucket.Website()
    ws.put(WebsiteConfiguration={
        'ErrorDocument': {
            'Key': 'error.html'
        },
        'IndexDocument': {
            'Suffix': 'index.html'
        }})
    url = "http://%s.s3-website.us-east-2.amazonaws.com" % s3_bucket.name
    print(f"url = {url}") 

    return


if __name__ == '__main__':
   # list_buckets()
    cli()
    print("hello world")
