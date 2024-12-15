import os
import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Price_Tracker:
    def __init__(self, smtp_server, smtp_port, email, heslo):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.heslo = heslo

    def get_price(self, url, CSS):
        driver = webdriver.Chrome()
        try:
            driver.get(url)
            driver.implicitly_wait(10)
            price_element = driver.find_element(By.CLASS_NAME, CSS)
            return price_element.text
        except Exception as e:
            print(f"Error during price retrieval: {e}")
            return None
        finally:
            driver.quit()  # Close browser here

    def email_send(self, subject, body, recipient):
        try:
            message = MIMEMultipart()
            message['From'] = self.email
            message['To'] = recipient
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.email, self.heslo)
                server.sendmail(self.email, recipient, message.as_string())
        except Exception as e:
            print(f"Error sending email: {e}")

    def periodic_tracker(self, url, CSS, recipient, interval_sec):
        while True:
            price = self.get_price(url, CSS)
            if price:
                print(f"Price {price}. Sending email...")
                self.email_send(
                    subject="Price Alert!",
                    body=f"The current price is: {price}",
                    recipient=recipient
                )
            else:
                print("Failed to retrieve price. Retrying after the interval...")
            time.sleep(interval_sec)

if __name__ == "__main__":
    # Email and SMTP server setup
    smtp_server = "smtp.seznam.cz"
    smtp_port = 465
    email = "deniska.matejkova@seznam.cz"
    password = os.environ.get("MAIL_PWD")  # Get password from environment variable

    # Create an instance of the Price_Tracker class
    tracker = Price_Tracker(smtp_server, smtp_port, email, password)

    # Parameters for tracking
    alza_url = "https://www.alza.cz/iphone-16-pro-128gb-cerny-titan-d12541644.htm"
    price_class_name = "price-box__price"
    receiver_email = "deniska.matejkova@seznam.cz"
    interval_seconds = 3600  # Interval check every hour

    # Start periodic tracking
    tracker.periodic_tracker(alza_url, price_class_name, receiver_email, interval_seconds)