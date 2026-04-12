import boto3
from datetime import datetime
from botocore.exceptions import NoCredentialsError, ClientError


def get_ec2_status():
    try:
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

    except NoCredentialsError:
        print("ERROR: AWS credentials not found")
        print("Fix: Run 'aws configure'")
        return []

    except ClientError as e:
        print(f"ERROR: AWS error — {e}")
        return []


def get_s3_status():
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()

        buckets = []
        for bucket in response['Buckets']:
            buckets.append({
                'name': bucket['Name'],
                'created': str(bucket['CreationDate'])
            })

        return buckets

    except NoCredentialsError:
        print("ERROR: AWS credentials not found")
        return []

    except ClientError as e:
        print(f"ERROR: AWS error — {e}")
        return []


def print_report():
    print("=" * 50)
    print("AWS Resource Report")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    print("\nEC2 Instances:")
    instances = get_ec2_status()

    if not instances:
        print(" No instances found")
    else:
        for i in instances:
            status = "🟢" if i['state'] == 'running' else "🔴"
            print(f" {status} {i['id']} | {i['state']} | {i['type']}")

    print("\nS3 Buckets:")
    buckets = get_s3_status()

    if not buckets:
        print(" No buckets found")
    else:
        for b in buckets:
            print(f" 📦 {b['name']}")

    print("\nSummary:")
    running = sum(1 for i in instances if i['state'] == 'running')
    stopped = sum(1 for i in instances if i['state'] == 'stopped')

    print(f" EC2 Running: {running}")
    print(f" EC2 Stopped: {stopped}")
    print(f" S3 Buckets: {len(buckets)}")
    print("=" * 50)


print_report()
