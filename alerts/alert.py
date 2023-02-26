import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import datetime

def terminal(text):
    current_time = datetime.datetime.now()
    print(str(current_time) + "  |  " + text)
    # time.sleep(1)