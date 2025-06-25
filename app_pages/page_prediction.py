import streamlit as st
import pandas as pd
from src.data_management import load_pkl_file, load_data
from src.machine_learning.predict_insurance import predict_insurance

def app_predict():

    # Load pipelines and features
    path = 'outputs/ml_pipelines/v1/'
    insurance_pipe_de_fe = load_pkl_file(
        f"{path}/pipeline_data_cleaning_feat_eng.pkl")
    insurance_pipe_model = load_pkl_file(
        f"{path}/clf_pipeline_model.pkl")
    insurance_features = (pd.read_csv(
        f"{path}/X_train.csv")
        .columns
        .tolist()
    )

    # Page title
    st.title("Predict Insurance Charges")
    st.write("Enter customer information to estimate their medical insurance cost.")

    # Generate Live Data
    X_live = DrawInputsWidgets()

    st.write(X_live)

    if st.button("Run Predictive Analysis"):
        insurance_prediction = predict_insurance(
            X_live, insurance_features, insurance_pipe_de_fe,
            insurance_pipe_model)
    
def DrawInputsWidgets():
    """
    Draws input widgets for user to enter customer information.
    
    Returns:
    - X_live: DataFrame containing the input features for prediction.
    """
    
    # load data
    df = load_data()

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type
    # (numerical or categorical) and set initial values
    with col1:
        feature = "age"
        st_widget = st.number_input(
            label=feature,
            value=25,
            min_value=0,
            max_value=100,
        )
    X_live[feature] = st_widget

    with col2:
        feature = "sex"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique(),
        )
    X_live[feature] = st_widget

    with col3:
        feature = "bmi"
        st_widget = st.number_input(
            label=feature,
            value=df[feature].median(),
            min_value= 16.1,
            max_value= 55.1,
            step= 0.1,
            help="Body Mass Index (BMI) is a measure of body fat based on height and weight."
        )
    X_live[feature] = st_widget

    with col4:
        feature = "children"
        st_widget = st.number_input(
            label=feature,
            value= 0,
            min_value=0,
            max_value=5,
            step=1
        )
    X_live[feature] = st_widget

    with col5:
        feature = "smoker"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique(),
        )
    X_live[feature] = st_widget

    with col6:
        feature = "region"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique(),
        )
    X_live[feature] = st_widget

    return X_live