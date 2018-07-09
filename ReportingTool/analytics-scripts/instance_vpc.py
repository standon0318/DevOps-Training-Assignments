import boto3
import json
import csv
import sys

ec2 = boto3.resource('ec2', region_name='us-east-1')
vpc_name = str(sys.argv[1])
filename = str(vpc_name) + '.csv'

 


filters = [{'Name':'tag:Name', 'Values':[vpc_name]}]
vpcs = list(ec2.vpcs.filter(Filters=filters))[0]
vpcid = str(vpcs.vpc_id)
    



def ec2_describe():
    instances = ec2.instances.filter(
    Filters=[{'Name': 'vpc-id', 'Values': [vpcid]}])
    with open(filename, 'w') as csvfile: 
        fieldnames = ['instance_name', 'instance_id', 'ec2_instance_type']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for instance in list(instances.all()):    
            if instance.tags is not None:
                for tag in instance.tags:
                    if tag['Key'] == 'Name':
                        instance_name = tag['Value'] 
            writer.writerow({'instance_name': instance_name, 'instance_id': instance.id, 'ec2_instance_type': instance.instance_type})
                # writer.writerow({'instance_id': instance.id, 'ec2_instance_type': instance.instance_type})

def main():
    ec2_describe()

if __name__ == '__main__':
    main()