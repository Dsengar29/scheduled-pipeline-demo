import os
import smtplib
from email.message import EmailMessage
from datetime import datetime, timezone, timedelta

# Convert current UTC time to IST
now_utc = datetime.now(timezone.utc)
IST = timezone(timedelta(hours=5, minutes=30))
now_ist = now_utc.astimezone(IST)
time_str = now_ist.strftime("%Y-%m-%d %I:%M %p IST")

# STATUS environment variable must be SUCCESS or FAILURE
status = os.environ.get("STATUS", "UNKNOWN")

EMAIL_USER = os.environ["EMAIL_USER"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]
EMAIL_TO = os.environ["EMAIL_TO"]

msg = EmailMessage()
msg["From"] = EMAIL_USER
msg["To"] = EMAIL_TO

if status == "SUCCESS":
    msg["Subject"] = "✅ Google Sheet Refresh SUCCESS"
    msg.set_content(
        f"Google Sheet was refreshed successfully at {time_str}.\n\n"
        "Please check the sheet for updated data."
    )
else:
    msg["Subject"] = "❌ Google Sheet Refresh FAILED"
    msg.set_content(
        f"Google Sheet refresh FAILED at {time_str}.\n\n"
        "Please check GitHub Actions logs immediately."
    )

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL_USER, EMAIL_PASSWORD)
    server.send_message(msg)

print(f"Email notification sent ({status}) at {time_str}")

