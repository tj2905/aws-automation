import boto3
import json
s3 = boto3.client('s3', region_name='ap-south-1')
# Unique bucket name — globally unique hona chahiye
BUCKET_NAME = 'tanay-devops-april-2026'
# Step 1 — Bucket banao
print("Bucket bana raha hoon...")
try:
   s3.create_bucket(
       Bucket=BUCKET_NAME,
       CreateBucketConfiguration={
           'LocationConstraint': 'ap-south-1'
       }
   )
   print(f" Bucket created: {BUCKET_NAME}")
except Exception as e:
    print(f" Bucket error: {e}")
# Step 2 — Test file banao locally
with open('test_file.txt', 'w') as f:
    f.write("Yeh meri pehli S3 file hai!")
# Step 3 — Upload karo
print("File upload kar raha hoon...")
s3.upload_file('test_file.txt', BUCKET_NAME, 'my-first-upload.txt')
print(" File uploaded!")
# Step 4 — List karo — verify
print("Bucket contents:")
response = s3.list_objects_v2(Bucket=BUCKET_NAME)
for obj in response.get('Contents', []):
    print(f" {obj['Key']} — {obj['Size']} bytes")
