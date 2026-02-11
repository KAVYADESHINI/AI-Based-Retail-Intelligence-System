🛍️ AI-Based Real-Time Retail Intelligence & Automated Business Insight System
📌 Overview

This project is an AI-powered retail analytics system that uses Computer Vision and Generative AI to analyze customer behavior inside a retail store.

The system detects and tracks customers in real time, calculates dwell time, and generates automated business insights to help improve sales and product placement strategies.

🚀 Key Features

Real-time customer detection using YOLOv8

Multi-object tracking using ByteTrack

Unique ID assignment for each customer

Dwell time calculation (store-level & zone-level)

SQLite-based analytics storage

AI-generated business insights using LLM

Interactive dashboard built with Streamlit

🧠 System Architecture

Video Input
→ YOLOv8 (Person Detection)
→ ByteTrack (Multi-Object Tracking)
→ Dwell Time Analytics
→ Database Storage
→ GenAI Report Generation
→ Streamlit Dashboard

🛠️ Tech Stack

Python

OpenCV

YOLOv8 (Ultralytics)

ByteTrack

Streamlit

SQLite

OpenAI API (for insight generation)

📊 Business Insights Generated

The system automatically generates:

Total visitor count

Average dwell time

High engagement product zones

Peak traffic hours

Low-conversion product alerts

AI-based recommendations for product placement and pricing

⚙️ Installation
pip install -r requirements.txt


Run the application:

streamlit run app.py

🎯 Future Enhancements

Age & gender detection

Emotion analysis

Heatmap visualization

Real-time cloud deployment (AWS/GCP)

Integration with billing data for conversion rate analysis

📌 Impact

This system enables data-driven retail decision-making by converting raw video data into actionable business intelligence.
