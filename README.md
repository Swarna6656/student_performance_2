# student_performance

# Student Performance Prediction Using Machine Learning

## Project Overview
This project predicts student academic performance using Machine Learning techniques. The system analyzes various academic and lifestyle-related factors such as study hours, previous scores, sleep hours, extracurricular activities, and practice papers to estimate the student’s overall performance index.

The project is designed to understand how different habits and academic activities influence student performance and helps in building a predictive model using regression techniques.

---

# Project Objective
The main objective of this project is to:
- Analyze the factors affecting student academic performance
- Build a Machine Learning model for prediction
- Predict student performance using educational and lifestyle data
- Understand the relationship between study patterns and academic success

---

# Dataset Information

Dataset Name:  
**Student_Performance.csv**

The dataset contains information related to students’ academic activities and daily habits.

## Features in the Dataset

| Feature Name | Description |
|---|---|
| Hours Studied | Number of hours spent studying daily |
| Previous Scores | Scores obtained in earlier examinations |
| Extracurricular Activities | Participation in extracurricular activities |
| Sleep Hours | Average number of sleeping hours per day |
| Sample Question Papers Practiced | Number of practice papers completed |
| Performance Index | Overall student performance score (Target Variable) |

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- Pickle

---

# Machine Learning Workflow

## 1. Data Collection
The dataset is collected and loaded into the project for analysis and prediction. It contains academic and lifestyle-related information of students.

---

## 2. Data Preprocessing
Data preprocessing is an important step in Machine Learning. In this stage:
- Categorical values are converted into numerical values
- Unnecessary data is removed
- Input features and target variables are separated
- Data is prepared for model training

The extracurricular activities column contains Yes/No values which are converted into numerical form for model understanding.

---

## 3. Exploratory Data Analysis (EDA)
EDA is performed to understand the dataset and identify relationships between variables.

Different visualizations and statistical methods are used to:
- Analyze correlations between features
- Understand data distribution
- Identify important factors affecting performance
- Detect patterns and trends in the dataset

Visualization techniques include:
- Heatmaps
- Histograms
- Scatter plots
- Correlation analysis

---

# Model Development

## Algorithm Used
### Multiple Linear Regression

Multiple Linear Regression is used to predict the student performance index based on multiple input features.

The model learns relationships between:
- Study habits
- Academic history
- Lifestyle factors
and the final performance score.

---

# Model Training
The dataset is divided into:
- Training data
- Testing data

The training data is used to train the Machine Learning model, while the testing data is used to evaluate model performance.

During training, the model learns patterns and relationships from the dataset.

---

# Model Prediction
After training, the model predicts student performance using unseen data. Predictions are generated based on user input values such as study hours, previous scores, and sleep hours.

---

# Model Evaluation
The model performance is evaluated using standard regression evaluation metrics.

## Mean Squared Error (MSE)
MSE measures the average prediction error of the model.

- Lower MSE indicates better model performance.

## R-Squared Score
R-Squared measures how well the model explains the relationship between input features and the target variable.

- Values closer to 1 indicate better prediction accuracy.

---

# Model Saving
The trained model is saved so that it can be reused later without retraining. This improves efficiency and allows deployment of the prediction system.

---

# User Prediction System
The project includes a prediction system where users can provide input values such as:
- Study hours
- Previous scores
- Sleep hours
- Practice papers

The model then predicts the expected student performance index.

---

# Project Structure

| Folder/File | Description |
|---|---|
| dataset | Contains the dataset file |
| notebook | Jupyter Notebook for analysis and training |
| models | Stores trained Machine Learning models |
| templates | HTML files for frontend UI |
| app.py | Main Flask application |
| requirements.txt | Required Python libraries |
| README.md | Project documentation |

---

# Installation
Required libraries are installed using the requirements file. The project can then be executed using the Flask application.

---

# Future Enhancements

Future improvements for this project include:
- Adding advanced Machine Learning algorithms
- Improving prediction accuracy
- Enhancing frontend design
- Deploying the application online
- Adding real-time student analytics
- Generating student performance reports

---

# Learning Outcomes
This project helps in understanding:
- Data preprocessing techniques
- Exploratory Data Analysis (EDA)
- Regression algorithms
- Model evaluation methods
- Machine Learning workflow
- Model deployment concepts

---

# Conclusion
This project demonstrates how Machine Learning can be applied to predict student academic performance using educational and lifestyle-related factors.

The project provides practical knowledge in:
- Data analysis
- Machine Learning
- Prediction systems
- Python programming
- Model deployment

It is a beginner-friendly project that helps in understanding the complete Machine Learning pipeline from data collection to prediction.

---

# Author

**Swarna**

Machine Learning Enthusiast | Python Developer | Aspiring Data Analyst

