import boto3
import requests
from datetime import datetime

# ─── AWS Check ───────────────────────────────
def get_aws_summary():
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    s3 = boto3.client('s3')

    # EC2
    ec2_response = ec2.describe_instances()
    running = 0
    stopped = 0

    for r in ec2_response['Reservations']:
        for i in r['Instances']:
            if i['State']['Name'] == 'running':
                running += 1
            elif i['State']['Name'] == 'stopped':
                stopped += 1

    # S3
    s3_response = s3.list_buckets()
    bucket_count = len(s3_response['Buckets'])

    return {
        'ec2_running': running,
        'ec2_stopped': stopped,
        's3_buckets': bucket_count
    }

# ─── Website Check ───────────────────────────
def check_websites():
    sites = [
        'https://google.com',
        'https://github.com',
        'https://hub.docker.com'
    ]

    results = []

    for url in sites:
        try:
            r = requests.get(url, timeout=5)
            status = "UP" if r.status_code == 200 else f"ISSUE({r.status_code})"
            emoji = "✅" if status == "UP" else "⚠️"

        except requests.exceptions.ConnectionError:
            status = "DOWN"
            emoji = "❌"

        except requests.exceptions.Timeout:
            status = "TIMEOUT"
            emoji = "⏱️"

        results.append({
            'url': url,
            'status': status,
            'emoji': emoji
        })

    return results

# ─── Final Report ─────────────────────────────
def run_monitor():
    print("=" * 50)
    print("DevOps Monitor Report")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    # AWS
    print("\nAWS Summary:")
    aws = get_aws_summary()
    print(f" EC2 Running : {aws['ec2_running']}")
    print(f" EC2 Stopped : {aws['ec2_stopped']}")
    print(f" S3 Buckets : {aws['s3_buckets']}")

    # Websites
    print("\nWebsite Health:")
    sites = check_websites()
    for site in sites:
        print(f" {site['emoji']} {site['url']} — {site['status']}")

    print("=" * 50)

run_monitor()
