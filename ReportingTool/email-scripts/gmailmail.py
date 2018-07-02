# Python code to illustrate Sending mail from 
# your Gmail account 

import smtplib

print("hello world")
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("standon@tavisca.com", "Shashank@08")

# message to be sent
message = "Hello From shashanktandon8"

# sending the mail
s.sendmail("standon@tavisca.com", "shashanktandon8@gmail.com", message)

# terminating the session
s.quit()
