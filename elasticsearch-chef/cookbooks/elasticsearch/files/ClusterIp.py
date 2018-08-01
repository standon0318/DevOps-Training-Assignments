#!/usr/local/bin/python2.7

import boto3
import sys

InstanceId = str(sys.argv[1]) 

def InitializeASGClient():
    client = boto3.client('autoscaling',region_name = "us-east-1")
    return client

def InitializeEC2Client():
    client = boto3.client('ec2',region_name = "us-east-1")
    return client

def GetASGName(client):
    response = client.describe_auto_scaling_instances(
    InstanceIds=[InstanceId])
    AutoScalingInstances = response.get('AutoScalingInstances')
    for AutoScalingInstance in AutoScalingInstances:
        return AutoScalingInstance.get('AutoScalingGroupName')

def GetInstanceIpAddress(ec2client,client,ASGName):
    response = client.describe_auto_scaling_groups(
    AutoScalingGroupNames=[ASGName])
    AutoScalingGroups = response.get('AutoScalingGroups')
    InstanceIDList = []
    for AutoScalingGroup in AutoScalingGroups:
        InstancesList = AutoScalingGroup.get('Instances')
        for Instance in InstancesList:
            InstanceIDList.append(str(Instance.get('InstanceId')))

    InstanceIPList = []
    response = ec2client.describe_instances(InstanceIds=InstanceIDList)
    for reservation in response.get('Reservations'):
        for instance in reservation.get('Instances'):
            InstanceIPList.append(instance.get('PrivateIpAddress'))

    SeedIps = ','.join(InstanceIPList)
    return SeedIps

def main():
    client = InitializeASGClient()
    ec2client = InitializeEC2Client()
    ASGName = GetASGName(client)
    SeedIps = GetInstanceIpAddress(ec2client,client,ASGName)
    exit(SeedIps)

if __name__ == '__main__':
    main()#!/usr/local/bin/python2.7
