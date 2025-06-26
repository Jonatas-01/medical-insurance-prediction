import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from src.data_management import load_pkl_file, load_data

def app_performance():
    # Load data
    path = 'outputs/ml_pipelines/v1/'
    insurance_pipe_de_fe = load_pkl_file(
        f"{path}/pipeline_data_cleaning_feat_eng.pkl")
    insurance_pipe_model = load_pkl_file(
        f"{path}/clf_pipeline_model.pkl")
    
    feat_importances_img = plt.imread(f"{path}/feature_importance_xgb.png")
    feat_importances_df = pd.read_csv(f"{path}/feature_importance_xgb.csv")

    plot_actual_vs_predicted = plt.imread(f"{path}/plot_actual_predicted.png")

    X_train = pd.read_csv(f"{path}/X_train.csv")
    X_test = pd.read_csv(f"{path}/X_test.csv")
    y_train = pd.read_csv(f"{path}/y_train.csv")
    y_test = pd.read_csv(f"{path}/y_test.csv")

    st.write("## ML Pipeline: Predict Charges")

    st.info(f"The goal was to create a machine learning pipeline that predicts insurance charges based on customer information,"
            f"such as age, lifestyle habits, and family details. The model performance meets the business requirements by providing"
            f" a reliable way to estimate medical insurance costs, with the accuracy of more than 80% on training and test."
            )
    st.write("---")

    # Pipelines
    st.write("### There are 2 ML Pipelines arranged in series:")

    st.write(f"* The first pipeline is responsible for data cleaning and\
             feature engineering.\n")
    st.write(insurance_pipe_de_fe)

    st.write(f"* The second pipeline is responsible for the model training and prediction.\n")
    st.write(insurance_pipe_model)
    st.write("---")

    # Feature Importance
    st.write("### Feature Importance")
    st.write(f"* The most important features used for training the model were\
             as follows:\n")
    st.write(feat_importances_df)
    st.image(feat_importances_img, caption="Feature Importance Plot")
    st.write("---")

    # Model Performance
    st.write("### Model Performance")
    st.success("The model achieved an accuracy close to 90% on both training and test datasets, " \
    "that meets the business requirements for accurate cost prediction.")
    st.write("* **Algorithm:** XGBoost Regressor")
    st.write("* **Hyperparameter Tunning:**  Performed via GridSearchCV with cross-validation.")

    st.subheader("Model Evaluation Summary")

    eval_data = {
        "Dataset": ["Train", "Test"],
        "R² Score": [0.891, 0.898],
        "MAE": [2148.08, 2448.13],
        "MSE": [15585545, 16296948],
        "RMSE": [3947.85, 4036.95]
    }

    st.image(plot_actual_vs_predicted, caption="Actual vs Predicted Charges Plot")

    df_eval = pd.DataFrame(eval_data)
    st.dataframe(df_eval, use_container_width=True)

    # Interpretations
    st.subheader("Interpretations")

    st.markdown("""
    - **R² Score**: The model explains **89.1%** of the variance in insurance charges on training data and **89.8%** on test data. This indicates a strong and generalizable fit.
    - **MAE (Mean Absolute Error)**: On average, predictions are within **~2,100–2,400 units** of the actual charges.
    - **MSE & RMSE**: Low values and minimal difference between training and testing metrics show the model is **not overfitting** and is **stable**.
    - **Balanced RMSE**: Consistency between training and test RMSE means the model performs reliably across unseen data.
    """)

    # Conclusion
    st.subheader("Conclusion")

    st.success("""
    The `XGBRegressor` model demonstrates good predictive power:

    - It accurately models the relationship between customer profiles and insurance charges.
    - Performance metrics indicate a balanced model that is ready for deployment.
    - This model is a strong candidate for integration into pricing tools or customer risk assessments.
    """)