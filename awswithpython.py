import boto3
ec2 = boto3.client('ec2')
des_inst = ec2.describe_instances()
print(des_inst)
# Create_Keypair--------
'''
resp_keypair = ec2.create_key_pair(KeyName='key_final')
print(resp_keypair['KeyMaterial'])
file = open('key_final.pem', 'w')
file.write(resp_keypair['KeyMaterial'])
file.close
'''
# Create_SecurityGroup-----------
'''
des_sec = ec2.describe_security_groups()
print(des_sec)
'''
'''
resp_sg = ec2.create_security_group(
    GroupName='sg_final',
    Description='sg_final',
    VpcId='vpc-034b89eef7dda70cd'
)

gid = resp_sg['GroupId']
print(gid)
ec2.authorize_security_group_ingress(
    GroupId=gid,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        },
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
    ]
)
'''
des_sec = ec2.describe_security_groups()
print(des_sec)

# Create Instance--------
ec2_resource = boto3.resource('ec2')
instances = ec2_resource.create_instances(
    ImageId='ami-0e1d30f2c40c4c701',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='key_final',
    BlockDeviceMappings=[
        {
            'DeviceName': "/dev/xvda",
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 20
            }
        }

    ],
    SecurityGroups=['sg_final']
)
