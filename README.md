# ![Project Image Representation](images/document_image.jpg)

Visit the live project here: [Medical Insurance Project](https://insurance-predict-4eed0585c61b.herokuapp.com/)

## Table of Contents

- [](#)
  - [Table of Contents](#table-of-contents)
  - [Dataset Content](#dataset-content)
  - [Business Case: Predicting Medical Insurance Costs](#business-case-predicting-medical-insurance-costs)
  - [Business Requirements](#business-requirements)
  - [Hypothesis and how to validate](#hypothesis-and-how-to-validate)
  - [The rationale to map the business requirements to the Data Visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
  - [ML Business Case](#ml-business-case)
    - [Predict Medical Insurance Charges](#predict-medical-insurance-charges)
  - [Epics \& User Stories](#epics--user-stories)
    - [Epic: Insights \& Hypothesis Validation](#epic-insights--hypothesis-validation)
    - [Epic: Personalized Insurance Quote Generation](#epic-personalized-insurance-quote-generation)
    - [Epic: Model Development \& Evaluation](#epic-model-development--evaluation)
    - [Epic: Transparency, Monitoring \& Strategic Decision Support](#epic-transparency-monitoring--strategic-decision-support)
  - [Dashboard Design (Streamlit App User Interface)](#dashboard-design-streamlit-app-user-interface)
    - [Page 1: Quick Project Summary](#page-1-quick-project-summary)
    - [Page 2: Project Hypotheses and Validation](#page-2-project-hypotheses-and-validation)
    - [Page 3: Correlation Analysis](#page-3-correlation-analysis)
    - [Page 4: Medical Insurance Charges Prediction](#page-4-medical-insurance-charges-prediction)
    - [Page 5: Model Evaluation and Feature Importance](#page-5-model-evaluation-and-feature-importance)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Important configuration files](#important-configuration-files)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Testing](#testing)
    - [Page 1: Quick Project Summary](#page-1-quick-project-summary-1)
    - [Page 2: Project Hypotheses and Validation](#page-2-project-hypotheses-and-validation-1)
    - [Page 3: Correlation Analysis](#page-3-correlation-analysis-1)
    - [Page 4: Medical Insurance Charges Prediction](#page-4-medical-insurance-charges-prediction-1)
    - [Page 5: Model Evaluation and Feature Importance](#page-5-model-evaluation-and-feature-importance-1)
  - [Validation](#validation)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)

## Dataset Content

This dataset is publicly available on [Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance) and contains information about individuals and their respective medical insurance charges. Each row in the dataset represents a unique customer profile, with various demographic and health-related attributes.

| Variable   | Meaning                                                              | Units                                  |
|------------|----------------------------------------------------------------------|----------------------------------------|
| age        | Age of primary beneficiary                                           | years                                  |
| sex        | insurance contractor gender, female, male                            | male / female                          |
| bmi        | Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9                                                      | kg/m²                                  |
| children   | Number of children covered by health insurance / Number of dependents               | count                                  |
| smoker     | Smoking status of the policyholder                                   | yes / no                               |
| region     | Residential region of the policyholder in the US                     | northeast / southeast / southwest / northwest |
| charges    | Annual medical insurance charges billed by the insurer              | USD                                    |

## Business Case: Predicting Medical Insurance Costs

A growing company that provides health insurance to individuals and families recognizes the need to improve how it determines insurance costs. As the business expands, it becomes increasingly important to calculate premiums based on each customer’s personal information, ensuring prices are both competitive and fair. The company aims to leverage data analytics and machine learning to enhance its pricing strategy, moving away from a one-size-fits-all approach to a more personalized model.

This initiative aligns with the company’s strategic goals of becoming more customer-centric and insight-driven. By enhancing pricing accuracy, the company can build greater trust, strengthen customer relationships, and reduce financial risk while also positioning itself as a modern, transparent leader in the health insurance market.

[Back to top](#table-of-contents)

## Business Requirements

* ### Insights from Data:
  * Analyze historical customer data to uncover the key factors that influence insurance costs. These insights will help guide pricing strategies, ensuring that the company can offer competitive rates while maintaining profitability.

* ### Accurate Cost Prediction:
  * Develop a reliable way to estimate medical insurance costs for new customers using the information they provide such as age, lifestyle habits, and family details. This ensures that each quote reflects the customer’s unique profile.

[Back to top](#table-of-contents)

## Hypothesis and how to validate

To better understand what influences medical insurance costs, we propose the following hypotheses. Each hypothesis will be tested using appropriate analysis techniques to confirm or reject its validity.

| Hypothesis                                                                 | Rationale                                                                 | Validation Method                                                                 |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **H1: Insurance charges increase with age.**                              | Older individuals are more likely to require medical services.           | Analyze the correlation between age and charges; visualize with scatter plots.   |
| **H2: Higher BMI leads to higher insurance costs.**                       | High BMI may indicate health conditions like obesity or heart disease.   | Examine BMI vs. charges using regression analysis or scatter plots.              |
| **H3: Smokers are charged significantly more than non-smokers.**          | Smoking is linked to higher health risks and medical costs.              | Compare average charges between smokers and non-smokers using statistical tests. |
| **H4: Customers with more children tend to have higher costs.**           | More dependents may lead to higher coverage needs and expenses.          | Compare average charges across different numbers of children.                    |
| **H5: Region affects insurance costs.**                                   | Healthcare costs can vary by region due to economic and service factors. | Analyze average charges by region using group comparisons tests.        |

Each validated hypothesis will help the company better understand cost drivers and refine its pricing strategy accordingly.

[Back to top](#table-of-contents)

## The rationale to map the business requirements to the Data Visualizations and ML tasks

* **Business Requirement 1: Insights from Data**
  * We will inspect the dataset to identify key factors influencing insurance costs.
  * We will visualize the relationships between variables to uncover patterns and correlations.
  * We will vizualize feature engineered dataset to understand how the features relate to the target variable (charges).

* **Business Requirement 2: Accurate Cost Prediction**
  * We will develop a machine learning model to predict insurance costs based on customer profiles.
  * We will create a user interface that allows users to input customer data and receive predicted insurance charges.
  * We will evaluate the model's performance and feature importance to ensure transparency and reliability.

[Back to top](#table-of-contents)

## ML Business Case

### Predict Medical Insurance Charges

**Regression Model:**

* We wanted a model that predicts the medical insurance charges based on customer profiles. The model aims to provide accurate estimates of insurance costs, helping the company set competitive and fair premiums. The target variable is the annual medical insurance charges
  * Target Variable: `charges`(float)
  * Features: `age`, `sex`, `bmi`, `children`, `smoker`, `region`
  * Best model: `XGBoost Regressor`
  
* The ideal outcome is the ability to input customer data and receive a predicted insurance charge, which can be used to inform pricing strategies.
* **Model Success Metrics:**
  * Achieve at least 80% accuracy in predicting insurance charges, minimizing the errors of overcharged or low charges.
* **Performance Metrics:**
  * R² Score: The model explains 89.1% of the variance in insurance charges on training data and 89.8% on test data. This indicates a strong and generalizable fit.
  * MAE (Mean Absolute Error): On average, predictions are within ~2,100–2,400 units of the actual charges.
  * MSE & RMSE: Low values and minimal difference between training and testing metrics show the model is not overfitting and is stable.
  * Balanced RMSE: Consistency between training and test RMSE means the model performs reliably across unseen data.

[Back to top](#table-of-contents)

## Epics & User Stories

### Epic: Insights & Hypothesis Validation

- **User Story**: As a data scientist, I want to analyze correlations between features like age, BMI, and charges, So that I can discover the main factors influencing insurance costs.
- **User Story**: As an insurance provider, I want to validate that factors like smoking status or region significantly impact pricing, So that I can make evidence-based pricing policy decisions.
- **User Story**: As a user, I want to see how changing certain lifestyle choices affects my quote, So that I understand how to potentially lower my premiums.

### Epic: Personalized Insurance Quote Generation

- **User Story**: As a user, I want to input my personal details, So that I can receive a personalized insurance cost estimate.
- **User Story**: As a data scientist, I want to deploy a predictive model that runs on real-time inputs, So that users can get instant and reliable insurance cost estimates.

### Epic: Model Development & Evaluation

- **User Story**: As a data scientist, I want to train a regression model using historical customer data, So that we can predict future insurance costs with high accuracy.
- **User Story**: As a data scientist, I want to evaluate the model using R², MAE, and RMSE, So that I can ensure it generalizes well to new data.
- **User Story**: As an insurance provider, I want to reduce the risk of over or under charge customers, So that we maintain trust while managing financial risk.

### Epic: Transparency, Monitoring & Strategic Decision Support

- **User Story**: As a data scientist, I want to view feature importance rankings, So that I can explain to stakeholders why the model makes specific predictions.
- **User Story**: As a user, I want the ability to change certain inputs (like smoking status or BMI) and see how it affects the premium, So that I can explore how lifestyle changes could lower my insurance cost.

[Back to top](#table-of-contents)

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary

* Quick project summary
  * Project Summary
  * Project Terms & Jargon
  * Dataset Overview
  * State Business Requirements

### Page 2: Project Hypotheses and Validation

* We report on whether the 5 hypotheses we posed earlier are correct
* Checkbox to display the corresponding plot for each hypothesis
  
### Page 3: Correlation Analysis

* Correlation matrix to visualize relationships between variables before feature engineering
* Correlation conclusions and considarations
* Show correlation matrix heatmap of the feature enginereed dataset
* Conclusions of correlated features after feature engineering

### Page 4: Medical Insurance Charges Prediction

* State business requirement 2
* Set of widget inputs related to the custumer profile. Each set of inputs is related to a given ML task to predict custumers charges.
* "Run predictive analysis" button that processes the custumer data through our ML pipelines and predicts the insurance charges.

### Page 5: Model Evaluation and Feature Importance

* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance
* Pipeline performance

[Back to top](#table-of-contents)

## Unfixed Bugs

* At the time of writing, there are no unfixed bugs within the project.

[Back to top](#table-of-contents)

## Deployment

### Heroku

* The App live link is: https://insurance-predict-4eed0585c61b.herokuapp.com/
* Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.

[Back to top](#table-of-contents)

## Important configuration files

* `setup.sh` should contain the following
```
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

* `Procfile` should contain
```
web: sh setup.sh && streamlit run app.py
```

[Back to top](#table-of-contents)

## Main Data Analysis and Machine Learning Libraries

* [Pandas](https://pandas.pydata.org/docs/index.html) - Data analysis and manipulation tool
* [Numpy](https://numpy.org/doc/stable/index.html) - The fundamental package for scientific computing with Python
* [Matplotlib](https://matplotlib.org/) - Comprehensive library for creating static, animated and interactive visualisations
* [Seaborn](https://seaborn.pydata.org/) - Data visualisation library for drawing attractive and informative statistical graphics
* [Feature-engine](https://feature-engine.trainindata.com/en/latest/) - Transformers to engineer and select features for machine learning models
* [scikit-learn](https://scikit-learn.org/stable/) - Machine learning library for training the ML model
* [XGBoost](https://xgboost.readthedocs.io/en/stable/) - Optimised distributed gradient boosting library
* [Joblib](https://joblib.readthedocs.io/en/stable/) - Tool for dumping pipeline to pickle files
* [Kaggle](https://pypi.org/project/kaggle/) - Kaggle API functionalit
* [Streamlit](https://streamlit.io/) - Build the web app.

[Back to top](#table-of-contents)

## Testing

The following table outlines manual tests performed to ensure that all five dashboard pages in the Streamlit application function as expected.

### Page 1: Quick Project Summary

| Feature | Action | Result |
|---------|--------|-----------------|
| Display of project overview and terms | Open the page and verify presence of project summary, dataset description, and business requirements | All content is rendered correctly without errors |
| Navigation | Click the page tab or use sidebar to access | User is redirected to the Quick Project Summary |

### Page 2: Project Hypotheses and Validation

| Feature | Action | Result |
|---------|--------|-----------------|
| Hypotheses checkboxes | Toggle checkboxes for each hypothesis | Corresponding plots or visual insights appear/disappear based on checkbox status |
| Hypotheses plots | Select each hypothesis one by one | Each plot matches the data claim and renders correctly |

### Page 3: Correlation Analysis

| Feature | Action | Result |
|---------|--------|-----------------|
| Initial correlation matrix | Load page and check if the pre-feature engineering heatmap appears | Correlation heatmap is displayed properly |
| Post-feature engineering matrix | Scroll or toggle to display second heatmap | Engineered correlation heatmap renders with updated variables |
| Correlation insights | Review written interpretation below matrix | Conclusions appear correctly and align with visual data |

### Page 4: Medical Insurance Charges Prediction

| Feature | Action | Result |
|---------|--------|-----------------|
| Input widgets for customer data | Fill in values for age, BMI, children, sex, region, and smoking status | Inputs are accepted and validated without breaking the form |
| Run Prediction button | Click the prediction button after entering data | A predicted insurance charge is displayed below the button |

### Page 5: Model Evaluation and Feature Importance

| Feature | Action | Result |
|---------|--------|-----------------|
| Feature importance chart | View bar chart or visualization of feature impact | The chart is rendered and shows logical importance rankings |
| Pipeline steps display | Review pipeline architecture or list | Model steps are shown in sequence and make sense |
| Model performance metrics | Scroll to view R², MAE, RMSE, etc. | All metrics are clearly displayed and values match training results |

[Back to top](#table-of-contents)

## Validation

All code within the `app_pages` and `src` directories has been validated for PEP8 compliance using Code Institute’s PEP8 Linter.

- A few files triggered warnings related to line length (long function parameters or URL links), which are not easily breakable without reducing code readability.
- These warnings do not affect the functionality or performance of the application in any way.

[Back to top](#table-of-contents)

## Credits

### Content

- The project concept was inspired by a publicly available dataset on Kaggle.
- Several helper functions and custom class snippets used in this project were provided by Code Institute, primarily adapted from their Predictive Analytics module.

### Media

- Image for README file was taken from [FreePik](https://www.freepik.com/)

[Back to top](#table-of-contents)
