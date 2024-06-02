import streamlit as st
import pandas as pd
from prediction import *

st.set_page_config(
    page_title="Intrusion Detection System (IDS)", page_icon=":guardsman:")


def render_footer():
    st.markdown("< / Made with ❤️ For ML CIA >", unsafe_allow_html=True)


def preprocess_uploaded_data(uploaded_file):
    # Read the uploaded file
    df = pd.read_csv(uploaded_file)

    # Assuming 'Label' column contains the target labels
    actual_labels = df[' Label']

    # Drop 'Label' column from the data
    df = df.drop(columns=[' Label'])

    # Select the necessary features
    selected_features = [
        ' Active Max', ' Idle Min', 'Active Mean', 'Idle Mean', ' Fwd IAT Std',
        ' PSH Flag Count', ' Idle Max', ' URG Flag Count', ' SYN Flag Count',
        'Fwd PSH Flags', ' Fwd IAT Max', ' Flow IAT Max', ' Active Min',
        'Init_Win_bytes_forward', ' Init_Win_bytes_backward', 'FIN Flag Count',
        ' Flow IAT Std', ' Flow Duration', ' Fwd Packet Length Std', ' ACK Flag Count',
        ' Active Std', 'Fwd Packets/s', ' Bwd IAT Min', ' ECE Flag Count',
        ' RST Flag Count', ' Fwd IAT Min', ' Bwd PSH Flags', ' Bwd URG Flags',
        ' Fwd Header Length', ' Bwd Header Length',
    ]

    df = df[selected_features]

    df = standard_scaler.transform(
        df.values.reshape(1, -1))

    # Perform any necessary scaling or transformations

    return df, actual_labels


def test_uploaded_data():
    st.title('Intrusion Detection System')
    st.markdown('## Test IDS with Uploaded Data:')

    st.write("Please upload a CSV file containing the data you want to predict.")

    st.markdown("""
    ### Expected CSV Format:
    - The CSV file should contain the data you want to predict.
    - These features include network traffic characteristics like:
        * Active periods (Max, Min, Mean, Std)
        * Idle periods (Max, Min, Mean)
        * Packet characteristics (IAT - Interarrival Time Std, Length Std)
        * Flag counts (PSH, URG, SYN, FIN, ACK, ECE, RST)
        * Window sizes (Initial Window size - forward and backward)
        * Flow duration
        * Header lengths (forward and backward)
    

    **Note:** Make sure the CSV file is in the correct format before uploading.
    """)

    uploaded_file = st.file_uploader("Upload CSV file", type="csv")

    if uploaded_file is not None:
        try:
            with st.spinner('Preprocessing uploaded data...'):
                data, actual = preprocess_uploaded_data(uploaded_file)

            # Display uploaded data
            st.subheader('Uploaded Data:')
            st.write(data.head())

            with st.spinner('Making prediction...'):
                predictions = predict_csv(data)

            # Display prediction results
            st.subheader('Prediction Results:')
            st.write(predictions)

        except Exception as e:
            st.error(f"Error during prediction: {e}")

    render_footer()


# test_uploaded_data()
