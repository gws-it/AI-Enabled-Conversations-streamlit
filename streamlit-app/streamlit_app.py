from flask import Flask
import streamlit as st
import requests

# Set the URL for the audio server
AUDIO_SERVER_URL = "http://localhost:5000"

st.title("Audio Transcription and Chat Application")

# Upload audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    # Send the audio file to the audio server for transcription
    files = {'audio': uploaded_file}
    response = requests.post(f"{AUDIO_SERVER_URL}/transcribe", files=files)
    
    if response.status_code == 200:
        transcription = response.json().get('transcript', '')
        st.success("Transcription successful!")
        st.write("Transcription:")
        st.write(transcription)
        
        # Chat with AI using the transcription
        messages = [{"role": "user", "content": transcription}]
        chat_response = requests.post(f"{AUDIO_SERVER_URL}/chat", json={"messages": messages})
        
        if chat_response.status_code == 200:
            ai_reply = chat_response.json().get('reply', '')
            st.write("AI Response:")
            st.write(ai_reply)
        else:
            st.error("Error getting AI response.")
    else:
        st.error("Error during transcription.")
else:
    st.info("Please upload an audio file to get started.")