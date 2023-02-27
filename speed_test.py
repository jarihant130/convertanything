import speedtest
import streamlit as st

def test_speed():
    st.title("SpeedTest App")
    st.write("Testing download and upload speed...")
    with st.spinner('Please wait...'):
        st.write("Connecting to nearby server...")
        st_speed = speedtest.Speedtest()
        st_speed.get_best_server()
        
        st.write("Measuring download speed...")
        download_speed = st_speed.download() / 1000000  # Convert to megabits per second
        st.write("Measuring upload speed...")
        col1, col2 = st.columns(2)
        
        
        col1.metric("Download Speed :arrow_down:", f"{download_speed:.2f}", "Mbps", delta_color="inverse")

        upload_speed = st_speed.upload() / 1000000  # Convert to megabits per second
        col2.metric("Upload Speed :arrow_up:", f"{upload_speed:.2f}", "Mbps")
        
        st.success("Speed test complete!")
