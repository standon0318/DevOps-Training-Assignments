import csv
ResourcesName = "IAM"
column1 = "Total Users"
column2 = "MFA Enabled"
column3 = "Without MFA"
column4 = "AccountId"
column5 = "xyz"
with open('report1.csv', 'w') as csvfile:
    fieldnames = ['ResourceName', '$column1', '$column2', '$column3', '$column4', '$column4', '$column5', '$column4', '$column4', '$column4', '$column4', '$column4', '$column4']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerows([{'ResourceName': '$ResourceName', '$column1': '20', '$column2': '15', '$column3': '5', '$column4': '1234567890', '$column5': '----', '$column4': '1234567890', '$column4': '1234567890', '$column4': '1234567890', '$column4': '1234567890', '$column4': '1234567890', '$column4': '1234567890', '$column4': '1234567890'}
                      #{'ResourceName': 'S3', 'TotalNumber': '20', 'WithoutError': '15', 'WithError': '5', 'AccountId': '1234567890'},
                     
                     #{'ResourceName': 'ECS', 'TotalNumber': '20', 'WithoutError': '15', 'WithError': '5', 'AccountId': '1234567890'},
                     #{'ResourceName': 'RDS', 'TotalNumber': '20', 'WithoutError': '15', 'WithError': '5', 'AccountId': '1234567890'},
                     #{'ResourceName': 'VPC', 'TotalNumber': '20', 'WithoutError': '15', 'WithError': '5', 'AccountId': '1234567890'},
                     ])
 
print("writing complete")