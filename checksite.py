import smtplib
import httplib
import sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

c = httplib.HTTPConnection('www.site.com')
c.request("HEAD", '')
if c.getresponse().status == 200:
    kod = "Site www.site.com not working."
else:
	sys.exit()
from_address = "my@mail.com"
to_address = "to@mail.com"
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = "Test if site is up"

msg.attach(MIMEText(kod, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(from_address, "L33tP455V0rD")
text = msg.as_string()
smtp_server.sendmail(from_address, to_address, text)
smtp_server.quit()
