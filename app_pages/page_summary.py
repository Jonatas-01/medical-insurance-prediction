import streamlit as st
from src.data_management import load_data

def page_summary():

      st.write("### Project Summary")
      st.info(
            f"A growing company that provides health insurance to individuals and families recognizes the need to improve how it determines insurance costs. "
            f"As the business expands, it becomes increasingly important to calculate premiums based on each customer’s personal information, ensuring prices are "
            f"both competitive and fair. Moving away from generalized pricing models, the company aims to deliver more accurate and personalized "
            f"cost estimates that better reflect individual risk profiles."
            f"\n\nThis initiative aligns with the company’s strategic goals of becoming more customer-centric and insight-driven. "
            f"By enhancing pricing accuracy, the company can build greater trust, strengthen customer relationships, and reduce financial "
            f"risk while also positioning itself as a modern, transparent leader in the health insurance market."
            )

      st.write("### Key Features and Concepts")
      st.info(
            """
            - **Insurance Charges**: The total medical cost billed to a customer.
            - **BMI (Body Mass Index)**: A person’s weight-to-height ratio, used to classify health risk.
            - **Smoker Status**: Whether the insured person is a smoker — one of the strongest predictors of cost.
            - **Region**: The geographical area of the insured person, which can influence healthcare costs.
            - **Age**: The age of the insured person.
            - **Risk Factors**: Variables that can increase the likelihood of higher medical costs, such as smoking and BMI.
            - **Feature Engineering**: The process of creating or transforming input variables to improve model performance.
            - **Model Pipeline**: A structured sequence of preprocessing steps and a model, wrapped into a single object for deployment.
            - **Grid Search**: An approach to find the best model parameters using exhaustive testing with cross-validation.
            """)

      st.write("### Data Overview")
      st.dataframe(load_data())
      
      st.write('For explanation of variable meanings and further, please check the [Project README file](https://github.com/Jonatas-01/medical-insurance-prediction/tree/main)')

      # Business Requirements
      st.write("### Business Requirements")
      st.success(
            " The project has 2 business requirements:\n\n"
            " 1 - Analyze historical customer data to uncover the key factors that influence insurance costs. "
            "These insights will help guide pricing strategies, identify customer segments with higher risk, and support data-driven business decisions.\n\n"
            " 2 - Develop a reliable way to estimate medical insurance costs for new customers using the information they provide such as age, " 
            "lifestyle habits, and family details. This ensures that each quote reflects the customers unique profile."
      )