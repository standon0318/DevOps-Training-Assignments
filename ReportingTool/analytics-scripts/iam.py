import boto3
import csv

def create_iam_client():

    client = boto3.client('iam')
    return client

def get_list_of_users_without_mfa(client):

    users_without_mfa_count = 0
    response = client.list_users()
    users = response.get('Users')
    for user in users:
        user_name = user.get('UserName')
        if "bot" not in user_name: 
            mfa_enabled = client.list_mfa_devices(UserName = user_name)
            name = mfa_enabled.get('MFADevices')
            if len(name) == 0:
                users_without_mfa_count += 1
            
    return users_without_mfa_count