# 📬 ColdReach – Internship Cold Email Automation

ColdReach is a lightweight, Streamlit-powered application that helps students and professionals send personalized cold emails for internship opportunities. With built-in Gmail integration, resume attachments, and Excel-based bulk sending, it streamlines outreach so you can focus on landing interviews instead of managing emails.

🌟 Key Features

📝 Customizable Templates – Write once, personalize for everyone using Jinja2 variables
📊 Excel Upload – Import recipient data for bulk emailing
📎 Resume Auto-Attach – Attach your PDF resume to all outgoing emails
🔒 Secure Gmail Login – Uses App Passwords with 2FA (never stores credentials)
📈 Progress Dashboard – Track emails sent in real-time with visual feedback
⚡ Rate Limiting – Enforces Gmail’s 200 emails/day cap to avoid spam flags
🎯 Dynamic Personalization – Each recipient gets a uniquely tailored message
📱 Responsive UI – Clean, intuitive design built with Streamlit

🚀 Quick Start
Prerequisites

Python 3.7+

Gmail account with 2FA enabled

Gmail App Password (16 characters, generated once)

Installation
git clone https://github.com/AbhirupDey/ColdReach.git
cd ColdReach
pip install -r requirements.txt

Run the App
streamlit run main.py


Access at 👉 http://localhost:8501

📋 Gmail Setup (Required)

Enable 2-Step Verification on your Google account.

Navigate to Google Account → Security → App passwords

Generate a new App Password for "Mail".

Use this 16-character password in ColdReach instead of your Gmail password.

🔗 Direct link: Generate Gmail App Password

📊 Excel File Format

Your Excel sheet (.xlsx) should include:

Column	Required	Description
Name	✅ Yes	Recipient’s full name
Email	✅ Yes	Recipient’s email address
Company	✅ Yes	Target company name
Title	❌ No	Job title (defaults to Hiring Manager)

Example:

Name        | Email                | Company    | Title
John Smith  | john@techcorp.com    | TechCorp   | HR Manager
Jane Doe    | jane@startupxyz.com  | StartupXYZ | CTO

🎯 Template Variables

Available variables for your email:

Your Info

{{your_name}}, {{university}}, {{phone}}, {{email}},

{{linkedin}}, {{github}}, {{portfolio_link}}

Recipient Info

{{name}}, {{company}}, {{title}}

Sample Email Template:

Subject: Internship Application – {{your_name}}

Dear {{title}},

My name is {{your_name}}, a Computer Science student at {{university}}.  
I’m reaching out to explore internship opportunities at {{company}}.  

Best regards,  
{{your_name}}  
{{phone}} | {{email}}

🏗️ Project Structure
ColdReach/
├── main.py                 # Streamlit application
├── email_sender.py         # Email sending logic
├── requirements.txt        # Dependencies
├── templates/
│   └── email_template.txt  # Default template
├── src/
│   └── app.py              # Optional Tkinter GUI
└── README.md               # Documentation

⚙️ How It Works

Fill Sidebar Details – Gmail, App Password, personal info, resume (PDF)

Customize Template – Edit and preview emails in the app

Upload Excel File – Recipient list with required columns

Send Emails – Start bulk sending and monitor progress

🛡️ Security

App Password login (never saves your real Gmail password)

Session-only credentials (not stored anywhere)

Auto cleanup of uploaded files

Daily rate limit (200 emails/day)

Detailed error handling for failed sends

🚫 Limitations

Daily cap: 200 emails/day (can be adjusted)

Resume file < 25 MB

Currently supports Gmail only

Requires internet connection

🔍 Troubleshooting

Auth errors? Use App Password (not Gmail password), check 2FA

File upload errors? Ensure .xlsx format with required columns

Sending failures? Check internet connection + Gmail limits

🤝 Contributing

Fork the repo

Create a branch (git checkout -b feature/my-feature)

Commit changes (git commit -m "Add feature")

Push (git push origin feature/my-feature)

Open a Pull Request

📜 License

MIT License – see LICENSE
 for details.

🙏 Acknowledgments

Streamlit
 for the UI

Jinja2
 for templating

pandas
 & openpyxl
 for Excel handling

📞 Support

Check Troubleshooting above

File an issue in GitHub Issues

Reinstall dependencies if errors persist

⭐ If you find this project helpful, don’t forget to star the repo!
