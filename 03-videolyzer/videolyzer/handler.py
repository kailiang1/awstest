import urllib
import boto3

def start_label_detection(bucket, key): 
    rk_client = boto3.client('rekognition')
    response = rk_client.start_label_detection(
        Video={
            'S3Object': {
                'Bucket': bucket, 
                'Name': key
            }
        })
    print("RK response: {}".format(response))
    return


def start_processing_video(event, context): 
    
    for record in event['Records']: 
        start_label_detection(
            record['s3']['bucket']['name'], 
            urllib.parse.unquote_plus(record['s3']['object']['key'])
        )

    return
