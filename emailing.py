import os
import smtplib
import imghdr
from email.message import EmailMessage

SENDER = 'programmingofficialacc@gmail.com'
PASSWORD = os.getenv("WEBCAM")
RECEIVER = 'programmingofficialacc@gmail.com'


def send_email(image_path):
    print("Send Email Function Started!")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content,
                                 maintype="image",
                                 subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("Send Email Function Ended!")


# Following code runs only when this .py is executed not when called by another .py file
if __name__ == "__main__":
    send_email("images/24.png")