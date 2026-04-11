import boto3

def check_cloudwatch():
    cloudwatch = boto3.client('cloudwatch', region_name='ap-south-1')
    print("CloudWatch connected!")
    print("(Metrics will come here in future)")

check_cloudwatch()
