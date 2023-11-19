# Lambda Function to Terminate Instances which are not in defined instance-type
import boto3

# Define List of Instance-types
type_list = ['t2.small', 't2.medium', 't2.micro', 't2.large']

# Empty Lists to get all Instancetypes and Instance-id's
InstanceType = []
all_instanceids = []

# Create EC2 Session
ec2_client = boto3.client('ec2', region_name='us-east-2')

# Get Response from all instances EC2 Session
response = ec2_client.describe_instances()['Reservations']

for instances in response:
    for type in instances['Instances']:
        # Get List of Instance id's which are in running state
        if type['State']['Name'] == "running":
            InstanceType.append(type['InstanceType'])
            all_instanceids.append(type['InstanceId'])

# Print all Instance-types and InstanceId's which are in running state.
print(InstanceType)
print(all_instanceids)

# Compare two lists for matching string
if bool(set(type_list) & set(InstanceType)) == True:
    print("Instance type is Present")
else:
    print("Instance type is not Present!!!Terminating Instances...")
    # print all instance-ids which are terminating..
    print(all_instanceids)
    # Terminate Instances which are not in defined type.
    response = ec2_client.terminate_instances(
        InstanceIds=all_instanceids)
    print("Terminated All Instances!!")
