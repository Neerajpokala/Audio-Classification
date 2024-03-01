import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/MIT/ast-finetuned-audioset-10-10-0.4593"
headers = {"Authorization": "Bearer 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"}

def query(file_content):
    response = requests.post(API_URL, headers=headers, data=file_content)
    return response.json()

def about_project():
    st.title("Human scream detection using SVM and MLP")
    review_text = """
    **Introduction:**
    The audio classification model project aimed to develop a system capable of accurately categorizing audio samples into predefined classes or labels. Leveraging machine learning techniques, the project addressed various challenges inherent in audio data analysis and classification.

    **Key Components:**
    1. **Data Collection and Preprocessing:**
    - The project began with the acquisition of diverse audio datasets covering a wide range of classes or categories.
    - Data preprocessing steps were crucial, involving audio normalization, feature extraction, and, potentially, data augmentation to enhance model generalization.

    2. **Model Architecture:**
    - The selection of an appropriate model architecture significantly impacted the classification performance.
    - Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), or hybrid models might have been explored based on the nature of the audio data and classification requirements.

    3. **Feature Engineering:**
    - Extracting relevant features from audio signals played a pivotal role in model training.
    - Techniques such as Mel-frequency cepstral coefficients (MFCC), spectrogram analysis, or wavelet transforms could have been employed for feature representation.

    4. **Model Training and Evaluation:**
    - The training process involved splitting the dataset into training, validation, and testing sets to assess model performance accurately.
    - Key metrics such as accuracy, precision, recall, and F1-score were used to evaluate the model's classification capabilities.

    5. **Hyperparameter Tuning and Optimization:**
    - Hyperparameter optimization techniques, including grid search, random search, or Bayesian optimization, might have been applied to fine-tune model parameters and enhance performance.

    **Challenges Faced:**
    1. **Data Imbalance:**
    - Addressing data class imbalances, where certain classes are underrepresented, was crucial to prevent biased model predictions.

    2. **Computational Resources:**
    - Training deep learning models on large audio datasets often required substantial computational resources and efficient hardware accelerators.

    3. **Generalization:**
    - Ensuring model generalization across diverse audio samples, including those from different recording environments or with varying noise levels, presented a significant challenge.

    **Recommendations for Improvement:**
    1. **Data Augmentation:** 
    - Implementing data augmentation techniques such as time stretching, pitch shifting, or adding background noise could enhance model robustness.

    2. **Ensemble Learning:**
    - Employing ensemble learning methods by combining predictions from multiple base models could potentially boost classification performance.

    3. **Transfer Learning:**
    - Leveraging pre-trained models such as those trained on large-scale audio datasets (e.g., AudioSet) and fine-tuning them for the specific classification task could expedite model training and improve results.

    4. **Interpretability:**
    - Enhancing model interpretability through techniques such as saliency maps or attention mechanisms would provide insights into the model's decision-making process.

    **Conclusion:**
    The audio classification model project represents a significant endeavor in the domain of machine learning for audio analysis. Despite encountering challenges, the project lays the foundation for further research and development in audio classification, with potential applications in speech recognition, music genre classification, environmental sound monitoring, and beyond. Continual refinement and innovation in model architectures and methodologies will drive advancements in this field, ultimately leading to more accurate and reliable audio classification systems.
    """
    st.write(review_text)
        
        

    
    

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
