import boto3
import csv
 

def create_s3_client():
    client = boto3.resource('s3')    
    return client

public_accessed_read_buckets_count = 0
public_accessed_write_buckets_count = 0 
public_accessed_fullaccess_buckets_count = 0

def s3_public_buckets_count(s3_clients):
    public_accessed_read_buckets_counts, public_accessed_write_buckets_counts, public_accessed_fullaccess_buckets_counts = check_S3_buckets_grants(public_accessed_read_buckets_count, public_accessed_write_buckets_count, public_accessed_fullaccess_buckets_count, s3_clients)
    return public_accessed_read_buckets_counts, public_accessed_write_buckets_counts, public_accessed_fullaccess_buckets_counts   
def check_bucket_grant(grant_permission, bucket_name, public_accessed_read_buckets_count, public_accessed_write_buckets_count, public_accessed_fullaccess_buckets_count):
    if grant_permission == 'read':
        public_accessed_read_buckets_count += 1
    elif grant_permission == 'write':
        public_accessed_write_buckets_count += 1
    elif grant_permission == 'full_control':
        public_accessed_fullaccess_buckets_count += 1   
    
    return [public_accessed_read_buckets_count, public_accessed_write_buckets_count, public_accessed_fullaccess_buckets_count]


def check_S3_buckets_grants(public_accessed_read_buckets_count, public_accessed_write_buckets_count, public_accessed_fullaccess_buckets_count, s3_client):
    for bucket in s3_client.buckets.all():
        acl = bucket.Acl()
        for grant in acl.grants:
            #http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html
            if grant['Grantee']['Type'].lower() == 'group' \
                and grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':
                public_accessed_read_buckets_count, public_accessed_write_buckets_count, public_accessed_fullaccess_buckets_count = check_bucket_grant(grant['Permission'].lower(), bucket.name, public_accessed_read_buckets_count, public_accessed_write_buckets_count, public_accessed_fullaccess_buckets_count)
    
    return  public_accessed_read_buckets_count, public_accessed_write_buckets_count, public_accessed_fullaccess_buckets_count

