import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/MIT/ast-finetuned-audioset-10-10-0.4593"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

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
    st.write("Upload an audio file and click 'Test' to analyze it.")

    uploaded_file = st.file_uploader("Choose an audio file...", type=["wav"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        # Perform voice testing
        output = query(uploaded_file)
        labels = [entry['label'] for entry in output]

        st.write("Predicted labels:")
        for label in labels:
            st.write(label)

def main():
    page = st.sidebar.selectbox("Choose a page", ["About Project", "Voice Testing"])

    if page == "About Project":
        about_project()
    elif page == "Voice Testing":
        voice_testing()

if __name__ == "__main__":
    main()
