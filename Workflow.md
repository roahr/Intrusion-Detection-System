# Intrusion Detection System

An Intrusion Detection System (IDS) is a system that monitors network traffic for suspicious activity and issues alerts when such activity is discovered.Any malicious venture or violation is normally reported either to an administrator or collected centrally using a security information and event management (SIEM) system. A SIEM system integrates outputs from multiple sources and uses alarm filtering techniques to differentiate malicious activity from false alarms

This Intrusion Detection System (IDS) utilizes machine learning models to classify network traffic as either normal or malicious. The system leverages two pre-trained models in a cascaded approach to enhance detection accuracy.

## Dataset Description

### **About Dataset :** https://www.unb.ca/cic/datasets/ids-2017.html

### **DataFrame Size:** 2,830,743 entries x 79 columns

### Snippet :

|     | Destination Port | Flow Duration | Total Fwd Packets | Total Backward Packets | Total Length of Fwd Packets | Total Length of Bwd Packets | Fwd Packet Length Max | Fwd Packet Length Min | Fwd Packet Length Mean | Fwd Packet Length Std | ... | min_seg_size_forward | Active Mean | Active Std | Active Max | Active Min | Idle Mean | Idle Std | Idle Max | Idle Min | Label  |
| --- | ---------------- | ------------- | ----------------- | ---------------------- | --------------------------- | --------------------------- | --------------------- | --------------------- | ---------------------- | --------------------- | --- | -------------------- | ----------- | ---------- | ---------- | ---------- | --------- | -------- | -------- | -------- | ------ |
| 0   | 54865            | 3             | 2                 | 0                      | 12                          | 0                           | 6                     | 6                     | 6.0                    | 0.0                   | ... | 20                   | 0.0         | 0.0        | 0          | 0          | 0.0       | 0.0      | 0        | 0        | BENIGN |
| 1   | 55054            | 109           | 1                 | 1                      | 6                           | 6                           | 6                     | 6                     | 6.0                    | 0.0                   | ... | 20                   | 0.0         | 0.0        | 0          | 0          | 0.0       | 0.0      | 0        | 0        | BENIGN |
| 2   | 55055            | 52            | 1                 | 1                      | 6                           | 6                           | 6                     | 6                     | 6.0                    | 0.0                   | ... | 20                   | 0.0         | 0.0        | 0          | 0          | 0.0       | 0.0      | 0        | 0        | BENIGN |
| 3   | 46236            | 34            | 1                 | 1                      | 6                           | 6                           | 6                     | 6                     | 6.0                    | 0.0                   | ... | 20                   | 0.0         | 0.0        | 0          | 0          | 0.0       | 0.0      | 0        | 0        | BENIGN |
| 4   | 54863            | 3             | 2                 | 0                      | 12                          | 0                           | 6                     | 6                     | 6.0                    | 0.0                   | ... | 20                   | 0.0         | 0.0        | 0          | 0          | 0.0       | 0.0      | 0        | 0        | BENIGN |

### Activities :

| Activity ID | Activity                   |
| ----------- | -------------------------- |
| 0           | Normal Activity (BEGNIN)   |
| 1           | DoS Hulk                   |
| 2           | PortScan                   |
| 3           | DDoS                       |
| 4           | DoS GoldenEye              |
| 5           | FTP-Patator                |
| 6           | SSH-Patator                |
| 7           | DoS slowloris              |
| 8           | DoS Slowhttptest           |
| 9           | Bot                        |
| 10          | Web Attack – Brute Force   |
| 11          | Web Attack – XSS           |
| 12          | Infiltration               |
| 13          | Web Attack – Sql Injection |
| 14          | Heartbleed                 |

<div style="page-break-after: always;"></div>

### Features Selection :

#### **Domain Knowledge Based Analysis**

### High-Priority Features (16):

1. **Destination Port:** Crucial for identifying suspicious traffic targeting specific ports often used in attacks. Traditional attacks like port scans and some DoS attempts exploit well-known ports.
2. **Flow Duration:** Deviations from normal session lengths can indicate attacks. Short or extremely long durations might be suspicious.
3. **Flow Bytes:** Unusual data transfer volume can be a hallmark of DoS attacks, where attackers flood the network with traffic.
4. **Flow Packets:** Abnormal packet counts within a flow suggest potential attacks. Similar to Flow Bytes, high packet counts can be indicative of DoS attempts.
5. **Fwd Packets/s & Bwd Packets/s:** High packet rates in either direction can be indicative of DoS attempts. These features capture the rate of packet transmission, which can be a red flag for flooding attacks.
6. **FIN Flag Count:** Abnormal usage patterns might suggest attacks attempting connection termination abruptly (e.g., SYN floods might use premature FIN flags).
7. **SYN Flag Count:** High SYN flag counts can be a sign of DoS attacks like SYN floods, which exploit excessive connection initiation requests.
8. **RST Flag Count:** Frequent resets could indicate issues or attacks exploiting connection resets (e.g., some DoS attacks might trigger abnormal resets).
9. **PSH Flag Count:** Unusual PSH flag usage might be associated with specific attacks. PSH flags indicate the desire to push data immediately, and some attacks might leverage this for faster exploitation.
10. **ACK Flag Count:** Deviations from normal ACK flag patterns can be suspicious. Abnormal acknowledgements can be a sign of manipulated communication flows.
11. **Packet Length Mean:** Significant changes in average packet size can point to DoS attacks using abnormally small or large packets. Unusual packet sizes can disrupt normal network communication.
12. **Packet Length Std:** High standard deviation in packet sizes can reveal unusual packet size distribution in DoS attacks. This captures the variability in packet sizes, which can be a sign of DoS attempts using packets of different sizes.
13. **ECE Flag Count:** Some DoS attacks might use Explicit Congestion Notification (ECE) flags to trick the network into congestion control measures.
14. **Down/Up Ratio:** Significant imbalance in upload/download traffic can be suspicious. This can indicate attacks targeting specific directions (e.g., upload DoS attacks).
15. **Average Packet Size:** While less specific than individual packet sizes (Mean and Std), it can offer additional insights into overall traffic patterns.

#### **Features Excluded and Why:**

- **Fwd IAT total & Bwd IAT total:** While inter-arrival time deviations might be helpful, they might be less informative than packet rates (Fwd/Bwd Packets/s) for identifying flooding attacks. Packet rates directly capture the volume of traffic, making them more reliable indicators.
- **Fwd PSH Flags, Bwd PSH Flags, Fwd URG Flags, Bwd URG Flags:** Flag usage can be informative, but some attacks might not rely heavily on these specific flags. Focusing on general flags like FIN, SYN, RST, PSH, and ACK provides broader coverage.
- **Fwd Header Length, Bwd Header Length:** Header length deviations might be subtle indicators and less impactful compared to other features.
- **Packet Length Variance:** This is highly correlated with Packet Length Std and provides redundant information.

### **Combined Feature Selection - Top 30 Features**

| Rank                                                | Feature                 | Domain Knowledge Relevance                                                         | Covariance | Possible Attack Types                                                                            |
| --------------------------------------------------- | ----------------------- | ---------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------ |
| 1                                                   | Active Max              | Potential for unusual activity patterns (DoS attacks might alter traffic patterns) | 0.353577   | DoS GoldenEye, DoS Hulk, DDoS                                                                    |
| 2                                                   | Idle Min                | Might be indicative of abnormal connection behavior                                | 0.348527   | Infiltration (scanning), Bot (unusual connection patterns)                                       |
| 3                                                   | Active Mean             | Potential for unusual activity patterns (DoS attacks might alter traffic patterns) | 0.341331   | DoS GoldenEye, DoS Hulk, DDoS                                                                    |
| 4                                                   | Idle Mean               | Might be indicative of abnormal connection behavior                                | 0.332132   | Infiltration (scanning), Bot (unusual connection patterns)                                       |
| 5                                                   | Fwd IAT Std             | Deviations in inter-arrival times can point to DoS attacks                         | 0.324352   | DoS GoldenEye, DoS Hulk (potential)                                                              |
| 6                                                   | PSH Flag Count          | Unusual PSH flag usage might be associated with specific attacks                   | 0.311891   | DoS GoldenEye (potential), DoS Hulk (potential), Web Attack (potential)                          |
| 7                                                   | Idle Max                | Might be indicative of abnormal connection behavior                                | 0.302576   | Infiltration (scanning), Bot (unusual connection patterns)                                       |
| 8                                                   | URG Flag Count          | Less common flag, high values might be suspicious                                  | 0.297769   | Scan (unusual flags), Web Attack (potential)                                                     |
| 9                                                   | SYN Flag Count          | High SYN flag counts can be a sign of DoS attacks (SYN floods)                     | 0.296373   | DoS GoldenEye (SYN floods), DoS Hulk                                                             |
| 10                                                  | Fwd PSH Flags           | Unusual PSH flag usage might be associated with specific attacks                   | 0.296373   | DoS GoldenEye (potential), DoS Hulk (potential), Web Attack (potential)                          |
| 11                                                  | Fwd IAT Max             | Significant deviations might suggest abnormal packet arrival patterns              | 0.292901   | DoS GoldenEye (potential), DoS Hulk (potential)                                                  |
| 12                                                  | Flow IAT Max            | Deviations in inter-arrival times within a flow can be suspicious                  | 0.291906   | DoS GoldenEye (potential), DoS Hulk (potential)                                                  |
| 13                                                  | Active Min              | Potential for unusual activity patterns (DoS attacks might alter traffic patterns) | 0.288449   | DoS GoldenEye, DoS Hulk, DDoS                                                                    |
| 14                                                  | Init_Win_bytes_forward  | Suspicious window sizes might indicate some attacks                                | 0.277809   | Infiltration (scanning), Bot (unusual connection establishment)                                  |
| 15                                                  | Init_Win_bytes_backward | Suspicious window sizes might indicate some attacks                                | 0.272854   | Infiltration (scanning), Bot (unusual connection establishment)                                  |
| 16                                                  | FIN Flag Count          |DoS attacks might use abnormal termination patterns | 0.264020                | DoS GoldenEye (SYN floods), DoS Hulk (potential)                                   |
| 17                                                  | Flow IAT Std            | Deviations in inter-arrival times within a flow                                    | 0.249098   | DoS GoldenEye (potential), DoS Hulk (potential)                                                  |
| 18                                                  | Flow Duration           | Deviations from normal session lengths                                             | 0.245105   | DoS GoldenEye, DoS Hulk, DoS Slowhttp, DoS Slowloris, Web Attack (short bursts/long connections) |
| 19                                                  | Fwd Packet Length Std   | Unusual packet sizes can disrupt normal communication                              | 0.237610   | DoS GoldenEye (potential), DoS Hulk (potential)                                                  |
| 20                                                  | ACK Flag Count          | Deviations from normal ACK flag patterns can be suspicious                         | 0.149964   | DoS GoldenEye (potential), DoS Hulk (potential), Infiltration (manipulated communication)        |
| 21                                                  | Active Std              | Potential for unusual activity patterns                                            | 0.202967   | DoS GoldenEye, DoS Hulk, DDoS                                                                    |
| 22                                                  | Fwd Packets/s           | High packet rates can be indicative of DoS attacks                                 | 0.178667   | DoS GoldenEye, DoS Hulk, DDoS                                                                    |
| 23                                                  | Bwd IAT Min             | Less informative than other IAT features                                           | 0.203635   | Less useful for IDS                                                                              |
| 24                                                  | ECE Flag Count          | Some DoS attacks might use Explicit Congestion Notification (ECE) flags            | Included   | DoS GoldenEye (potential), DoS Hulk (potential)                                                  |
| 25                                                  | RST Flag Count          | Frequent resets could indicate issues or attacks exploiting connection resets      | Included   | DoS GoldenEye (potential), DoS Hulk (potential), Infiltration (exploiting resets)                |
| 26                                                  | Fwd IAT Min             | Less informative than other IAT features                                           | 0.178470   | Less useful for IDS                                                                              |
| 27                                                  | Bwd PSH Flags           | Might be useful for some attacks, but weigh against redundancy with other flags    | Included   | DoS GoldenEye (potential), DoS Hulk (potential), Web Attack (potential)                          |
| 28                                                  | Bwd URG Flags           | Similar to Bwd PSH Flags, consider potential redundancy                            | Included   | DoS GoldenEye (potential), DoS Hulk (potential), Web Attack (potential)                          |
| 29                                                  | 'Fwd Header Length'     | Suspicious window sizes might indicate some attacks                                | 0.277809   | Infiltration (scanning), Bot (unusual connection establishment)                                  |
| 30                                                  | 'Bwd Header Length'     | Suspicious window sizes might indicate some attacks                                | 0.272854   | Infiltration (scanning), Bot (unusual connection establishment)                                  |

<div style="page-break-after: always;"></div>

## Preprocessing

## Data Preprocessing Overview

### 1. Loading the Dataset

The dataset is loaded into memory using the appropriate data loading function (`pd.read_csv()` in this case) from the data manipulation library, such as Pandas.

### 2. Splitting the Data with Detection of Anomalies

Anomalies or outliers are identified and separated from the main dataset based on specific criteria. These anomalies may be removed or flagged for further analysis.

### 3. Mapping Labels

Categorical labels are mapped to numerical values to facilitate model training. This process involves creating a mapping dictionary and updating the label column accordingly.

### 4. Handling Null Values

Null values or missing data points in the dataset are identified and handled appropriately. Common strategies include imputation (replacing null values with a suitable value) or removal of rows/columns with null values.

### 5. Applying Standard Scalar

Feature scaling is performed to ensure that all features have a similar scale, preventing any particular feature from dominating the learning algorithm due to its larger magnitude. The Standard Scalar is a common method used for this purpose, which standardizes features by removing the mean and scaling to unit variance.

## Methodology

### Synthetic Minority Over-sampling Technique (SMOTE)

#### Dataset Label Distribution

The dataset consists of various types of network traffic, each labeled with a specific category. However, upon analysis, it's evident that the distribution of these labels is highly imbalanced. Some categories have significantly more instances compared to others. Here is the distribution of labels in the dataset:

- DoS Hulk: 231,073
- PortScan: 158,930
- DDoS: 128,027
- DoS GoldenEye: 10,293
- FTP-Patator: 7,938
- SSH-Patator: 5,897
- DoS slowloris: 5,796
- DoS Slowhttptest: 5,499
- Bot: 1,966
- Web Attack – Brute Force: 1,507
- Web Attack – XSS: 652
- Infiltration: 36
- Web Attack – Sql Injection: 21
- Heartbleed: 11

#### Resampling with SMOTE

To address the imbalance in label distribution and ensure that each category has sufficient representation for effective model training, the Synthetic Minority Over-sampling Technique (SMOTE) is employed.

SMOTE generates synthetic samples for the minority classes by interpolating between existing samples. This oversampling technique creates new synthetic instances of the minority class by selecting similar instances and perturbing them in feature space. By doing so, SMOTE balances the class distribution, making the dataset more suitable for training machine learning models.

### Principal Components Analysis (PCA)

**Here we reduce the 30 features into 10 Components**

#### Model 1

| Column Number | Column Name                                                                                                                                                                        | Dtype   |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| 0             | Idle Max - Flow IAT Max - Fwd IAT Max - Idle Mean - Idle Min - Flow IAT Std - Fwd IAT Std - Flow Duration - Bwd IAT Min - Fwd IAT Min                                              | float64 |
| 1             | Active Max - Active Mean - Active Min - Active Std - PSH Flag Count - Init_Win_bytes_forward - Fwd Packet Length Std - Flow Duration - Init_Win_bytes_backward - RST Flag Count    | float64 |
| 2             | SYN Flag Count - Fwd PSH Flags - ACK Flag Count - Fwd Packets/s - Active Mean - Active Max - Active Min - URG Flag Count - Active Std - Bwd IAT Min                                | float64 |
| 3             | ECE Flag Count - RST Flag Count - SYN Flag Count - Fwd PSH Flags - Init_Win_bytes_forward - Fwd Packet Length Std - PSH Flag Count - Fwd Packets/s - ACK Flag Count - Fwd IAT Std  | float64 |
| 4             | Bwd IAT Min - Fwd IAT Min - Flow IAT Std - PSH Flag Count - Fwd PSH Flags - SYN Flag Count - Init_Win_bytes_forward - Active Std - Active Max - Active Mean                        | float64 |
| 5             | URG Flag Count - ACK Flag Count - Active Min - Active Mean - Active Max - Fwd IAT Min - Init_Win_bytes_backward - Bwd IAT Min - RST Flag Count - ECE Flag Count                    | float64 |
| 6             | FIN Flag Count - Fwd Packets/s - Active Mean - Active Min - Active Max - Active Std - ECE Flag Count - RST Flag Count - SYN Flag Count - Fwd PSH Flags                             | float64 |
| 7             | Active Std - Active Max - Flow Duration - URG Flag Count - FIN Flag Count - Init_Win_bytes_backward - ACK Flag Count - Bwd IAT Min - Bwd PSH Flags - Bwd URG Flags                 | float64 |
| 8             | Active Min - Init_Win_bytes_forward - Fwd Packet Length Std - Fwd PSH Flags - SYN Flag Count - PSH Flag Count - Init_Win_bytes_backward - Flow IAT Max - Fwd IAT Max - Fwd IAT Std | float64 |
| 9             | Fwd Packets/s - Init_Win_bytes_backward - FIN Flag Count - Init_Win_bytes_forward - PSH Flag Count - Fwd IAT Min - Bwd IAT Min - Active Min - Active Mean - Flow IAT Std           | float64 |

#### Model 2

|     | Column                                                                                                                                                                                  | Dtype   |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| 0   | Fwd Header Length - Bwd Header Length - Flow Duration - Active Std - ACK Flag Count - Active Max - Active Mean - Fwd Packet Length Std - Active Min - ECE Flag Count                    | float64 |
| 1   | Active Max - Active Std - Active Mean - Active Min - Bwd Header Length - SYN Flag Count - Fwd PSH Flags - Fwd Packet Length Std - Bwd IAT Min - Flow Duration                           | float64 |
| 2   | SYN Flag Count - Fwd PSH Flags - Fwd IAT Min - Bwd IAT Min - ACK Flag Count - URG Flag Count - Fwd Packet Length Std - Flow IAT Std - Flow Duration - Idle Max                          | float64 |
| 3   | Init_Win_bytes_backward - SYN Flag Count - Fwd PSH Flags - Bwd IAT Min - Fwd IAT Min - Flow IAT Std - Active Std - Bwd Header Length - Fwd IAT Max - Flow Duration                      | float64 |
| 4   | Bwd Header Length - URG Flag Count - SYN Flag Count - Fwd PSH Flags - Fwd Packet Length Std - ACK Flag Count - Init_Win_bytes_backward - Fwd Packets/s - Bwd PSH Flags - ECE Flag Count | float64 |
| 5   | Active Std - URG Flag Count - Bwd IAT Min - Init_Win_bytes_backward - Fwd Header Length - ACK Flag Count - Fwd IAT Min - Active Max - ECE Flag Count - RST Flag Count                   | float64 |
| 6   | Active Std - Fwd Packet Length Std - Bwd IAT Min - Bwd Header Length - PSH Flag Count - Init_Win_bytes_forward - Fwd IAT Min - Flow IAT Std - Flow Duration - Idle Max                  | float64 |
| 7   | Fwd IAT Min - Bwd IAT Min - Active Min - Flow IAT Std - URG Flag Count - Idle Min - Idle Mean - Fwd IAT Max - Idle Max - Flow IAT Max                                                   | float64 |
| 8   | Fwd Packet Length Std - URG Flag Count - Init_Win_bytes_backward - Flow Duration - Flow IAT Std - Flow IAT Max - Idle Max - Fwd IAT Max - Idle Mean - Idle Min                          | float64 |
| 9   | Bwd IAT Min - PSH Flag Count - Init_Win_bytes_forward - Fwd Packet Length Std - Fwd IAT Min - Active Min - URG Flag Count - Fwd PSH Flags - SYN Flag Count - Active Mean                | float64 |

<div style="page-break-after: always;"></div>

## Models Used

### Model 1 : To classify the netowrk traffic as abnormal or not

| Model              | Training Accuracy | Test Accuracy | Training Precision | Test Precision | Training Recall | Test Recall |
| ------------------ | ----------------- | ------------- | ------------------ | -------------- | --------------- | ----------- |
| KNeighbors         | 99.82%            | 99.75%        | 99.34%             | 99.12%         | 99.73%          | 99.62%      |
| LogisticRegression | 83.94%            | 83.91%        | 74.54%             | 74.59%         | 27.95%          | 28.02%      |

### Model 2 : To classify the abnormal netowrk traffic to Possible Attack

| Model        | Training Accuracy | Test Accuracy | Confusion Matrix                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | ----------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| KNeighbors   | 99.1846           | 98.7807       | [[58031, 6, 1, 38, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0], [7, 57899, 1, 0, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0], [5, 0, 57375, 11, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0], [17, 0, 0, 57881, 0, 0, 0, 11, 0, 22, 12, 0, 52, 0], [0, 0, 0, 0, 57695, 0, 3, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 57684, 0, 5, 0, 4, 0, 0, 0, 0], [2, 1, 0, 14, 0, 2, 57749, 113, 3, 3, 5, 0, 0, 0], [0, 0, 0, 5, 0, 0, 198, 57353, 3, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 57941, 3, 0, 10, 0, 0], [0, 0, 0, 23, 0, 1, 0, 0, 0, 52666, 4923, 0, 7, 0], [0, 1, 0, 21, 0, 0, 0, 0, 0, 4308, 53547, 0, 5, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 57845, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 57371, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 57858]] |
| RandomForest | 99.9289           | 98.9831       | [[58049, 7, 0, 22, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], [7, 57899, 0, 1, 0, 0, 0, 0, 0, 2, 2, 1, 0, 0], [2, 0, 57388, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0], [9, 0, 0, 57942, 0, 0, 0, 5, 0, 1, 0, 0, 38, 0], [0, 0, 0, 0, 57697, 0, 3, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 57688, 0, 4, 0, 0, 0, 0, 0, 0], [1, 0, 0, 5, 0, 1, 57802, 74, 4, 2, 3, 0, 0, 0], [0, 0, 0, 6, 0, 1, 214, 57339, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 57946, 0, 0, 8, 0, 0], [0, 0, 0, 16, 0, 1, 1, 0, 0, 53558, 4041, 0, 3, 0], [0, 1, 0, 1, 0, 0, 1, 0, 0, 3725, 54151, 0, 3, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 57845, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 57370, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 57858]]          |

## Working

### Functionality Breakdown

1. **Data Preprocessing**: Incoming data points are preprocessed to ensure compatibility with the models. This might involve scaling numerical features and applying Principal Component Analysis (PCA) for dimensionality reduction.
2. **Initial Classification with Model 1**: The preprocessed data is fed into the first model (Random Forest). This model provides an initial classification of the traffic into _Normal_ or _Abnormal_ Activity.
3. **Confidence Score**: The confidence score associated with the Model 1 prediction is retrieved. This score indicates the model's certainty in its classification.
4. **Further Classification with Model 2 (if needed)**: If the initial prediction from Model 1 suggests an _Anomaly_, the data is passed through a second model (KNeighbors) for a more granular classification. This step helps identify specific attack types.
5. **Threat Level Determination**: Based on the final prediction (from Model 1 or 2), a threat level is assigned (0 - No Threat, 1 - Threat).
6. **Attack Type Identification (if Threat)**: If a threat is detected, the corresponding attack type is retrieved from a pre-defined mapping dictionary using the final prediction value.
7. **Output**: The system outputs a report containing the threat level, possible attack type (if applicable), and confidence score. This information can be used to trigger alerts, block malicious traffic, or for further investigation by security personnel.

### Flow Diagram

<img src="D:\College_sem4\ML_CIA\Final\Dataset\Flow\Model.jpeg" width=300>
<img src="D:\College_sem4\ML_CIA\Final\Dataset\Flow\all.jpeg" width=600>

<div style="page-break-after: always;"></div>

## Result

<img src="C:\Users\Roahith\Documents\ShareX\Screenshots\2024-04\chrome_XHF0EZAh2q.png">

## Future Scope

- If your dataset includes features related to **connection origin** (source IP) and **duration**, they can be valuable for detecting infiltration and bot attacks.
- For **Web Attacks**, consider incorporating features related to **User-Agent** strings, **request methods** (e.g., excessive GET or POST requests), and **URLs** targeting vulnerabilities (if available).
- **Heartbleed:** While network traffic features might show anomalies, consider system-level features related to **OpenSSL versions** or specific error messages (if your data source provides them).

### Features For Consideration:

1. **Connection Origin (Source IP):** Valuable for detecting infiltration and bot attacks. Possibility of exposing TOR end-nodes, such that can be blocked immediately.
2. **User-Agent (if available):** Valuable for detecting web attacks targeting specific user agents.
3. **Request Methods (if available):** Abnormal request methods (e.g., excessive GET or POST) can indicate web attacks.
4. **URLs (if available):** URLs targeting vulnerabilities can be indicative of web attacks.
5. **OpenSSL Version (if available):** System-level feature for Heartbleed detection.
6. **Specific Error Messages (if available):** System-level feature for Heartbleed detection.

