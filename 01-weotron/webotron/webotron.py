# coding: utf-8
import boto3
session = boto3.Session(profile_name='kliang-strict')
s3 = session.resource ('s3')

import click


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

if __name__ == '__main__':
   # list_buckets()
    cli()
    print("hello world")
