import streamlit as st
import requests
from twilio.rest import Client

API_URL = "https://api-inference.huggingface.co/models/MIT/ast-finetuned-audioset-10-10-0.4593"
headers = {"Authorization": "Bearer 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"}

def query(file_content):
    response = requests.post(API_URL, headers=headers, data=file_content)
    return response.json()

def send_dnd_alert():
    # Twilio API credentials
    account_sid = 'AC423d9b4bac7fbac5ce51c21acd4d17c5'
    auth_token = '[AuthToken]'
    client = Client(account_sid, auth_token)

    # Send DND Alert message
    message = client.messages.create(
        from_='+15304545628',
        body='Screaming detected! Please do not disturb.',
        to='+919059657973'
    )

    # Print the SID of the message
    st.write("DND Alert message sent. SID:", message.sid)

def about_project():
    st.title("About Project")
    st.write(
        """
        ## Voice Testing App

        This is a Streamlit app that allows you to test audio files against a pre-trained model.

        The app provides two main functionalities:

        - **About Project**: Learn more about the project and its objectives.
        - **Voice Testing**: Upload an audio file and test it against the pre-trained model to identify sounds.

        This app uses the Hugging Face API for inference.

        """
    )

def voice_testing():
    st.title("Voice Testing")
    st.write("Upload an audio file (in WAV or MP3 format) and click 'Test' to analyze it.")

    uploaded_file = st.file_uploader("Choose an audio file...", type=["wav", "mp3"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        # Display the preview of the uploaded audio file
        file_type = uploaded_file.type
        st.audio(uploaded_file, format='audio/wav' if 'wav' in file_type else 'audio/mpeg')

        # Perform voice testing
        file_content = uploaded_file.read()
        output = query(file_content)
        labels = [entry['label'] for entry in output]

        st.write("Predicted labels:")
        if "Screaming" in labels:
            st.write("Screaming")
            
            # Send DND Alert using Twilio API
            send_dnd_alert()
            
        else:
            st.write(labels[0])

def main():
    page = st.sidebar.selectbox("Choose a page", ["About Project", "Voice Testing"])

    if page == "About Project":
        about_project()
    elif page == "Voice Testing":
        voice_testing()

if __name__ == "__main__":
    main()
