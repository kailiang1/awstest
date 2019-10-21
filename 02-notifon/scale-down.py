# coding: utf-8
import boto3
session = boto3.Session(profile_name='kliang-strict')
as_client = session.client('autoscaling')
#as_client.describe_auto_scaling_groups()
#as_client.describe_policies()
print(as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Down'))
#print(as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='scale up'))
