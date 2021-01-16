#!/usr/bin/env python

import boto3
ec2client = boto3.client('ec2')
# Select required AWS Region
regions = ec2client.describe_regions(
    Filters=[
        {
            'Name': 'region-name',
            'Values': ['us-east-1']
        }
    ],
    AllRegions=False
)
for region in regions["Regions"]:
    print("Below are the instance running in " + region["RegionName"])  

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