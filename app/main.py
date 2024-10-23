from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Route for the form page
@app.route('/')
def form():
    return render_template('index.html')

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Example criteria: basic check on the name and email (you can expand this)
    if "pharmacy" in name.lower() or "pharmacy" in email.lower():
        # If criteria are met, send acceptance email
        send_email(email, "Accepted", f"Hello {name}, you have been accepted into the collaboration!")
        return f"Congratulations {name}, you've been accepted!"
    else:
        # If criteria are not met, send rejection email
        send_email(email, "Not Accepted", f"Hello {name}, unfortunately, your application was not accepted.")
        return f"Sorry {name}, you did not meet the criteria."

# Function to send an email
def send_email(recipient_email, subject, body):
    sender_email = "your-email@gmail.com"  # Replace with your email
    sender_password = "your-password"      # Replace with your email password (or app-specific password)

    # Create the email content
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Sending the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

if __name__ == '__main__':
    app.run(debug=True)
