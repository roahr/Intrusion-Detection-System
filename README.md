# Intrusion-Detection-System
# Intrusion Detection System (IDS)

Welcome to the Intrusion Detection System (IDS) repository! This system is designed to monitor network traffic for suspicious activity and classify it as normal or potentially malicious using machine learning models. 

## Dataset Description

The dataset used in this IDS project contains 2,830,743 entries with 79 columns. It's sourced from [UNB's CIC IDS 2017 dataset](https://www.unb.ca/cic/datasets/ids-2017.html) and covers various network activities, including both benign and malicious traffic.

## Workflow Overview

1. **Data Preprocessing**: The incoming data is preprocessed to ensure compatibility with the models. This includes handling null values, mapping labels, and applying standard scaling.
   
2. **Initial Classification (Model 1)**: The preprocessed data is fed into the first model, typically a Random Forest classifier, to determine whether the traffic is normal or abnormal.

3. **Further Classification (Model 2)**: If Model 1 indicates abnormal activity, the data is passed through a second model, often a KNeighbors classifier, for more granular classification, identifying specific attack types.

4. **Threat Level Determination**: Based on the final prediction, a threat level is assigned, indicating the severity of the detected activity.

5. **Output and Reporting**: The system generates a report containing the threat level, possible attack type, and confidence score. This information can trigger alerts or further investigation.

## Models Used

### Model 1: Binary Classification (Normal vs. Abnormal Traffic)

Two models are typically used for initial classification:

- **Random Forest**: Achieves high accuracy in classifying traffic as normal or abnormal.
- **Logistic Regression**: Provides additional insights into the data, although with slightly lower accuracy.

### Model 2: Multi-Class Classification (Type of Attack)

For granular classification of abnormal traffic, KNeighbors and RandomForest classifiers are employed to identify specific attack types.

## Result and Performance

The IDS system exhibits high accuracy and precision in both binary and multi-class classification tasks. Below is a summary of the model performance:

- **Model 1 (Binary Classification)**
  - Random Forest: Training Accuracy - 99.82%, Test Accuracy - 99.75%
  - Logistic Regression: Training Accuracy - 83.94%, Test Accuracy - 83.91%

- **Model 2 (Multi-Class Classification)**
  - KNeighbors: Training Accuracy - 99.1846%, Test Accuracy - 98.7807%
  - RandomForest: Training Accuracy - 99.9289%, Test Accuracy - 98.9831%



## Getting Started

To get started with the IDS system, follow these steps:

1. **Clone the Repository**: Clone or download this repository to your local machine.
2. **Install Dependencies**: Make sure you have all the required dependencies installed. Check the `requirements.txt` file for details.
3. **Preprocess Data**: Use the provided scripts or notebooks to preprocess your data.
4. **Train Models**: Train the models using the preprocessed data.
5. **Run the System**: Run the IDS system and analyze the results.

Feel free to explore and modify the system according to your requirements and data characteristics.

Happy detecting! 🛡️👀