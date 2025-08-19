📬 ColdReach – Automated Cold Email Sender for Internships

ColdReach is a Streamlit-based tool that simplifies cold emailing for internship applications. It allows you to send personalized, professional emails with resume attachments to multiple companies efficiently, saving time and effort while keeping your outreach polished.

🌟 Features

📝 Customizable Templates – Edit and preview emails using Jinja2 variables
📊 Excel Integration – Upload recipient data for bulk sending
📎 Resume Attachment – Automatically attach your resume (PDF)
🔒 Secure Gmail Login – Uses Gmail App Passwords (2FA required)
📈 Live Progress Tracking – Visual feedback for email status
⚡ Rate Limiting – Restricts to 200 emails/day to avoid spam
🎯 Personalization – Dynamic content for each recipient
📱 Responsive UI – Simple and clean interface built with Streamlit

🚀 Quick Start
Prerequisites

Python 3.7+

Gmail account with 2-Factor Authentication enabled

Gmail App Password (16-character password)

Installation
git clone https://github.com/AbhirupDey/ColdReach.git
cd ColdReach
pip install -r requirements.txt

Run the App
streamlit run main.py


Open in browser: http://localhost:8501

📋 Gmail Setup Guide

To use ColdReach, you must generate a Gmail App Password:

Enable 2-Factor Authentication in your Google account

Go to Google Account → Security → App passwords

Create a new App Password for Mail

Copy the 16-character password (without spaces)

🔗 Direct link: Generate Gmail App Password

⚠️ Use this password in the app, not your regular Gmail password.

📊 Excel File Format

Your Excel sheet (.xlsx) should include these columns:

Column	Required	Description
Name	✅ Yes	Recipient’s full name
Email	✅ Yes	Recipient’s email address
Company	✅ Yes	Company name
Title	❌ No	Job title (defaults to Hiring Manager)

Example File:

Name        | Email                | Company    | Title
John Smith  | john@techcorp.com    | TechCorp   | HR Manager
Jane Doe    | jane@startupxyz.com  | StartupXYZ | CTO

🎯 Template Variables

You can use the following Jinja2 variables in your templates:

Your Info

{{your_name}}, {{university}}, {{phone}}, {{email}}

{{linkedin}}, {{github}}, {{portfolio_link}}

Recipient Info

{{name}}, {{company}}, {{title}}

Example Template

Subject: Internship Application – {{your_name}}

Dear {{title}},

My name is {{your_name}}, a Computer Science student at {{university}}.  
I’m writing to express interest in internship opportunities at {{company}}.  

Best regards,  
{{your_name}}  
{{phone}} | {{email}}

🏗️ Project Structure
ColdReach/
├── main.py                 # Streamlit interface
├── email_sender.py         # Email sending logic
├── requirements.txt        # Dependencies
├── templates/
│   └── email_template.txt  # Default template
├── src/
│   └── app.py              # Optional Tkinter GUI
└── README.md               # Documentation

⚙️ Usage

Fill Personal Info (Sidebar) – Gmail, App Password, personal details, resume

Edit Email Template – Customize using {{variables}}

Upload Excel File – With required recipient columns

Send Emails – Start bulk sending & track progress live

🛡️ Security

Secure Gmail authentication via App Passwords

No password storage (credentials live only per session)

Resume files cleaned up automatically

Daily sending cap (200 emails/day)

Error handling for failed deliveries

🚫 Limitations

Daily limit: 200 emails/day

Resume file size must be < 25 MB

Supports Gmail only

Requires internet connection

🔍 Troubleshooting

Authentication issues? → Enable 2FA + use App Password (not Gmail password)

Excel errors? → Ensure .xlsx format with required columns

Email not sent? → Check internet, recipient email, Gmail limits

🤝 Contributing

Fork the repository

Create a new branch:

git checkout -b feature/my-feature


Commit changes:

git commit -m "Add new feature"


Push and open a Pull Request

📜 License

This project is licensed under the MIT License – see the LICENSE
 file.

🙏 Acknowledgments

Built with Streamlit

Templates powered by Jinja2

Excel support with pandas
 and openpyxl

📞 Support

See Troubleshooting section

Open an Issue on GitHub

Verify dependencies are installed

⭐ If you found ColdReach useful, don’t forget to star the repo!

Made with ❤️ to help students land internships 🚀
