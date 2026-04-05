import boto3
from datetime import datetime


def get_ec2_status():
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    response = ec2.describe_instances()

    instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                'id': instance['InstanceId'],
                'state': instance['State']['Name'],
                'type': instance['InstanceType']
            })

    return instances


def get_s3_status():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    buckets = []
    for bucket in response['Buckets']:
        buckets.append({
            'name': bucket['Name'],
            'created': str(bucket['CreationDate'])
        })

    return buckets


def print_report():
    print("=" * 50)
    print("AWS Resource Report")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    # EC2 Report
    print("\nEC2 Instances:")
    instances = get_ec2_status()

    if not instances:
        print(" No instances found")
    else:
        for i in instances:
            status = "🟢" if i['state'] == 'running' else "🔴"
            print(f" {status} {i['id']} | {i['state']} | {i['type']}")

    # S3 Report
    print("\nS3 Buckets:")
    buckets = get_s3_status()

    if not buckets:
        print(" No buckets found")
    else:
        for b in buckets:
            print(f" 📦 {b['name']}")

    # Summary
    print("\nSummary:")
    running = sum(1 for i in instances if i['state'] == 'running')
    stopped = sum(1 for i in instances if i['state'] == 'stopped')

    print(f" EC2 Running: {running}")
    print(f" EC2 Stopped: {stopped}")
    print(f" S3 Buckets: {len(buckets)}")
    print("=" * 50)


# Run
print_report()
