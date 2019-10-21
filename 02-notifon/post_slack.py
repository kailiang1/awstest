# coding: utf-8
import requests
url ='https://hooks.slack.com/services/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'
data = { "text": "2Hello from python" }
response = requests.post(url, json=data)
print(f"Response : {response}")
