import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from src.data_management import load_data, load_feature_engineering_data

def app_correlation():
    st.title("Correlation Analysis")
    st.info("This section provides correlation analysis between all features in the dataset to anwser **Business Requirement 1**. "
            "The correlation method used is Pearson correlation coefficient, which measures the linear relationship between two variables.")

    # Encode categorical variables
    df = load_data()
    df['sex'] = df['sex'].map({'male': 1, 'female': 0})
    df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})
    df['region'] = df['region'].astype('category').cat.codes

    # Compute correlation
    corr_matrix = df.corr()

    # Display correlation matrix
    st.subheader("Correlation Matrix Heatmap")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', center=0, ax=ax)
    st.pyplot(fig)

    # Show raw matrix as a table (optional)
    with st.expander("Show Raw Correlation Matrix"):
        st.dataframe(corr_matrix)

    # Analysis conclusions
    st.subheader("Correlation Analysis")
    st.success("""
    - **Age vs Charges**: Moderate positive correlation – insurance charges tend to increase with age.
    - **BMI vs Charges**: Weak correlation – BMI alone is not a strong indicator.
    - **Children vs Charges**: Very weak correlation.
    
    These are the correlations before feature engineering.
    After feature engineering, the model will be able to capture more complex relationships.
    """)

    # Load processed dataset
    st.title("Correlation Analysis on Feature Engineered Data")
    st.write("This page analyzes the correlation between the engineered features and the insurance charges.")

    # Load processed dataset
    df = load_feature_engineering_data()  # custom function to load the transformed dataset
    df_corr = df.select_dtypes(include=['int64', 'float64'])  # numeric only

    # Compute correlation
    corr_matrix = df_corr.corr()
    charges_corr = corr_matrix["charges"].sort_values(ascending=False).drop("charges")

    # Plot correlation heatmap
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", center=0)
    st.pyplot(fig)

    # Display correlation to charges
    st.subheader("Feature Correlation with Charges")
    st.dataframe(charges_corr.to_frame(name="Correlation with Charges"))

    # Generate conclusions
    st.subheader("Conclusions")
    st.markdown(generate_conclusions(charges_corr))


def generate_conclusions(corr_series, threshold_high=0.4, threshold_moderate=0.2):
    strong = corr_series[abs(corr_series) >= threshold_high]
    moderate = corr_series[(abs(corr_series) < threshold_high) & (abs(corr_series) >= threshold_moderate)]
    weak = corr_series[abs(corr_series) < threshold_moderate]

    conclusion = ""

    if not strong.empty:
        conclusion += "**Strongly correlated features with charges:**\n"
        for feat, val in strong.items():
            conclusion += f"- `{feat}` (corr = {val:.2f})\n"
    else:
        conclusion += "No strongly correlated features found.\n"

    if not moderate.empty:
        conclusion += "\n**Moderately correlated features:**\n"
        for feat, val in moderate.items():
            conclusion += f"- `{feat}` (corr = {val:.2f})\n"

    if not weak.empty:
        conclusion += "\n**Weak or no correlation features:**\n"
        for feat, val in weak.items():
            conclusion += f"- `{feat}` (corr = {val:.2f})\n"

    return conclusion

