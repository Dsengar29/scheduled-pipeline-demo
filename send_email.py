import os
import smtplib
from email.message import EmailMessage

# STATUS environment variable must be SUCCESS or FAILURE
status = os.environ.get("STATUS", "UNKNOWN")

EMAIL_USER = os.environ["EMAIL_USER"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]
EMAIL_TO = os.environ["EMAIL_TO"]

msg = EmailMessage()
msg["From"] = infra.monitoring.ai@gmail.com
msg["To"] = prachi.patil3@wipro.com

if status == "SUCCESS":
    msg["Subject"] = "✅ Google Sheet Refresh SUCCESS"
    msg.set_content(
        "Google Sheet was refreshed successfully at 12:30 PM IST.\n\n"
        "Please check the sheet for updated data."
    )
else:
    msg["Subject"] = "❌ Google Sheet Refresh FAILED"
    msg.set_content(
        "Google Sheet refresh FAILED.\n\n"
        "Please check GitHub Actions logs immediately."
    )

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL_USER, EMAIL_PASSWORD)
    server.send_message(msg)

print("Email notification sent")

