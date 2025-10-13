
import streamlit as st
import csv
from pathlib import Path
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials


st.title("Rental Request Form")

# User input fields
name = st.text_input("Your name",key="name_input")
email = st.text_input("Your email",key="email_input")
request = st.text_input("Request about House or Apartment renting:", key="request_input")

# Submit button
if st.button("Submit"):
    if not name or not email or not request:
        st.warning("Please fill in all fields before submitting.")
    else:
        st.success("Request submitted ✅")
        
        print(f"Name: {name}, Email: {email}, Request: {request}")
        # Save to CSV in the background
        file_path = Path("requests.csv")
        file_exists = file_path.is_file()
        with open(file_path, mode='a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["timestamp", "name", "email", "request"])  # header
            writer.writerow([datetime.now().isoformat(), name, email, request])
    
        # Save  to Google Sheets
            
    try:
            # Read credentials from Streamlit Secrets
            google_creds= st.secrets["google"]
            

            # Define the scope
            scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
             

            # create a Credentials object from the dictionary
            creds= Credentials.from_service_account_info(google_creds, scopes=scope)

            # Authorize the client
            client = gspread.authorize(creds)

            # Open the target sheet
            sheet = client.open("House Requests").sheet1
            sheet.append_row([datetime.now().isoformat(), name, email, request])

            st.success("📊 Data also saved to Google Sheets.")
    except Exception as e:
            st.error(f"❌ Failed to save to Google Sheets: {e}")
    
    
        



        
       
    
        


