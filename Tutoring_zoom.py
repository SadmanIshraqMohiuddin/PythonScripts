import datetime
import webbrowser
import urllib.parse

# Get current day
current_day = datetime.datetime.now().strftime("%A")

# Dictionary mapped: days to email recipients
email_recipients = {
    "Monday": ["student_email@domain.com"], ["student_email@domain.com"],
    "Tuesday": ["student_email@domain.com"], ["student_email@domain.com"],
    "Wednesday": ["student_email@domain.com"], ["student_email@domain.com"],
    "Thursday": ["student_email@domain.com"], ["student_email@domain.com"],
    "Friday": ["student_email@domain.com"], ["student_email@domain.com"],
    "Saturday": ["student_email@domain.com"], ["student_email@domain.com"], ["student_email@domain.com"],
    "Sunday": ["student_email@domain.com"],
}

# Check if current day in dict
if current_day in email_recipients:
    recipient_emails = email_recipients[current_day]

    # Compose Email with details
    subject = "Link"
    body = """Hello,

Here is your class link.

======================

Tutor_Name is inviting you to a scheduled Zoom meeting.

Join Zoom Meeting:

{Type in your zoom link here}

Meeting ID: Type in your zoom meeting ID here
Passcode: Type in your zoom Passcode here

======================

Best Regards,
Tutor_Name
"""
    body_encoded = urllib.parse.quote(body)
    recipient_emails_encoded = ','.join([urllib.parse.quote(email) for email in recipient_emails])
    compose_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={recipient_emails_encoded}&su={urllib.parse.quote(subject)}&body={body_encoded}"

    # Open time sheet
    time_sheet = "Type in your google sheet time sheet link here"
    webbrowser.open(time_sheet)
    
    # Open the compose URL 
    webbrowser.open(compose_url)

    # Open  Zoom link 
    zoom_link = "Type in your zoom link here"
    webbrowser.open(zoom_link)

    print("Entered emails:", recipient_emails)
else:
    print("No email recipients specified for", current_day)
