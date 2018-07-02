import csv
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import smtplib
 
me = 'standon@tavisca.com'
password = 'Shashank@08'
#server = 'smtp.gmail.com:587'
li = ["hverma@tavisca.com", "shashanktandon8@gmail.com"]

text = """
Hello Team.

Here is daily report data:

{table}

Regards,

DevOps"""

html = """
<html><body><p>Hello Team,</p>
<p>Here is daily report data:</p>
{table}
<p>Regards,</p>
<p>DevOps</p>
</body></html>
"""

with open('example5.csv') as input_file:
    reader = csv.reader(input_file)
    data = list(reader)

#text = text.format(table=tabulate(data, headers="firstrow", tablefmt="grid"))
html = html.format(table=tabulate(data, headers="firstrow", tablefmt="html"))
message = MIMEMultipart(
"alternative", None, [MIMEText(text), MIMEText(html,'html')])
filename = "example5.csv"
attachment = open("example5.csv", "rb")
 
# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')
 
# To change the payload into encoded form
p.set_payload((attachment).read())
 
# encode into base64
encoders.encode_base64(p)
  
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
# attach the instance 'p' to instance 'msg'
message.attach(p)
 
for i in range(len(li)):
	message['Subject'] = "Daily Analysis report"
	message['From'] = me
	message['To'] = li[i]
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(me, password)
	server.sendmail(me, li[i], message.as_string())
	server.quit()
