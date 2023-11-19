"Create EC2 Instances based on the input."
import boto3
no_of_vm = int(input("Please Enter The Number Of VMs You Want to Deploy Between 1 to 3:"))
ec2client = boto3.client('ec2', region_name='us-east-1')
sg='sg-0664fad55261dd1fa'
subnets = ['subnet-0d124b5eb12011584', 'subnet-027c6daa4133a59ff', 'subnet-0e595f62126dd8670']
userdata = '''#!/bin/bash
sudo apt update
sudo apt install -y nginx
sudo service nginx start
echo "<div><h1>$(cat /etc/hostname)</h1></div>" >> /var/www/html/index.nginx-debian.html
'''
for i in range(no_of_vm):
    create_ec2_instances = ec2client.run_instances(
    ImageId="ami-057b8cf7bc7d04fca",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName="LaptopKey",
    SubnetId=subnets[i],
    UserData=userdata,
    SecurityGroupIds=[
        sg,
    ],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
                            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'WelcomeServer00'+str(i+1)
                },
                {
                    'Key': 'Env',
                    'Value': 'Development'
                },
            ]
        },
    ]
)

