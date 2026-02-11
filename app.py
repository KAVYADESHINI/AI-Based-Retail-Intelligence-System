import streamlit as st
from video_processor import process_video
from analytics import calculate_dwell_time
from genai_insights import generate_insights

st.title("AI Retail Intelligence Dashboard")

video = st.file_uploader("Upload Store Video")

if video is not None:
    entry_times = process_video(video)
    dwell_data = calculate_dwell_time(entry_times)

    total_visitors = len(dwell_data)
    avg_dwell = sum(dwell_data.values()) / total_visitors

    st.metric("Total Visitors", total_visitors)
    st.metric("Average Dwell Time", avg_dwell)

    if st.button("Generate AI Insights"):
        insights = generate_insights(total_visitors, avg_dwell)
        st.write(insights)
