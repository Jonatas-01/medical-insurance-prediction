import streamlit as st
from app_pages.multi_pages import MultiPage

# Import all pages
from app_pages.page_summary import page_summary
from app_pages.page_hypotheses import app_hypotheses
from app_pages.page_correlation import app_correlation
from app_pages.page_prediction import app_predict
from app_pages.page_performance import app_performance

# Create an instance of the MultiPage class
app = MultiPage(app_name="Medical Insurance Cost Prediction")

# Set the page configuration
app.app_page("Project Summary", page_summary)
app.app_page("Project Hypotheses and Validations", app_hypotheses)
app.app_page("Correlation Analysis", app_correlation)
app.app_page("Predict Insurance Charges", app_predict)
app.app_page("Model Performance", app_performance)

# Run the app
app.run()