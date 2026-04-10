import boto3
import os

s3 = boto3.client('s3', region_name='ap-south-1')

BUCKET_NAME = 'tanay-devops-april-2026'

# Step 1 — List bucket contents
print("Bucket contents:")

response = s3.list_objects_v2(Bucket=BUCKET_NAME)
files = response.get('Contents', [])

if not files:
    print(" Bucket is empty")
else:
    for obj in files:
        print(f" {obj['Key']} — {obj['Size']} bytes")

# Step 2 — Download files
print("\nDownloading files...")

download_folder = 'downloads'
os.makedirs(download_folder, exist_ok=True)

for obj in files:
    filename = obj['Key']
    local_path = os.path.join(download_folder, filename)

    s3.download_file(BUCKET_NAME, filename, local_path)
    print(f" Downloaded: {filename} → {local_path}")

print("\nDone!")
