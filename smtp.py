import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create a multipart message object
    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Create both plain text and HTML versions of the email
    text = 'This is a plain text email.'
    html = f'<html><body><>{message}</h1></body></html>'

    # Attach the plain text and HTML versions to the email
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    # SMTP server settings for Outlook
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587

    try:
        # Create a secure SSL/TLS connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to your Outlook email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print("Error sending email:", str(e))

    finally:
        # Close the connection to the SMTP server
        server.quit()

# Example usage
sender_email = "senthilsomeshwar2002@gmail.com"
sender_password = 'SenthilSundar@2002'
recipient_email = 'senthilsomeshwar2002@gmail.com'
subject = 'Hello from Python'
message = 'This is an HTML email sent using smtplib and Outlook.'

send_email(sender_email, sender_password, recipient_email, subject, message)