import boto3
import csv

from iam import *
from ec2 import *
from autoscaling import *
from s3 import *


def get_account_id():
    iam = boto3.resource('iam')
    account_id = iam.CurrentUser().arn.split(':')[4]
    return account_id

def main():
    with open('reports.csv', 'w') as csvfile: 
        fieldnames = ['Account_ID', 'EC2_Untagged_Instances', 'EC2_Running_Instances','EC2_Stopped_Instances','Autocsaling_Unused_LC','Users_without_MFA','S3_Public_Read','S3_Public_Write','S3_Public_FullAccess']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        account_id = get_account_id()
        ec2client = create_ec2_client()
        iamclient = create_iam_client()
        s3_client = create_s3_client()
        autoscalingclient = create_autoscaling_client()
        untagged_count = get_all_running_ec2_instances_without_name_tag(ec2client)
        running_instance_count, stopped_instance_count = get_running_and_stopped_instance_count(ec2client)
        unused_lc_count = get_unassociated_launch_configurations(autoscalingclient)
        users_without_mfa_count = get_list_of_users_without_mfa(iamclient)
        public_accessed_read_buckets_count, public_accessed_write_buckets_count, public_accessed_fullaccess_buckets_count = s3_public_buckets_count(s3_client)
        writer.writerow({'Account_ID': account_id, 'EC2_Untagged_Instances': untagged_count, 'EC2_Running_Instances': running_instance_count, 'EC2_Stopped_Instances': stopped_instance_count, 'Autocsaling_Unused_LC': unused_lc_count, 'Users_without_MFA': users_without_mfa_count, 'S3_Public_Read': public_accessed_read_buckets_count, 'S3_Public_Write': public_accessed_write_buckets_count, 'S3_Public_FullAccess': public_accessed_fullaccess_buckets_count })
        csvfile.close()
        return csvfile
       
if __name__ == '__main__':
    main()