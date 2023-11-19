"Find S3 Buckets Which Are Empty"
import boto3
s3_client = boto3.client('s3', region_name='us-east-1')
list_buckets = s3_client.list_buckets().get('Buckets', [])
bucket_list = [bucket['Name'] for bucket in list_buckets]
#print(bucket_list)
for bucket in bucket_list:
    obj_count = s3_client.list_objects(Bucket=bucket)
    #print(bucket)
    #print(obj_count.keys())
    try:
        print(obj_count['Contents'])
        pass
    except KeyError:
        print(f'Bucket {bucket} is empty')

