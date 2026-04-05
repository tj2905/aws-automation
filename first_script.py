import boto3
# S3 se connect
s3=boto3.client('s3')
# Buckets list
response=s3.list_buckets()
print("S3 buckets in my account : ")
buckets=response['Buckets']
if not buckets:
    print("No bucket but connection successful!")
else:
    for bucket in buckets:
        printf(f" {bucket['Name']}")

