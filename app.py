

import streamlit as st
import csv
from pathlib import Path
from datetime import datetime
import streamlit as st
import csv
from pathlib import Path
from datetime import datetime

st.title("Rental Request Form")

# User input fields
name = st.text_input("Your name")
email = st.text_input("Your email")
request = st.text_input("Request about House or Apartment renting:")

# Submit button
if st.button("Submit"):
    if not name or not email or not request:
        st.warning("Please fill in all fields before submitting.")
    else:
        st.success("Request submitted ✅")
        
        # Save to CSV in the background
        file_path = Path("requests.csv")
        file_exists = file_path.is_file()
        with open(file_path, mode='a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["timestamp", "name", "email", "request"])  # header
            writer.writerow([datetime.now().isoformat(), name, email, request])
