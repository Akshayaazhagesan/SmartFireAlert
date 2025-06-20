import smtplib
from email.mime.text import MIMEText

def send_email_alert():
    sender = "akshayaazhagesan143@gmail.com"
    password = "jxkm ybwi wogy ryii"  # Your app password
    receiver = "akshayaak9159@gmail.com"

    msg = MIMEText("🔥 Fire detected! Check immediately!")
    msg['Subject'] = "FIRE ALERT!"
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        print("✅ Email sent!")
    except Exception as e:
        print("❌ Error:", e)
# Call the function
send_email_alert()
