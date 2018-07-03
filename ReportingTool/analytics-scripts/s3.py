import boto3
import csv

def create_s3_client():
    s3_client = boto3.resource('s3')
    return s3_client

def get_all_s3_public_buckets(s3_client):
    public_accessed_read_buckets_count = 0
    public_accessed_write_buckets_count = 0
    public_accessed_fullaccess_buckets_count = 0                                
    for bucket in s3_client_connection.buckets.all():
    print(bucket.name)
    acl = bucket.Acl()
    for grant in acl.grants:
    if grant['Grantee']['Type'].lower() == 'group' \ 
    and grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':
    grant_permission = grant['Permission'].lower()

    if grant_permission == 'read':
    public_accessed_read_buckets_count += 1

    elif grant_permission == 'write':
    public_accessed_read_buckets_count += 1
    
    elif grant_permission == 'read_acp':
    public_accessed_read_buckets_count += 1
    
    elif grant_permission == 'write_acp':
    public_accessed_write_buckets_count += 1

    elif grant_permission == 'full_control':
    public_accessed_fullaccess_buckets_count += 1   
    return public_accessed_write_buckets_count