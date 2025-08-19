# 📬 ColdReach - Cold Email Sender for Internships

A streamlined Streamlit application that automates personalized cold email sending for internship applications. Send professional, customized emails with resume attachments to multiple companies efficiently.

## 🌟 Features

- **📝 Customizable Email Templates**: Edit and preview email templates with Jinja2 variables
- **📊 Excel Integration**: Upload Excel files with recipient data for bulk email sending
- **📎 Resume Attachment**: Automatically attach your PDF resume to all emails
- **🔒 Secure Gmail Integration**: Uses Gmail App Passwords for secure authentication
- **📈 Real-time Progress Tracking**: Monitor email sending progress with visual feedback
- **⚡ Rate Limiting**: Built-in daily email limit (200 emails) to prevent spam
- **🎯 Personalization**: Dynamic content replacement for each recipient
- **📱 Responsive UI**: Clean, intuitive interface built with Streamlit

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Gmail account with 2-Factor Authentication enabled
- Gmail App Password (16-character password)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AbhirupDey/ColdReach.git
   cd ColdReach
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run main.py
   ```

4. **Access the app**: Open your browser to `http://localhost:8501`

## 📋 Gmail Setup Guide

### Enable App Passwords (Required)

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate App Password**:
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Navigate to **2-Step Verification**
   - Scroll down to **App passwords**
   - Generate a new password for "Mail"
   - Copy the **16-character password** (no spaces)

3. **Alternative direct link**: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

⚠️ **Important**: Use the App Password in the application, NOT your regular Gmail password.

## 📊 Excel File Format

Create an Excel file (`.xlsx`) with the following columns:

| Column Name | Required | Description |
|-------------|----------|-------------|
| `Name` | ✅ Yes | Recipient's full name |
| `Email` | ✅ Yes | Recipient's email address |
| `Company` | ✅ Yes | Company name |
| `Title` | ❌ No | Job title (defaults to "Hiring Manager") |

### Example Excel Structure:
```
Name          | Email                    | Company    | Title
John Smith    | john@techcorp.com       | TechCorp   | HR Manager
Jane Doe      | jane@startupxyz.com     | StartupXYZ | CTO
```

## 🎯 Template Variables

The email template supports the following Jinja2 variables:

### Your Information:
- `{{your_name}}` - Your full name
- `{{university}}` - Your university name
- `{{phone}}` - Your phone number
- `{{email}}` - Your email address
- `{{linkedin}}` - Your LinkedIn profile URL
- `{{github}}` - Your GitHub profile URL
- `{{portfolio_link}}` - Your portfolio website URL

### Recipient Information:
- `{{name}}` - Recipient's name (from Excel)
- `{{company}}` - Company name (from Excel)
- `{{title}}` - Job title (from Excel, defaults to "Hiring Manager")

### Example Template Usage:
```
Subject: Application for Full Stack Developer Internship - {{your_name}}

Dear {{title}},

My name is {{your_name}}, a Computer Science student at {{university}}. 
I'm interested in internship opportunities at {{company}}.

Best regards,
{{your_name}}
{{phone}} | {{email}}
```

## 🏗️ Project Structure

```
ColdReach/
├── main.py                 # Main Streamlit application
├── email_sender.py         # Email sending functionality
├── requirements.txt        # Python dependencies
├── templates/
│   └── email_template.txt  # Default email template
├── src/
│   └── app.py             # Alternative Tkinter GUI (optional)
└── README.md              # Project documentation
```

## 🔧 Core Components

### [`main.py`](main.py)
- Streamlit web interface
- Template editor and preview
- File upload handling
- Progress tracking and error handling

### [`email_sender.py`](email_sender.py)
- Gmail SMTP integration
- Email composition with attachments
- Authentication and error handling
- Template rendering with Jinja2

### [`templates/email_template.txt`](templates/email_template.txt)
- Default email template
- Customizable through the web interface
- Supports Jinja2 variable substitution

## ⚙️ Usage Instructions

1. **Fill Personal Information** (Sidebar):
   - Gmail address and App Password
   - Personal details (name, university, contact info)
   - Upload your resume (PDF format)

2. **Customize Email Template**:
   - Edit the template in the main interface
   - Use `{{variable}}` format for dynamic content
   - Save changes to persist modifications

3. **Upload Recipient Data**:
   - Prepare Excel file with required columns
   - Upload through the file uploader
   - Review recipient list with pagination

4. **Send Emails**:
   - Click "Send Emails" button
   - Monitor real-time progress
   - Review success/failure reports

## 🛡️ Security Features

- **App Password Authentication**: Secure Gmail integration
- **No Password Storage**: Credentials entered per session
- **Rate Limiting**: Maximum 200 emails per day
- **Temporary File Cleanup**: Resume files automatically deleted
- **Error Handling**: Detailed error messages for troubleshooting

## 🚫 Limitations

- **Daily Email Limit**: 200 emails maximum (configurable in `MAX_EMAILS_PER_DAY`)
- **File Size**: Resume attachments should be under 25MB
- **Gmail Only**: Currently supports Gmail SMTP only
- **Internet Required**: Needs active internet connection for email sending

## 🔍 Troubleshooting

### Common Issues:

**Authentication Error**:
- Ensure 2-Factor Authentication is enabled
- Use App Password, not regular Gmail password
- Generate a new App Password if needed

**File Upload Issues**:
- Check Excel file format (.xlsx only)
- Verify required columns exist
- Ensure file size is reasonable

**Email Sending Failures**:
- Check internet connection
- Verify recipient email addresses
- Review Gmail sending limits

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Email templating powered by [Jinja2](https://jinja.palletsprojects.com/)
- Excel processing with [pandas](https://pandas.pydata.org/) and [openpyxl](https://openpyxl.readthedocs.io/)

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review Gmail App Password setup
3. Create an issue on GitHub
4. Ensure all dependencies are properly installed

---

⭐ **Star this repository if you find it helpful!**

*Made with ❤️ for students seeking internships*
