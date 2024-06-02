import pandas as pd
import random
import joblib

# Load models and other necessary objects
model1 = joblib.load('Model1/RandomForest_model1.pkl')
model2 = joblib.load('Model2/KNeighbors_model2.pkl')
pca_model1 = joblib.load('Model1/Objects/pca_object_model1.pkl')
pca_model2 = joblib.load('Model2/Objects/pca_object_model2.pkl')
standard_scaler = joblib.load('Model1/Objects/standard_scaler_object.pkl')

# Dictionary mapping of attacks
mapping = {
    '0': 'Normal Activity', '1': 'DoS Hulk', '2': 'PortScan', '3': 'DDoS', '4': 'DoS GoldenEye', '5': 'FTP-Patator',
    '6': 'SSH-Patator', '7': 'DoS slowloris', '8': 'DoS Slowhttptest', '9': 'Bot', '10': 'Web Attack – Brute Force',
    '11': 'Web Attack    – XSS', '12': 'Infiltration', '13': 'Web Attack – Sql Injection', '14': 'Heartbleed'
}

# Function to predict using model1


def predict_model1(data):
    data = pca_model1.transform(data)
    prediction = model1.predict(data)
    return prediction, data

# Function to predict using model2


def predict_model2(data):
    data = pca_model2.transform(data)
    prediction = model2.predict(data)
    return prediction, data

# Function to sample new data


def sample_data_new():
    df = pd.read_csv('D:/College_sem4/ML_CIA/CICIDS2017.csv')
    random_index = random.randint(0, len(df) - 1)
    random_datapoint = df.iloc[random_index]

    Actual_Label_Data = random_datapoint
    random_datapoint = random_datapoint.drop(' Label')

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

    random_datapoint = random_datapoint[selected_features]
    random_datapoint = standard_scaler.transform(
        random_datapoint.values.reshape(1, -1))

    return random_datapoint, Actual_Label_Data

# Function to predict


def predict(data):
    prediction1, data_pca1 = predict_model1(data)
    confidence1 = model1.predict_proba(data_pca1)[0][prediction1]

    prediction2 = None

    if prediction1 == 1:
        prediction2, data_pca2 = predict_model2(data)

    combined_confidence = confidence1[0]

    if prediction1 == 1:
        if prediction2 == 0:
            return {'Threat': 0, 'Possible Attack': 'No Threat - Good To Go', 'Confidence': combined_confidence}
        else:
            possible_attack = mapping.get(str(prediction2[0]), 'Unknown')
            return {'Threat': 1, 'Possible Attack': possible_attack, 'Confidence': combined_confidence}
    else:
        return {'Threat': 0, 'Possible Attack': 'No Threat - Good To Go', 'Confidence': combined_confidence}


def predict_csv(data_df):
    predictions = []
    for index, row in data_df.iterrows():
        prediction = predict(row.values.reshape(1, -1))
        predictions.append(prediction)

    predictions_df = pd.DataFrame(predictions)

    predictions_df.rename(
        columns={'Possible Attack': 'More Info'}, inplace=True)

    return predictions_df
