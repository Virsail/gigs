import os
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to Events Pub'
    sender = 'virsaileric@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/newsemail.txt',{"name": name})
    html_content = render_to_string('email/newsemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

message = Mail(
    from_email='virsaileric@gmail.com',
    to_emails='ericmbagaya@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)