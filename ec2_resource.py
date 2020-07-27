import os
print (os.environ.get('AWS_SECRET_ACCESS_KEY'))
import boto3
ec2_resource=boto3.resource('ec2',aws_access_key_id=os.environ.get('AWS_SECRET_ACCESS_KEY'),aws_secret_access_key=os.environ.get('AWS_ACCESS_KEY_ID'))
response=ec2_resource.create_instances(
    ImageId='ami-08f3d892de259504d',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1
)
print(response)
