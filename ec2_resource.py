import os
print('This is boto3...')
print (os.environ.get('Password'))
"""import boto3
ec2_resource=boto3.resource('ec2')
response=ec2_resource.create_instances(
    ImageId='ami-08f3d892de259504d',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1
)
print(response)
"""
