import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "arwaghmode09@gmail.com"
password = "omxiiypohorykhcx"

receiver = "arwaghmode09@gmail.com"
context = ssl.create_default_context()

message = """\
Hi! How are you?
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    # For sender's and receiver's email address
    server.sendmail(username, receiver, message)