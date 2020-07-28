import os
import boto3

print(os.environ.get('ACCESS_KEY1'))
print(os.environ.get('SEC_VALUE1'))
ec2_resource=boto3.resource('ec2',aws_access_key_id=os.environ.get('ACCESS_KEY1'),aws_secret_access_key=os.environ.get('SEC_VALUE1'),region_name='us-east-1')
response=ec2_resource.create_instances(
    ImageId='ami-08f3d892de259504d',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1
)
print(response)

