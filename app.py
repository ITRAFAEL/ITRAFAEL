from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def forward_message():
    data = request.get_json()
    
    # Extract relevant information from the incoming message
    sender = data.get('sender')
    message = data.get('message')
    
    # Process the message or collect additional information
    if message:
        # You can perform additional processing on the message if needed
        # For example, you can store it in a database or perform sentiment analysis
        
        # Forward the message to your desired recipient (Rafael in this case)
        forward_to_rafael(sender, message)
        
    return "Message received and forwarded."

def forward_to_rafael(sender, message):
    # Logic to forward the message to Rafael
    # You can use any preferred method of communication (email, API, etc.)
    # Send the relevant information to Rafael
    
    # Example: Send an email
    # You will need to set up an email server and provide the necessary credentials
    # Replace the placeholders with your own email server details
    import smtplib
    from email.message import EmailMessage
    
    sender_email = "your_email@example.com"
    recipient_email = "rafael@example.com"
    
    email_subject = f"New message from {sender}"
    email_content = f"Message: {message}"
    
    msg = EmailMessage()
    msg.set_content(email_content)
    msg['Subject'] = email_subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    with smtplib.SMTP('your_email_server_address', your_email_server_port) as server:
        server.login(sender_email, 'your_email_password')
        server.send_message(msg)

if __name__ == '__main__':
    app.run()
