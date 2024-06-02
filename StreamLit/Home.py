import streamlit as st
import pandas as pd
from prediction import *

st.set_page_config(
    page_title="Intrusion Detection System (IDS)", page_icon=":guardsman:")


def render_footer():
    st.markdown("< / Made with ❤️ For ML CIA >", unsafe_allow_html=True)


def render_home():
    st.title('Intrusion Detection System (IDS)')

    st.markdown("#### This Intrusion Detection System (IDS) utilizes machine learning models to classify network traffic as either normal or malicious. The system leverages two pre-trained models in a cascaded approach to enhance detection accuracy.")
    st.markdown("#### Here's a breakdown of the functionality:")
    st.markdown("1. **Data Preprocessing**: Incoming data points are preprocessed to ensure compatibility with the models. This might involve scaling numerical features and applying Principal Component Analysis (PCA) for dimensionality reduction.")
    st.markdown("2. **Initial Classification with Model 1**: The preprocessed data is fed into the first model (Random Forest). This model provides an initial classification of the traffic into *Normal* or *Abnormal* Activity.")
    st.markdown("3. **Confidence Score**: The confidence score associated with the Model 1 prediction is retrieved. This score indicates the model's certainty in its classification.")
    st.markdown("4. **Further Classification with Model 2 (if needed)**: If the initial prediction from Model 1 suggests a *Anpmaly*, the data is passed through a second model (KNeighbors) for a more granular classification. This step helps identify specific attack types.")
    st.markdown("5. **Threat Level Determination**: Based on the final prediction (from Model 1 or 2), a threat level is assigned (0 - No Threat, 1 - Threat).")
    st.markdown("6. **Attack Type Identification (if Threat)**: If a threat is detected, the corresponding attack type is retrieved from a pre-defined mapping dictionary using the final prediction value.")
    st.markdown("7. **Output**: The system outputs a report containing the threat level, possible attack type (if applicable), and confidence score. This information can be used to trigger alerts, block malicious traffic, or for further investigation by security personnel.")

    st.markdown("#### Flow Diagram : ")
    st.image('D:\College_sem4\ML_CIA\Final\Dataset\Flow\Model.jpeg', width=300)

    st.markdown("### Activities Detected by IDS:")

    activities = {
        '0': 'Normal Activity (BEGNIN)',
        '1': 'DoS Hulk',
        '2': 'PortScan',
        '3': 'DDoS',
        '4': 'DoS GoldenEye',
        '5': 'FTP-Patator',
        '6': 'SSH-Patator',
        '7': 'DoS slowloris',
        '8': 'DoS Slowhttptest',
        '9': 'Bot',
        '10': 'Web Attack – Brute Force',
        '11': 'Web Attack – XSS',
        '12': 'Infiltration',
        '13': 'Web Attack – Sql Injection',
        '14': 'Heartbleed'
    }

    # Create a table to display activities
    st.table(
        pd.DataFrame.from_dict(
            activities, orient='index', columns=['Activity']).style.set_table_styles(
            [{'selector': 'tr:hover', 'props': 'background-color: #ddd;'}])
    )


if __name__ == "__main__":
    render_home()
