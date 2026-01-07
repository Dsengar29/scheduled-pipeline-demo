import os
import json
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Load credentials from GitHub Secrets
creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = Credentials.from_service_account_info(creds_dict, scopes=scopes)

client = gspread.authorize(credentials)

# Name of your Google Sheet (must match exactly)
SHEET_NAME = "TEST_PERFORMANCE_P1"
sheet = client.open(SHEET_NAME).sheet1

# Example refreshed data
now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
data = [
    ["Last Refresh Time (UTC)", now],
    ["Metric A", 123],
    ["Metric B", 456],
    ["Metric C", 789],
]

# Clear old data and update
sheet.clear()
sheet.update("A1", data)

print("Google Sheet refreshed successfully")

