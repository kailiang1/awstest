# coding: utf-8
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-2:467665379466:handleLabelDetectionTopic:e8ef7efc-bd44-4471-a5f4-47e65822b31a', 'Sns': {'Type': 'Notification', 'MessageId': 'a6865b66-715d-5504-a3d5-0d4f43e2e2fd', 'TopicArn': 'arn:aws:sns:us-east-2:467665379466:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"dd5b9a92f3a1faf9ed44397f943a8533591dd9f5408a7236cb3eb108f6e63726","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1571762303663,"Video":{"S3ObjectName":"Pexels Videos 1460853.mp4","S3Bucket":"kliang-new-videolyzer123"}}', 'Timestamp': '2019-10-22T16:38:23.725Z', 'SignatureVersion': '1', 'Signature': 'RLWKa5tjIjiiYO4CdyWuBI40qRFpbJCyk9ImuUIsGKoM9x2Sd2xECHfYg5sLQWlxPz6mFELLObOyNRDWczmxn793Tc2gNI11WVKqUSERB84XdKn546f+jL7MsFcfhIqZ1+ne7J3qDuGODu9XBtCpQkvM/SVA8o9W4VDGuzWw4nLlxeY5oo8a8Btx/nHRtBDZz31rNN5iDp0sybKsj3+fmXGG+35alD2pXMtfNkBItKb40rOA691XQ5J2OQCCjIl+Fs3//GdiZdzBll1CYhtZQcG2XjgjSGZppg76/FaskLk1xZZq1xthvq/3y0LHJCZ/nk8jd5GLVYYBY28mOedJTA==', 'SigningCertUrl': 'https://sns.us-east-2.amazonaws.com/SimpleNotificationService-6aad65c2f9911b05cd53efda11f913f9.pem', 'UnsubscribeUrl': 'https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:467665379466:handleLabelDetectionTopic:e8ef7efc-bd44-4471-a5f4-47e65822b31a', 'MessageAttributes': {}}}]}
event
event.keys()
event['Records']
event['Records'][0].keys()
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion']
event['Records'][0]['EventSubscriptionArn']
event['Records'][0]['Sns']
import json
json.loads(event['Records'][0]['Sns']['Message'])
