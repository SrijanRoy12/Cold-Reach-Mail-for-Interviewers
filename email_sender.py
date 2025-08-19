import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from jinja2 import Template
import os

def load_template(path_or_content):
    """
    Load template from file path or direct content string
    """
    if isinstance(path_or_content, str):
        if os.path.exists(path_or_content):
            with open(path_or_content, 'r') as file:
                content = file.read()
        else:
            content = path_or_content
    return Template(content)

def send_email(gmail_user, gmail_pass, to_email, subject, body, attachment_path=None, attachment_file=None):
    """
    Send email using Gmail SMTP.
    You can provide either attachment_path (file path) or attachment_file (in-memory file-like object, e.g. from Streamlit).
    
    IMPORTANT: For gmail_pass, you MUST use a 16-character App Password, not your regular Gmail password.
    
    To set up App Password:
    1. Enable 2-Factor Authentication on your Google Account (MUST be fully enabled, not just turned on)
    2. Wait 10-15 minutes after enabling 2FA for App passwords option to appear
    3. Go to Google Account → Security → 2-Step Verification
    4. Scroll down to find "App passwords" section (it appears AFTER 2FA is fully active)
    5. If you don't see "App passwords":
       - Make sure 2FA is completely set up (verify with phone/authenticator)
       - Try logging out and back into your Google account
       - Use this direct link: https://myaccount.google.com/apppasswords
    6. Generate a new App Password for "Mail" or "Other (Custom name)"
    7. Use the 16-character password (no spaces) as gmail_pass
    
    Alternative: If App passwords still don't appear, you may need to use OAuth2 instead of SMTP login.
    
    Args:
        gmail_user (str): Your Gmail address
        gmail_pass (str): 16-character App Password (NOT your regular password)
        to_email (str): Recipient email address
        subject (str): Email subject
        body (str): Email body content
        attachment_path (str): Path to the file to be attached (optional)
        attachment_file (file-like object): In-memory file object to be attached (optional)
    """
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Attach file if provided (in-memory file or file path)
    if attachment_file is not None:
        # Streamlit's file_uploader returns a file-like object with .name and .getvalue()
        attachment_file.seek(0)  # Reset pointer to start for each email
        filename = getattr(attachment_file, "name", "resume.pdf")
        file_bytes = attachment_file.getvalue()
        file_attachment = MIMEApplication(file_bytes)
        file_attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(file_attachment)
    elif attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            file_attachment = MIMEApplication(f.read())
            file_attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
            msg.attach(file_attachment)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_pass)
        server.send_message(msg)
        server.quit()
        return True, None
    except smtplib.SMTPAuthenticationError as e:
        error_msg = ("Authentication failed. Please ensure you're using a 16-character App Password, "
                    "not your regular Gmail password. Enable 2FA and generate App Password at: "
                    "Google Account → Security → 2-Step Verification → App passwords")
        print(f"Auth error sending to {to_email}: {e}")
        return False, error_msg
    except smtplib.SMTPRecipientsRefused as e:
        error_msg = "Recipient email address rejected."
        print(f"Recipient error sending to {to_email}: {e}")
        return False, error_msg
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(f"Error sending to {to_email}: {e}")
        return False, error_msg
