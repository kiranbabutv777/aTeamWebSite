import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.ateamsoftsolutions.com')
browser.maximize_window()

# Finding an element in the application

browser.find_element(By.XPATH, "//span[@onclick='closePromo();']").click()
time.sleep(10)
browser.save_screenshot('Home Screen.png')
browser.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='x'])[2]/following::div[2]").click()
time.sleep(10)
browser.save_screenshot('Menus.png')
act_title = browser.title
exp_title = "Software App Development Company - Digital Professionals | aTeam Soft Solutions"

if act_title == exp_title:
    print("Test Passed")

    # Email configuration
    sender_email = "kiran@ateamsoftsolutions.com"
    receiver_email = "kiran@ateamsoftsolutions.com"
    subject = "aTeam Website Health Check"
    message = """
    Dear Team,

    I hope this email finds you well. I'm pleased to provide you with an update on the recent automated test execution activities for the aTeam Website.

    Today's execution is passed

    Thank you for your continued support

    Best Regards,

    QA Team
    """
    # Set up the MIME object
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "kiran@ateamsoftsolutions.com"
    smtp_password = "hmso ohbt onpt lvra"

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to the SMTP server
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Disconnect from the server
        server.quit()

else:
    print("Test Failed")
