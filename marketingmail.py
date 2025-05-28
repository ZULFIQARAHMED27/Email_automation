import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Function to send marketing emails
def send_marketing_emails(file_path, sender_email, sender_password):
    # Read the Excel file
    client_data = pd.read_excel(file_path)

    # Check if the required columns exist
    if 'Name' not in client_data.columns or 'Email' not in client_data.columns:
        print("Error: Excel file must contain 'Name' and 'Email' columns.")
        return

    # Email content template
    email_subject = "Exclusive Offer Just for You!"
    email_body_template = """Dear {name},

We are excited to bring you our latest offer. Explore our exclusive products and services today. Don't miss out!

Best regards,
Your Company Team
"""

    # SMTP setup
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Connect to the SMTP server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        print("Logged in successfully.")
    except Exception as e:
        print(f"Failed to connect to the email server: {e}")
        return

    # Send emails
    for index, row in client_data.iterrows():
        recipient_name = row['Name']
        recipient_email = row['Email']

        # Personalize the email
        email_body = email_body_template.format(name=recipient_name)

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = email_subject
        msg.attach(MIMEText(email_body, 'plain'))

        try:
            server.send_message(msg)
            print(f"Email sent to {recipient_name} ({recipient_email})")
        except Exception as e:
            print(f"Failed to send email to {recipient_name} ({recipient_email}): {e}")

        # Wait for 15 seconds before sending the next email
        time.sleep(15)

    # Close the SMTP server connection
    server.quit()
    print("All emails have been sent.")

# Usage example
if __name__ == "__main__":
    excel_file_path = input("Enter the path to the Excel file: ")
    company_email = input("Enter your company Gmail address: ")
    company_email_password = input("Enter your Gmail password: ")

    send_marketing_emails(excel_file_path, company_email, company_email_password)

#Email: syzaglobal@gmail.com
#App specific Password: jgky pakg pcgd kwzh