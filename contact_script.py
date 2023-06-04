import smtplib
from email.message import EmailMessage

def send_email(sender_name, sender_email, message):
    # Replace the placeholders with your own email server details
    email_server = "your_email_server_address"
    email_port = your_email_server_port
    email_username = "your_email_username"
    email_password = "your_email_password"
    recipient_email = "your_email@example.com"
    
    email_subject = f"New message from {sender_name}"
    email_content = f"Sender Email: {sender_email}\n\nMessage: {message}"
    
    msg = EmailMessage()
    msg.set_content(email_content)
    msg['Subject'] = email_subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    with smtplib.SMTP(email_server, email_port) as server:
        server.login(email_username, email_password)
        server.send_message(msg)

def collect_user_info():
    sender_name = input("Your Name: ")
    sender_email = input("Your Email: ")
    message = input("Your Message: ")
    
    send_email(sender_name, sender_email, message)
    print("Message sent successfully!")

# Entry point of the script
if __name__ == "__main__":
    collect_user_info()
