import boto3
from botocore.exceptions import ClientError
regions = ['us-east-1','us-east-2']
KName='HelloNewKey'
public_key='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCzsEivxCf8u9S9NbpZsCrRfshmy8BWUKuxNvmrDOObMALeNmF0T4Oqog2yXDMrOO6Iz9fTpNScPe9CzX5mtxMMK09hQbD1CZaQImYkq2U1UmO4pFgkRsszfvAAqbRPtaa2LTjE7fGOKd/B2S+ve4xD5/uWn3h8N2QODv2UKKwqChMXMthCL9rLuHmxxFrWNSkY2lq42kBN1o4shBbi18vH6liqbK6wkRQCYLtB1TJUDFoMTtydVZS+iXFuxPh6rHoEC+52TriVuHPhaHZYZFwO1GGsKWBsMCtZt83lN/tU/AO3i3VlL5n1JPSN/jqMpqR8pZnHFlTed4sMoMFgGcQx'
for reg in regions:
    ec2 = boto3.client('ec2',region_name=reg)
    try:
        get_keypairs = ec2.describe_key_pairs(KeyNames=[KName])
        print(get_keypairs)
    except ClientError:
        print('IMPORTING KEYPAIR...')
        response = ec2.import_key_pair(KeyName=KName, PublicKeyMaterial=public_key)
    # else:
    #     response = ec2.import_key_pair(KeyName=KName, PublicKeyMaterial=public_key)
    finally:
        ec2.delete_key_pair(KeyName=KName)
