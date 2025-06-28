# ![Project Image Representation](images/document_image.jpg)

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

## Business Requirements

* ### Insights from Data:
  * Analyze historical customer data to uncover the key factors that influence insurance costs. These insights will help guide pricing strategies, ensuring that the company can offer competitive rates while maintaining profitability.

* ### Accurate Cost Prediction:
  * Develop a reliable way to estimate medical insurance costs for new customers using the information they provide such as age, lifestyle habits, and family details. This ensures that each quote reflects the customer’s unique profile.

## Hypothesis and how to validate?

To better understand what influences medical insurance costs, we propose the following hypotheses. Each hypothesis will be tested using appropriate analysis techniques to confirm or reject its validity.

| Hypothesis                                                                 | Rationale                                                                 | Validation Method                                                                 |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **H1: Insurance charges increase with age.**                              | Older individuals are more likely to require medical services.           | Analyze the correlation between age and charges; visualize with scatter plots.   |
| **H2: Higher BMI leads to higher insurance costs.**                       | High BMI may indicate health conditions like obesity or heart disease.   | Examine BMI vs. charges using regression analysis or scatter plots.              |
| **H3: Smokers are charged significantly more than non-smokers.**          | Smoking is linked to higher health risks and medical costs.              | Compare average charges between smokers and non-smokers using statistical tests. |
| **H4: Customers with more children tend to have higher costs.**           | More dependents may lead to higher coverage needs and expenses.          | Compare average charges across different numbers of children.                    |
| **H5: Region affects insurance costs.**                                   | Healthcare costs can vary by region due to economic and service factors. | Analyze average charges by region using group comparisons tests.        |

Each validated hypothesis will help the company better understand cost drivers and refine its pricing strategy accordingly.

## The rationale to map the business requirements to the Data Visualizations and ML tasks

* **Business Requirement 1: Insights from Data**
  * We will inspect the dataset to identify key factors influencing insurance costs.
  * We will visualize the relationships between variables to uncover patterns and correlations.
  * We will vizualize feature engineered dataset to understand how the features relate to the target variable (charges).

* **Business Requirement 2: Accurate Cost Prediction**
  * We will develop a machine learning model to predict insurance costs based on customer profiles.
  * We will create a user interface that allows users to input customer data and receive predicted insurance charges.
  * We will evaluate the model's performance and feature importance to ensure transparency and reliability.

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

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

* The App live link is: https://insurance-predict-4eed0585c61b.herokuapp.com/
* Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.

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

## Credits

### Content

* The idea was taken from Kaggle, using one of their DataSet.
* Helper functions and custom classes snippets were used in this project were provided by Code Institute. These are mainly adapted from the predictive analytics module.

### Media

* Image for README file was taken from [FreePik](https://www.freepik.com/)