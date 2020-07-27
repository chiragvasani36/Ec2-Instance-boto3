import os
print (os.environ.get('Password'))
"""
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--pass1',  help='value of pass')


args = parser.parse_args()
print(args.pass1)

import boto3
ec2_resource=boto3.resource('ec2')
response=ec2_resource.create_instances(
    ImageId='ami-08f3d892de259504d',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1
)
print(response)
"""
