import os
import json
import sys
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import pytz

try:
    # Load credentials from GitHub Secrets
    creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = Credentials.from_service_account_info(
        creds_dict, scopes=scopes
    )

    client = gspread.authorize(credentials)

    # ✅ REPLACE WITH YOUR SHEET ID
    SPREADSHEET_ID = "1Y9BfnGx832lwlLWNqVHnYzShj0N4hecvRZMbwdrHttk"

    sheet = client.open_by_key(SPREADSHEET_ID).sheet1

    # IST time (easy to verify cron)
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S IST")

    data = [
        ["Last Refresh Time", now],
        ["Metric A", 123],
        ["Metric B", 456],
        ["Metric C", 789],
    ]

    sheet.clear()
    sheet.update("A1", data)

    print(f"✅ Google Sheet refreshed successfully at {now}")

except Exception as e:
    print("❌ Failed to refresh Google Sheet")
    print(str(e))
    sys.exit(1)   # VERY IMPORTANT
