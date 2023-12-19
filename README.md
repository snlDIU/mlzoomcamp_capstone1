# Machine Learning Capstone Project

## Introduction

This notebook is part of the capstone project for the Machine Learning Zoomcamp course Cohort 2023. The objective of this project is to develop a machine learning algorithm to predict the math scores of high school students in the United States based on various features. The prediction of math scores can provide insights into the factors influencing academic performance.

## Problem Description

The dataset contains information on marks secured by students in high school. The goal is to create a machine learning model that predicts the math scores of students. By analyzing the features influencing math results, we aim to gain a deeper understanding of the factors contributing to academic success.

## Dataset Description

The dataset used in this project was obtained from Kaggle and can be found at [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams). It includes various features such as gender, ethnicity, parental education, lunch type, and test preparation course completion. The target variable is the math score.

## Project Description

In this project, we explored various machine learning models to predict math scores. The following models were trained and evaluated:

- Linear Regression
- Lasso
- Ridge
- K-Neighbors Regressor
- Decision Tree Regressor
- Random Forest Regressor
- XGBRegressor
- CatBoosting Regressor
- AdaBoost Regressor

A set of metrics, including Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared, were used for model evaluation. The data preparation, exploratory data analysis (EDA), and model selection process are documented in the Jupyter Notebook file `notebook_capstone1.ipynb`.

## Repository Structure

- **README.md**: The current file.
- **notebook_capstone1.ipynb**: Jupyter Notebook containing data preparation, EDA, and model selection.
- **requirements.txt**: Text file listing all the required packages.
- **app.py (incomplete)**: Python script for the future deployment of the model using Flask.

## Getting Started

To replicate the environment used in this project, create a virtual environment using the following commands:

```bash
conda create -p venv python==3.8 -y
conda activate venv
pip install -r requirements.txt
```

## Future Work

The project outlines potential future work, including:

- Model deployment using Flask.
- Building a Docker container for easier deployment and scalability.

## Conclusion

As a newcomer to machine learning, I acknowledge that this project is a starting point. I understand that there is more to explore and learn in the field of ML. I look forward to updating and expanding on this project in the future.

Thank you for reviewing my work.

*Another Machine Learning Enthusiast*