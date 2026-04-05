import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')

response = ec2.describe_instances()

reservations = response['Reservations']

print("EC2 Instances:")

if not reservations:
    print("Koi instance nahi hai")
else:
    for reservation in reservations:
        for instance in reservation['Instances']:
            print(f"ID: {instance['InstanceId']}")
            print(f"State: {instance['State']['Name']}")
            print(f"Type: {instance['InstanceType']}")
            
            # BONUS (real-world useful)
            print(f"Launch Time: {instance['LaunchTime']}")
            
            print("---")
