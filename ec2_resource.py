import os
import boto3
ec2_session =boto3.session.Session(aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),region_name='us-east-1')
ec2_resource=ec2_session.resource('ec2')
response=ec2_resource.create_instances(
    ImageId='ami-08f3d892de259504d',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1
)
print(response)
