import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/MIT/ast-finetuned-audioset-10-10-0.4593"
headers = {"Authorization": "Bearer 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"}

def query(file_content):
    response = requests.post(API_URL, headers=headers, data=file_content)
    return response.json()

def about_project():
    st.title("About Project")
    st.write(
        """
        ## Audio Classification App

        This is a Streamlit app that allows you to test audio files against a pre-trained model.

        The app provides two main functionalities:

        - **About Project**: Learn more about the project and its objectives.
        - **Audio Testing**: Upload an audio file and test it against the pre-trained model to identify sounds.

        This app uses the Hugging Face API for inference.

        """
    )

def voice_testing():
    st.title("Audio Testing")
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
