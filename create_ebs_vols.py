import boto3
client = boto3.client('ec2')
num = int(input("Enter The Volume Count Between 1 to 5:"))
for I in range(num):
    client.create_volume(
        AvailabilityZone='us-east-1a',
        VolumeType='gp2',
        Size = 1,
    TagSpecifications=[
        {
            'ResourceType': 'volume',
                            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'EBSVOL00'+str(I+1)
                },
                {
                    'Key': 'Env',
                    'Value': 'Development'
                },
            ]
        },
    ]
    )