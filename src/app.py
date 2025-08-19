import tkinter as tk
from tkinter import ttk, scrolledtext
import pandas as pd

DEFAULT_TEMPLATE = """Subject: Application for Full Stack Web Developer Internship: {{your_name}}

Dear {{title}},

I am {{your_name}}, a final-year Computer Science student at {{university}}. I'm reaching out to express my interest in a Full Stack Web Developer internship at {{company}}.

I have built several full-stack projects using technologies like React.js, Node.js, Express, and MongoDB. My work reflects a strong understanding of both frontend and backend development, and I enjoy crafting clean, user-focused web experiences.

I have attached my resume to this email, and you can also view my portfolio ({{portfolio_link}}) to see my project work in detail. I would appreciate the chance to discuss how I can contribute to your team.

Thank you for your time.

Sincerely,  
{{your_name}}  
{{phone}}  
{{email}}  
{{linkedin}} 
{{github}}
{{portfolio_link}}"""

class EmailSenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cold Email Sender")
        self.email_template = DEFAULT_TEMPLATE
        self.excel_data = None
        
        self.setup_ui()

    def setup_ui(self):
        # Template Input Section
        template_frame = ttk.LabelFrame(self.root, text="Email Template")
        template_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.template_text = scrolledtext.ScrolledText(template_frame, width=60, height=15)
        self.template_text.insert(tk.END, self.email_template)
        self.template_text.pack(pady=5, padx=5, fill="both", expand=True)
        
        # Excel Review Section
        excel_frame = ttk.LabelFrame(self.root, text="Excel Data Review")
        excel_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.tree = ttk.Treeview(excel_frame)
        self.tree.pack(pady=5, padx=5, fill="both", expand=True)

    def update_template(self, event=None):
        self.email_template = self.template_text.get("1.0", tk.END).strip()

    def load_excel_data(self, file_path):
        self.excel_data = pd.read_excel(file_path, engine="openpyxl")
        self.update_excel_view()

    def update_excel_view(self):
        if self.excel_data is not None:
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Set up columns
            self.tree["columns"] = list(self.excel_data.columns)
            for col in self.excel_data.columns:
                self.tree.heading(col, text=col)
            
            # Add data
            for idx, row in self.excel_data.iterrows():
                self.tree.insert("", "end", values=list(row))

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailSenderApp(root)
    root.mainloop()
