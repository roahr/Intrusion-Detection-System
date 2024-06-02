import streamlit as st
import pandas as pd
from prediction import *

st.set_page_config(
    page_title="Intrusion Detection System (IDS)", page_icon=":guardsman:")


def render_footer():
    st.markdown("< / Made with ❤️ For ML CIA >", unsafe_allow_html=True)


def test_random_data():
    st.title('Intrusion Detection System')
    st.markdown('## Test IDS with Random Data:')

    if st.button('Predict Random Sample'):
        try:

            with st.spinner('Baking Custom Datapoints...'):
                d = sample_data_new()
                data, actual = d[0], d[1]

            # Display chosen sample data
            st.subheader('Sample Data:')
            # Display actual label and selected features
            st.write(actual)

            with st.spinner('Making prediction...'):
                prediction = predict(data)

            # Display prediction results

            threat_level = prediction['Threat']
            confidence = prediction['Confidence']
            threat_scale = st.empty()

            if threat_level == 0:
                threat_scale.success(
                    f"""Threat Level: Low  -- Confidence Score: {(float(confidence))*100} % \n\n
                        More Info : {prediction['Possible Attack']}""")

            else:
                threat_scale.error(
                    f"""Threat Level: High -- Confidence Score: {(float(confidence))*100} %")\n\n
                    More Info : {prediction['Possible Attack']}""")

        except Exception as e:
            st.error(f"Error during prediction: {e}")

    render_footer()


test_random_data()
