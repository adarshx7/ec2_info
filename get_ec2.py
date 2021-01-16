#!/usr/bin/env python

import boto3
ec2client = boto3.client('ec2', region_name='us-east-1')

print("Below are the instance running in us-east-1")

ec2instance = ec2client.describe_instances(
    Filters=[
        {
            'Name': 'instance-type',
            'Values': ['r5.large']
        }
    ],
    MaxResults=100
)
for reservation in ec2instance["Reservations"]:
    for instanceinfo in reservation["Instances"]:
 
        print(instanceinfo["InstanceId"]) #List Instance-Id of EC2 Instances under default VPC