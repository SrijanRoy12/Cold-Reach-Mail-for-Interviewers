import streamlit as st
import pandas as pd
from email_sender import load_template, send_email
from jinja2 import Template
import time
import io  # <-- Add this import

# Add a constant for the maximum daily email limit
MAX_EMAILS_PER_DAY = 200

st.title("📬 Cold Email Sender for Internships")

# Add template editor section
st.header("📝 Email Template")
with open("templates/email_template.txt", "r") as f:
    default_template = f.read()

email_template = st.text_area(
    "Edit Email Template",
    value=default_template,
    height=400,
    help="Use {{variable}} format for placeholders. Available variables: your_name, university, phone, email, linkedin, github, portfolio_link, name, company, title"
)

# Save template changes if needed
if st.button("Save Template"):
    with open("templates/email_template.txt", "w") as f:
        f.write(email_template)
    st.success("✅ Template saved successfully!")

st.divider()

# Use the current template content instead of loading from file
template = Template(email_template)

# Add Gmail setup instructions
st.info("""
📧 **Gmail Setup Required:**
1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password: Google Account → Security → 2-Step Verification → App passwords
3. Try direct link: https://myaccount.google.com/apppasswords
4. Use the 16-character App Password (not your regular password)
""")

st.sidebar.header("Sender Info")
gmail_user = st.sidebar.text_input("Your Gmail Address", value="roysrijan53@gmail.com")
gmail_pass = st.sidebar.text_input("Your App Password (16 characters)", type="password", value="Enter your App Password")
your_name = st.sidebar.text_input("Your Full Name", value="Srijan Roy")
university = st.sidebar.text_input("University", value="Institute of Engineering and Management, Kolkata")
phone = st.sidebar.text_input("Phone Number", value="6290875585")
linkedin = st.sidebar.text_input("LinkedIn URL", value="https://www.linkedin.com/in/srijan-roy-iemians/")
github = st.sidebar.text_input("GitHub URL", value="https://github.com/SrijanRoy12")
portfolio_link = st.sidebar.text_input("Portfolio URL", value="https://srijanroy12.github.io/Srijan_portfolio/")
resume_file = st.sidebar.file_uploader("Upload Resume (PDF)", type=["pdf"])
email = gmail_user  # For simplicity

uploaded_file = st.file_uploader("Upload Excel with Name, Email, Company columns", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    if len(df) > MAX_EMAILS_PER_DAY:
        st.error(f"⚠️ Your Excel file contains {len(df)} emails. Please keep it under {MAX_EMAILS_PER_DAY} emails per day.")
    else:
        # Add pagination
        st.info(f"Total emails to be sent: {len(df)}")
        items_per_page = 10
        total_pages = (len(df) + items_per_page - 1) // items_per_page
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            current_page = st.selectbox("Page", options=range(1, total_pages + 1), format_func=lambda x: f"Page {x} of {total_pages}")
        
        start_idx = (current_page - 1) * items_per_page
        end_idx = min(start_idx + items_per_page, len(df))
        
        st.write("📊 Preview of Email Recipients")
        st.dataframe(df.iloc[start_idx:end_idx], use_container_width=True)

        # Show page info
        st.caption(f"Showing emails {start_idx + 1} to {end_idx} of {len(df)}")

        # Validate required fields
        required_fields = {
            "Gmail Address": gmail_user,
            "App Password": gmail_pass,
            "Full Name": your_name,
            "University": university
        }
        missing_fields = [name for name, value in required_fields.items() if not str(value).strip()]
        resume_uploaded = (
            resume_file is not None
            and hasattr(resume_file, "name")
            and resume_file.name.lower().endswith(".pdf")
            and resume_file.size > 0
        )
        if missing_fields or not resume_uploaded:
            if missing_fields:
                st.warning(f"⚠️ Please fill in all required fields: {', '.join(missing_fields)}.")
            if not resume_uploaded:
                st.warning("⚠️ Please upload your resume in PDF format in the sidebar before sending emails.")
        else:
            # Read resume file into memory as bytes before the loop
            resume_bytes = resume_file.getvalue()
            resume_filename = getattr(resume_file, "name", "resume.pdf")
            if st.button("Send Emails"):
                sent_count = 0
                failed_emails = []
                progress_bar = st.progress(0)
                status_text = st.empty()
                try:
                    for index, row in df.iterrows():
                        status_text.text(f"Sending email to {row['Email']}")
                        # Prepare personalized email
                        context = {
                            'your_name': your_name,
                            'university': university,
                            'phone': phone,
                            'email': email,
                            'linkedin': linkedin,
                            'github': github,
                            'portfolio_link': portfolio_link,
                            'name': row['Name'],
                            'company': row['Company'],
                            'title': row.get('Title', 'Hiring Manager'),
                        }
                        rendered = template.render(**context)
                        subject, body = rendered.split('\n', 1)
                        # Use a new in-memory file object for each send
                        resume_file_obj = io.BytesIO(resume_bytes)
                        resume_file_obj.name = resume_filename
                        try:
                            success, error_msg = send_email(
                                gmail_user, 
                                gmail_pass, 
                                row['Email'], 
                                subject.replace("Subject: ", ""), 
                                body,
                                attachment_file=resume_file_obj
                            )
                        except Exception as e:
                            success = False
                            error_msg = f"Unexpected error: {str(e)}"
                        if success:
                            sent_count += 1
                        else:
                            failed_emails.append((row['Email'], error_msg))
                            # If a critical SMTP error occurs, break the loop to avoid infinite hang
                            if error_msg and (
                                "Connection unexpectedly closed" in error_msg or
                                "Server not connected" in error_msg or
                                "timed out" in error_msg or
                                "Too many" in error_msg or
                                "rate limit" in error_msg
                            ):
                                st.error(f"Critical error encountered: {error_msg}. Stopping further sends.")
                                break
                        progress_bar.progress((index + 1) / len(df))
                        time.sleep(1)  # Add delay to avoid Gmail throttling
                except Exception as loop_exception:
                    st.error(f"❌ Unexpected error during sending: {loop_exception}")
                status_text.text("Completed!")
                if sent_count > 0:
                    st.success(f"✅ Sent {sent_count} emails successfully.")
                if failed_emails:
                    st.error(f"❌ Failed to send {len(failed_emails)} emails:")
                    for email, error in failed_emails:
                        st.write(f"• {email}: {error}")
                    if "Username and Password not accepted" in str(failed_emails[0][1]):
                        st.error("""
                        🔒 **Authentication Error:** 
                        - Make sure you're using an App Password, not your regular Gmail password
                        - Verify 2-Factor Authentication is enabled on your Gmail account
                        - Generate a new App Password if needed
                        """)

