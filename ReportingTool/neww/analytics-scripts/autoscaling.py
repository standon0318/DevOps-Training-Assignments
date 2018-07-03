import boto3
import csv

def create_autoscaling_client():

    client = boto3.client('autoscaling')
    return client



def get_unassociated_launch_configurations(client):

    unassociated_launch_configurations = []
    autoscaling_groups_response = client.describe_auto_scaling_groups()
    launch_configurations_response = client.describe_launch_configurations()
    attached_lc = 0
    launch_configurations = launch_configurations_response.get('LaunchConfigurations')
    autoscaling_groups =  autoscaling_groups_response.get('AutoScalingGroups')
    for lc in launch_configurations:
        lc_name = lc.get('LaunchConfigurationName')
        attached_lc = 0
        for asg in autoscaling_groups:
            if lc_name == asg.get('LaunchConfigurationName'):
                attached_lc += 1
        if attached_lc == 0 :
            unassociated_launch_configurations.append(lc_name)
            
    return len(unassociated_launch_configurations)
    
            
        
    