# coding: utf-8
import boto3
session = boto3.Session(profile_name='kliang-strict')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file: 
    key_file.write(key.key_material)
    
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
list(ec2.images.filter(Owners=['amazon']))
img = ec2.Image('ami-00c03f7f7f2ec15c3')
img.name
ami_name = img.name
ami_name
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owner=['amazon'], Filters=filters))
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
list(ec2_apse2.images.filter(Owners=['amazon'], Filters=filters))
img
key
instancts = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instancts
inst = instancts[0]
inst
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst
inst.public_dns_name
inst.public_ip_address
inst.wait_until_running()
inst.public_ip_address
inst.reload()
inst.public_ip_address
inst.public_dns_name
inst.security_groups
# Look up the security group. authorize incoming connections from our public ip
secgrp = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
secgrp
response = secgrp.authorize_ingress(IpPermissions=[{
'IpRanges': [{'CidrIp': '108.29.78.215/32'}], 
'FromPort':22, 
'ToPort':22, 'IpProtocol': 'TCP'}]) 
response2 = secgrp.authorize_ingress(CidrIp='108.29.78.214/32',FromPort=22,ToPort=22,IpProtocol='TCP')
response2
response2 = secgrp.revoke_ingress(CidrIp='108.29.78.214/32',FromPort=22,ToPort=22,IpProtocol='TCP')
