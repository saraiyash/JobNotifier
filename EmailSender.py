import datetime
import smtplib
from email.message import EmailMessage
import pandas as pd
from jproperties import Properties

configs = Properties()

with open('credentials.properties', 'rb') as config_file:
    configs.load(config_file)

class Sender:
    @staticmethod
    def csv_to_html():
        print("csv_to_html()")
        df = pd.read_csv("Jobs.csv")
        df = df.to_html()
        return df

    @staticmethod
    def send_email():
        print("send_email()")
        today = datetime.date.today()
        email_address = (configs.get("email_address")).data
        email_password = (configs.get("email_password")).data
        recepients = ((configs.get("recepients")).data).split(';')

        msg = EmailMessage()
        msg["Subject"] = "New Jobs - " + (today.strftime("%b %d %Y"))
        msg["From"] = email_address
        msg["To"] = recepients

        msg.set_content("Hello friends, Plaintext lelo!")

        html_content = Sender.csv_to_html()

        print(html_content)

        msg.add_alternative("""Content = {}
      """.format(Sender.csv_to_html()), subtype="html")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
            print("Message sent")

Sender.send_email()