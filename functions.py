from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd


def train_and_predict_N_category(df, humidity, temperature, rainfall, ph, id_value):
    # Encode the categorical 'id' column
    label_encoder = LabelEncoder()
    df['id'] = label_encoder.fit_transform(df['id'])

    # Features and target variable
    X = df[['humidity', 'temperature', 'rainfall', 'ph', 'id']]

    if 'N' not in df.columns:
        raise KeyError("'N' column is missing in the DataFrame")
    y = df['N']

    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create and train the Gradient Boosting Classifier model
    gb_classifier = GradientBoostingClassifier(random_state=42)
    gb_classifier.fit(X_scaled, y)

    # Encode the input 'id_value'
    id_encoded = label_encoder.fit_transform([id_value])

    # Scale the input values
    input_scaled = scaler.transform(
        [[humidity, temperature, rainfall, ph, id_encoded[0]]])

    # Make predictions
    predicted_n_category = gb_classifier.predict(input_scaled)

    return predicted_n_category[0]


def train_and_predict_K_category(df, humidity, temperature, rainfall, ph, id_value):
    # Encode the categorical 'id' column
    label_encoder = LabelEncoder()
    df['id'] = label_encoder.fit_transform(df['id'])

    # Features and target variable
    X = df[['humidity', 'temperature', 'rainfall', 'ph', 'id']]
    y = df['K_category']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create and train the Random Forest Classifier model
    rf_classifier = RandomForestClassifier(random_state=42)
    rf_classifier.fit(X_train_scaled, y_train)

    # Encode the input 'id_value'
    id_encoded = label_encoder.transform([id_value])

    # Scale the input values
    input_scaled = scaler.transform(
        [[humidity, temperature, rainfall, ph, id_encoded[0]]])

    # Make predictions
    predicted_K_category = rf_classifier.predict(input_scaled)

    return predicted_K_category[0]


def train_and_predict_P_category(df, humidity, temperature, rainfall, ph, id_value):
    # Encode the categorical 'id' column
    label_encoder = LabelEncoder()
    df['id'] = label_encoder.fit_transform(df['id'])

    # Features and target variable
    X = df[['humidity', 'temperature', 'rainfall', 'ph', 'id']]
    y = df['P_category']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create and train the Random Forest Classifier model
    rf_classifier = RandomForestClassifier(random_state=42)
    rf_classifier.fit(X_train_scaled, y_train)

    # Encode the input 'id_value'
    id_encoded = label_encoder.transform([id_value])

    # Scale the input values
    input_scaled = scaler.transform(
        [[humidity, temperature, rainfall, ph, id_encoded[0]]])

    # Make predictions
    predicted_P_category = rf_classifier.predict(input_scaled)

    return predicted_P_category[0]


def train_evaluate_random_forest(df, N, temperature, humidity, ph, rainfall):
    # Features and target variable
    X = df[['N', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = df['label']

    # Split the dataset into training and testing sets
    X_train1, X_test1, y_train1, y_test1 = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Create and train the RandomForestClassifier model without scaling
    rf_classifier = RandomForestClassifier(random_state=42)
    rf_classifier.fit(X_train1, y_train1)

    input_data = [[N, temperature, humidity, ph, rainfall]]

    # Make predictions without scaling
    predicted_yield = rf_classifier.predict(input_data)

    return predicted_yield[0]


def train_and_predict_N(df, humidity, temperature, rainfall, ph, pid_value):
    # Encode the categorical 'id' column
    label_encoder = LabelEncoder()
    df['id'] = label_encoder.fit_transform(df['id'])

    # Features and target variable
    X = df[['humidity', 'temperature', 'rainfall', 'ph', 'id']]
    y = df['N']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create and train the Random Forest Classifier model
    rf_model1 = RandomForestRegressor(random_state=42)
    rf_model1.fit(X_train_scaled, y_train)

    # Encode the input 'pid_value'
    pid_encoded = label_encoder.transform([pid_value])

    # Scale the input values
    input_scaled = scaler.transform(
        [[humidity, temperature, rainfall, ph, pid_encoded[0]]])

    # Make predictions
    predicted_N = rf_model1.predict(input_scaled)

    return predicted_N[0]
