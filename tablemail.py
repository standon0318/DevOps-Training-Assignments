from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import csv
import smtplib


me = 'standon@tavisca.com'
password = 'Shashank@08'
#server = 'smtp.gmail.com:587'
li = ["standon@tavisca.com"]
i = 1
table = ''
with open('Reporting tool.csv') as csvFile: 
    reader = csv.DictReader(csvFile, delimiter=',')    
    table = '<tr class="col">{}</tr>'.format(''.join(['<th class="cell">{}</th>'.format(header) for header in reader.fieldnames])) 
    for row in reader:  
        table_row = '<tr>' 
        for fn in reader.fieldnames:            
			table_row += '<td class="cell">{}</td>'.format(row[fn]) 
        table_row += '</tr>' 
        table += table_row

      

#text = """
#Hello Team.

#Here is daily report data:

#{table}

#Regards,

#DevOps"""

html = """
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>html title</title>
<style type="text/css" media="screen">

table{
       background-color: white;
       empty-cells:hide;
       Border:2px solid black;
 }

td.cell{
    border: 1px solid;
	color: white;
    text-align: left;
    padding: 8px;
	background-color: grey;
}
th.cell{
	color: red;
    text-align: center;
    padding: 8px;
	
}
tr.col:nth-child(even){background-color: grey;}

</style>
</head><html><body><p>Hello Team,</p>
<p>Here is daily report data:</p>

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsRyRK0JErIu4_sNLWJQipqu1dGBR4UcKgtd3C4xfe-VtnMB7i" width="50" height="50" align="left" alt="AWS"/>

<img src="https://prnewswire2-a.akamaihd.net/p/1893751/sp/189375100/thumbnail/entry_id/0_gbtwnru9/def_height/500/def_width/500/version/100012/type/1" width="100" height="50" align="right" alt="Tavisca Logo"/>
<br />
<br />
<hr />
 <table> 
%s
</table>

<p>Regards,</p>
<p>DevOps</p>
</body></html>""" % table

message = MIMEMultipart(
"alternative", None, [MIMEText(html,'html')])
filename = "Reporting tool.csv"
attachment = open("Reporting tool.csv", "rb")
 
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
