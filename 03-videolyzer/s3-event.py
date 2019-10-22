# coding: utf-8
event  = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-2', 'eventTime': '2019-10-21T20:35:36.726Z', 'eventName': 'ObjectCreated:CompleteMultipartUpload', 'userIdentity': {'principalId': 'AWS:AIDAWZYYHMCFLTN6NLGRG'}, 'requestParameters': {'sourceIPAddress': '108.29.78.215'}, 'responseElements': {'x-amz-request-id': 'C699452200161EBB', 'x-amz-id-2': 'dLT+k7LolQBjohJTXevfBjSBnkMvd2JqBAj8wliIw7OqlifjFhppze+ipVSv9ttVt/OdGfXeN64='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'e6694d0e-c022-40e8-a0ac-528c1a9e00fa', 'bucket': {'name': 'kliang-new-videolyzer123', 'ownerIdentity': {'principalId': 'AADXIJYXN49FU'}, 'arn': 'arn:aws:s3:::kliang-new-videolyzer123'}, 'object': {'key': 'woman+camera.mp4', 'size': 24842917, 'eTag': '1fa0417290251e68ba9be5dcaa00c2fb-3', 'sequencer': '005DAE16955E33D936'}}}]}
event
event['Records][0]
event['Records'][0]
event['Records'][0]['bucket']
event['Records'][0]['bucket']['name']
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
