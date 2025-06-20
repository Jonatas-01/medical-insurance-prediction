import streamlit as st
from app_pages.multi_pages import MultiPage

# Import all pages
from app_pages.page_summary import page_summary
from app_pages.page_hypotheses import app_hypotheses
from app_pages.page_correlation import app_correlation

# Create an instance of the MultiPage class
app = MultiPage(app_name="Medical Insurance Cost Prediction")

# Set the page configuration
app.app_page("Project Summary", page_summary)
app.app_page("Project Hypotheses and Validations", app_hypotheses)
app.app_page("Correlation Analysis", app_correlation)

# Run the app
app.run()