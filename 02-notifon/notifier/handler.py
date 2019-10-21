import os
import requests


def post_to_slack(event, context):
    slack_webhook = os.environ['SLACK_WEBHOOK_URL']

    slack_mesg = "From {source} at {detail[StartTime]}: {detail[Description]}".format(**event)
    data = { "text": slack_mesg }
    requests.post(slack_webhook, json=data)

    print(slack_webhook)
    print(event)
    return 
