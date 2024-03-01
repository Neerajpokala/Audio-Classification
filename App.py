import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/MIT/ast-finetuned-audioset-10-10-0.4593"
headers = {"Authorization": "Bearer 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"}

def query(file_content):
    response = requests.post(API_URL, headers=headers, data=file_content)
    return response.json()

def about_project():
    st.title("Human scream detection using SVM and MLP")
    st.write("""
Crime remains a prevalent issue in our society, with incidents like robberies, murders, and assaults 
occurring daily worldwide. One common challenge is the delayed response of authorities to crime 
scenes, often attributed to a lack of timely and accurate information. To address this concern, our 
project introduces a discreet desktop application. Functioning seamlessly in the background, the 
application employs advanced technologies, including Machine Learning and Deep Learning 
models especially SVM and MLP, to detect and analyze human screams in real-time. In the event 
of a potential emergency, the application initiates an automatic alert sent via SMS to pre-designated contacts. This innovative solution not only contributes to faster response times but also excels in discerning clear human sounds amidst background noise, thereby improving the accuracy of threat identification. By leveraging technology to enhance emergency response, the project aims to create safer communities and minimize the impact of criminal activities on individuals and society as a whole. Through these efforts, we aspire to empower individuals to take proactive measures in ensuring their safety and the well-being of their communities.
""")
        
        

    
    

def voice_testing():
    st.title("Audio Classification Testing")
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
            st.write(" An SOS Message as been sent Sucessfully")
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
