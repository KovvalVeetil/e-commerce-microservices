from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Configuration for the SMTP server
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_username@example.com'
SMTP_PASSWORD = 'your_password'
EMAIL_FROM = 'your_email@example.com'

def send_email(recipient, subject, body):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Establish connection to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        # Send the email
        server.sendmail(EMAIL_FROM, recipient, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

@app.route('/notifications/email', methods=['POST'])
def send_email_notification():
    data = request.json
    recipient = data.get('recipient')
    subject = data.get('subject')
    body = data.get('body')

    if not recipient or not subject or not body:
        return jsonify({'message': 'Missing required fields'}), 400

    success = send_email(recipient, subject, body)
    if success:
        return jsonify({'message': 'Email sent successfully'}), 200
    else:
        return jsonify({'message': 'Failed to send email'}), 500

if __name__ == '__main__':
    app.run(port=5005)
