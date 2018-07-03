import csv
import sys
import smtplib
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def main():
    filename = sys.argv[1]
    report_mail("AWS Daily Report", ["standon@tavisca.com"], "standon@tavisca.com", filename, "Shashank@08")
if __name__ == '__main__':
    main()     
def report_mail(Subject, RecieversList, SenderEmail, FileName, SenderEmailPassword):
    Body = emailbody(FileName)
    File_Attachment = fileattach(FileName)
    for RecieverAddress in range(len(RecieversList)):
        # Create message container - the correct MIME type is multipart/alternative here!
        MESSAGE = MIMEMultipart('alternative', None, [MIMEText(Body,'html')])
        MESSAGE['subject'] = Subject
        MESSAGE['To'] = RecieversList[RecieverAddress]
        MESSAGE['From'] = SenderEmail
        # Record the MIME type text/html.
        HTML_BODY = MIMEText(Body, 'html')
        MESSAGE.attach(HTML_BODY)
        MESSAGE.attach(File_Attachment)
        # The actual sending of the e-mail
        server = smtplib.SMTP('smtp.gmail.com:587')
        # Credentials (if needed) for sending the mail
        password = SenderEmailPassword
        server.starttls()
        server.login(SenderEmail,password)
        server.sendmail(SenderEmail, RecieversList[RecieverAddress], MESSAGE.as_string())
        server.quit()
    
#table structure 

def emailbody(FileName):
    table = ''
    with open(FileName) as csvFile: 
        reader = csv.DictReader(csvFile, delimiter=',')    
        table = '<tr class="col">{}</tr>'.format(''.join(['<th class="cell">{}</th>'.format(header) for header in reader.fieldnames])) 
        for row in reader:  
            table_row = '<tr>' 
            for fn in reader.fieldnames:            
		        table_row += '<td class="cell">{}</td>'.format(row[fn]) 
            table_row += '</tr>' 
            table += table_row
    Body = """
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
        </style>
        </head><html><body><p>Hello Team,</p>
        <p
        <h4 align="center">Daily Analysis Report</h4>

        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsRyRK0JErIu4_sNLWJQipqu1dGBR4UcKgtd3C4xfe-VtnMB7i" width="50" height="50" align="left" alt="AWS"/>

        <img src="https://prnewswire2-a.akamaihd.net/p/1893751/sp/189375100/thumbnail/entry_id/0_gbtwnru9/def_height/500/def_width/500/version/100012/type/1" width="100" height="50" align="right" alt="Tavisca Logo"/>
        <br />
        <br />
        <hr/>
        <table> 
        %s
        </table>

        <p>Regards,</p>
        <p>DevOps</p>
        </body></html>
        """ % table
    return Body

def fileattach(FileName):
    filename = FileName
    attachment = open(filename, "rb")
 
# instance of MIMEBase and named as p
    file_Attachment = MIMEBase('application', 'octet-stream')
 
# To change the payload into encoded form
    file_Attachment.set_payload((attachment).read())
 
# encode into base64    
    encoders.encode_base64(file_Attachment)
  
    file_Attachment.add_header('Content-Disposition', "attachment; filename= %s" % filename)    
    return file_Attachment


 
