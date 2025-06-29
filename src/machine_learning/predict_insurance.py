import streamlit as st


def predict_insurance(X_live, insurance_features, insurance_pipe_dc_fe, insurance_pipe_model):
    """
    Predicts insurance charges based on the input features.

    Parameters:
    - X_live: DataFrame containing the input features for prediction.
    - insurance_features: List of feature names used in the model.
    - insurance_pipe_dc_fe: Data cleaning and feature engineering pipeline.
    - insurance_pipe_model: Trained machine learning model pipeline.

    Returns:
    - insurance_prediction: Predicted insurance charges.
    """

    # from live data, subset features related to this pipeline
    X_live_insurance = X_live.filter(insurance_features)

    # Apply data cleaning and feature engineering
    X_live_insurance_dc_fe = insurance_pipe_dc_fe.transform(X_live_insurance)

    # Make predictions using the trained model
    insurance_prediction = insurance_pipe_model.predict(X_live_insurance_dc_fe)

    # Display the prediction result
    st.success(f"Predicted Insurance Charges: ${insurance_prediction[0]:,.2f}")

    return insurance_prediction
