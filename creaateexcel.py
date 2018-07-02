import csv
 
with open('example5.csv', 'w') as csvfile:
    fieldnames = ['ResourceName', 'TotalNumber', 'WithoutError', 'WithError', 'AccountId']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerows([{'ResourceName': 'EC2', 'TotalNumber': '20', 'WithoutError': '15', 'WithError': '5', 'AccountId': '1234567890'},
                      {'ResourceName': 'S3', 'TotalNumber': '20', 'WithoutError': '15', 'WithError': '5', 'AccountId': '1234567890'},
                     
                     {'ResourceName': 'ECS', 'TotalNumber': '20', 'WithoutError': '15', 'WithError': '5', 'AccountId': '1234567890'},
                     {'ResourceName': 'RDS', 'TotalNumber': '20', 'WithoutError': '15', 'WithError': '5', 'AccountId': '1234567890'},
                     {'ResourceName': 'VPC', 'TotalNumber': '20', 'WithoutError': '15', 'WithError': '5', 'AccountId': '1234567890'},
                     ])
 
print("writing complete")