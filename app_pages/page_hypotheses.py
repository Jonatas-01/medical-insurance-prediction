import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import load_data

sns.set_style("whitegrid")

def app_hypotheses():
    df = load_data()

    st.title("Hypotheses and Validations")

    # Hypotheses Section
    st.write("### Hypotheses 1")
    st.warning('We hypothesize that insurance charges increase with age.')
    st.success(' * According to correlataion analysis, there is a strong positive correlation between age and insurance charges.'
               ' We see that as age increases, the insurance charges also tend to increase.\n'
               ' * The scatter plot below shows the distribution of insurance charges with respect to age, confirming our hypothesis.')

    if st.checkbox("Inspect Age-Charges relation"):
        show_scatter_plot(df, 'age')

    st.write("### Hypotheses 2")
    st.warning('We hypothesize that insurance charges increase with BMI.')
    st.success(' * According to correlataion analysis, there is a moderate positive correlation between BMI and insurance charges.'
                ' We see that as BMI increases, the insurance charges also tend to increase.\n'
                ' * The scatter plot below shows the distribution of insurance charges with respect to BMI, confirming our hypothesis.')

    if st.checkbox("Inspect BMI-Charges relation"):
        show_scatter_plot(df, 'bmi')

    st.write("### Hypotheses 3")
    st.warning('We hypothesize that insurance charges are higher for smokers than non-smokers.')
    st.success(' * According to correlataion analysis, there is a strong positive correlation between avarage charges for smoking status and insurance charges.'
                ' We see that smokers tend to have significantly higher insurance charges compared to non-smokers.\n'
                ' * The bar plot below shows the average insurance charges for smokers and non-smokers, confirming our hypothesis.')

    if st.checkbox("Inspect Smoker-Charges relation"):
        show_bar_plot(df, 'smoker')

    st.write("### Hypotheses 4")
    st.warning('We hypothesize that insurance charges increase with the number of children.')
    st.success(' * According to correlataion analysis, there is a weak positive correlation between the avarage charges number of children and insurance charges.'
                ' We see that as the number of children increases, the insurance charges also tend to increase, but the effect is not very strong.\n'
                ' * The bar plot below shows the average insurance charges with respect to the number of children, confirming our hypothesis.')

    if st.checkbox("Inspect Children-Charges relation"):
        show_bar_plot(df, 'children')

    st.write("### Hypotheses 5")
    st.warning('We hypothesize that insurance charges vary by region.')
    st.success(' * According to correlataion analysis, there is a weak variation in insurance charges across the avarage charges of different regions.'
                ' We see that the average insurance charges differ significantly by region.\n'
                ' * The bar plot below shows the average insurance charges for each region, confirming our hypothesis.')

    if st.checkbox("Inspect Region-Charges relation"):
        show_bar_plot(df, 'region')


def show_bar_plot(df, x_col):
    charges = df['charges'].groupby(df[x_col]).mean()
    f, ax = plt.subplots(1,1, figsize=(10, 8))
    ax = sns.barplot(x=charges.index, y=charges.values, palette='viridis')
    ax.set_title(f'{x_col} vs charges')
    ax.set_xlabel(x_col)
    ax.set_ylabel('charges')
    st.pyplot(f)

def show_scatter_plot(df, x_col):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x_col, y='charges', alpha=0.5)
    plt.title(f'Distribution of Charges by {x_col.capitalize()}')
    plt.xlabel(x_col.capitalize())
    plt.ylabel('Charges')
    st.pyplot(plt.gcf())