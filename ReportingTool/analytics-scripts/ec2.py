import boto3
import csv

def create_ec2_client():

    client = boto3.resource('ec2')    
    return client

def get_running_and_stopped_instance_count(client):

    running_instance_Count = 0 
    stopped_instance_Count = 0

    running_instances = client.instances.filter(Filters=[
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ])

    stopped_instances = client.instances.filter(Filters=[
        {
            'Name': 'instance-state-name', 
            'Values': ['stopped']
        }
    ])
 
    for instance in running_instances:
        running_instance_Count += 1
    for instances in stopped_instances:
        stopped_instance_Count += 1
    
    return running_instance_Count, stopped_instance_Count


def get_all_running_ec2_instances_without_name_tag(client):
    filters = [
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
                                    
    instances = client.instances.filter(Filters=filters)
    RunningInstances = []
    for instance in instances:
        tag_count = 0
        for tags in instance.tags:
            if tags["Key"] == 'Name':
                tag_count += 1 
        if tag_count == 0:
            print(instance.id,"doesn't have a name tag present in it")
            RunningInstances.append(instance.id)
    untagged_count = 0
    for instance in RunningInstances:
        untagged_count += 1
        print(instance)
    
    return untagged_count





    


