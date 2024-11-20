import smtplib
from tkinter import Tk, Label, Entry, Button, Text, END, messagebox


def send_email():
    try:
        sender_email = sender_email_entry.get()
        password = password_entry.get()
        recipient_email = recipient_email_entry.get()
        subject = subject_entry.get()
        body = message_text.get("1.0", END)

        message = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, message)

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


root = Tk()
root.title("Prem's Email Sender")
root.geometry("500x400")

Label(root, text="Sender Email:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
sender_email_entry = Entry(root, width=40)
sender_email_entry.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
password_entry = Entry(root, width=40, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Recipient Email:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
recipient_email_entry = Entry(root, width=40)
recipient_email_entry.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Subject:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
subject_entry = Entry(root, width=40)
subject_entry.grid(row=3, column=1, padx=10, pady=5)

Label(root, text="Message:").grid(row=4, column=0, padx=10, pady=5, sticky="nw")
message_text = Text(root, width=40, height=10)
message_text.grid(row=4, column=1, padx=10, pady=5)

send_button = Button(root, text="Send Email", command=send_email)
send_button.grid(row=5, column=1, pady=10)

root.mainloop()
