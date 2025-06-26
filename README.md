# ![Project Image Representation](images/document_image.jpg)

## Dataset Content

This dataset is publicly available on Kaggle and contains information about individuals and their respective medical insurance charges. Each row in the dataset represents a unique customer profile, with various demographic and health-related attributes.

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

* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks

## ML Business Case

* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course

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

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people who provided support through this project.

