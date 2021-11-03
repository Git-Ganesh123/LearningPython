import smtplib

sender = "senderName@gamil.com"
receiver = "receiverName@gmail.com"
password = "Password"
subject = "Python e-mail test"
body = "I wrote this on python"

message = f"""From: Ganesh{sender}
To: Person{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()  # start transport layer security

try:
    server.login(sender, password)
    print("Logged in")
    server.sendmail(sender, receiver, message)
    print("E-mail has been sent")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
