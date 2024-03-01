import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/MIT/ast-finetuned-audioset-10-10-0.4593"
headers = {"Authorization": "Bearer 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"}

def query(file_content):
    response = requests.post(API_URL, headers=headers, data=file_content)
    return response.json()

def about_project():
    st.title("Human scream detection using SVM and MLP")
    st.write(content)
    content = """
# Abstract
Crime remains a prevalent issue in our society, with incidents like robberies, murders, and assaults 
occurring daily worldwide. One common challenge is the delayed response of authorities to crime 
scenes, often attributed to a lack of timely and accurate information. To address this concern, our 
project introduces a discreet desktop application. Functioning seamlessly in the background, the 
application employs advanced technologies, including Machine Learning and Deep Learning 
models especially SVM and MLP, to detect and analyze human screams in real-time. In the event 
of a potential emergency, the application initiates an automatic alert sent via SMS to pre-designated contacts. This innovative solution not only contributes to faster response times but also excels in discerning clear human sounds amidst background noise, thereby improving the accuracy of threat identification. By leveraging technology to enhance emergency response, the project aims to create safer communities and minimize the impact of criminal activities on individuals and society as a whole. Through these efforts, we aspire to empower individuals to take proactive measures in ensuring their safety and the well-being of their communities.

---

# Proposed System
This study proposes an innovative solution for crime prevention through the application of advanced 
Machine Learning and Deep Learning algorithms, specifically employing Support Vector Machine 
(SVM) and Multilayer Perceptron Neural Network (MPN). The primary objective is to develop a 
robust system for the real-time detection and analysis of human screams, contributing to enhanced 
public safety and crime rate control.  
The first algorithm utilized in our solution is the Support Vector Machine (SVM). SVM is employed 
for the initial detection of human screams in the audio data. Trained on a carefully curated dataset, 
SVM excels in classifying and distinguishing between positive and negative class instances. The 
positive class comprises approximately 2000 instances of human screams, while the negative class 
encompasses around 3000 non-scream sounds. This dual-class dataset ensures a comprehensive 
learning process, enhancing the SVM model's ability to identify genuine threats.

---

# Process of the Project
**Input: Testing Voice**  
Audio input is captured for testing, representing the real-time sound environment.

**Phase 1: Environmental Noise Filtering (Tag1: Noisy Environment)**  
If the initial analysis determines that the environment is noisy, further processing is required.  
Decision (Tag1): If "Noisy Environment" is tagged, proceed to the next stage. Otherwise, terminate.

**Phase 2: Sound Classification (Tag1: Speech, Tag2: Scream, Shout)**  
In this phase, the system classifies the sound into different categories, including speech, scream, and 
shout.  
Decision (Tag1): If "Speech" is tagged, the system may continue processing or take specific actions 
based on project requirements.  
Decision (Tag2): If "Scream" or "Shout" is tagged, proceed to the next stage. Otherwise, terminate.

**Phase 3: Scream and Shout Classification (Tag1: Shout, Tag2: Scream)**  
Further refinement of sound classification focuses on differentiating between screams and shouts.  
Decision (Tag1): If "Shout" is tagged, the system may continue processing or take specific actions 
based on project requirements.  
Decision (Tag2): If "Scream" is tagged, proceed to the next stage. Otherwise, terminate.

**Multilayer Perceptron (MLP) Model (Scream Classification)**  
The input, identified as a potential scream, is sent to the Multilayer Perceptron (MLP) model for a 
more detailed classification.  
Decision: If the MLP model confirms the presence of a scream, the system proceeds to generate an 
alert SMS. Otherwise, the process terminates.

**Alert SMS Generation**  
Upon confirmation of a scream by the MLP model, the system generates an alert SMS.
"""
        
        

    
    

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
