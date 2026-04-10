import boto3

s3 = boto3.client('s3', region_name='ap-south-1')

BUCKET_NAME = 'tanay-devops-april-2026'

def list_files():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    return response.get('Contents', [])

def delete_file(filename):
    s3.delete_object(Bucket=BUCKET_NAME, Key=filename)
    print(f" Deleted: {filename}")

def cleanup():
    print("Files before cleanup:")
    files = list_files()

    if not files:
        print(" No files found")
        return

    for f in files:
        print(f" {f['Key']}")

    # Delete files
    print("\nCleanup started...")
    for f in files:
        delete_file(f['Key'])

    # Verify
    print("\nFiles after cleanup:")
    remaining = list_files()
    if not remaining:
        print(" Bucket empty — cleanup successful!")

cleanup()
