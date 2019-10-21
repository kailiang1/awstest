# coding: utf-8
import requests
url ='https://hooks.slack.com/services/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'
data = { "text": "Hello from python" }
requests.post(url, json=data)
get_ipython().run_line_magic('save', 'post_slack.py')
