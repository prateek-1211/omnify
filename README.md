Booking Analysis Dashboard

📌 Project Overview

This project involves cleaning, analyzing, and visualizing booking data to provide insights into booking trends, facility usage, and revenue generation. The dataset was processed using Python, Pandas, and Streamlit, ensuring high-quality visual representation of key performance indicators (KPIs) and trends.

🚀 Features

Data Cleaning: Handling missing values, converting date formats, and filtering incorrect entries.

Data Transformation: Extracting key time components and aggregating data for analysis.

Key Performance Indicators (KPIs):

Total Bookings

Total Revenue

Average Booking Price

Visualizations:

Booking Type Distribution (Pie Chart)

Facility Usage Analysis (Bar Chart)

Time Slot Popularity (Bar Chart)

Monthly Booking Trends (Line Chart)

🛠 Technologies Used

Python (Pandas, NumPy, Plotly, Streamlit)

Data Handling: Pandas for data manipulation

Visualization: Plotly for interactive charts

Deployment: Streamlit for dashboard visualization

⚡ Installation & Usage

Clone the repository:

git clone https://github.com/your-username/booking-analysis-dashboard.git
cd booking-analysis-dashboard

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

🐞 Issues & Fixes

JSON Serialization Issue: Resolved by converting Pandas Period objects to strings before visualization.

Incorrect Time Slot Formatting: Handled using errors='coerce' to prevent script failures.
