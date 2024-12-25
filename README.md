# Premium Insurance Prediction with Django  

## Overview  
This project is a full-stack data science application designed to predict insurance premiums. The project integrates data preprocessing, machine learning model development, and a web-based interface built using Django. By analyzing historical data, users can obtain accurate insurance premium predictions through an interactive and user-friendly application.  

---

## Features  
- Preprocessed datasets sourced from Kaggle for better model accuracy.  
- Comparison of machine learning models like Linear Regression, Random Forest, and others to select the best-performing model.  
- Django-based web application for real-time predictions.  
- Clean, interactive frontend for user input and results display.  
- Scalable and customizable architecture for various use cases.  

---

## Workflow  

### 1. Dataset  
- Datasets are sourced from **[Kaggle](https://www.kaggle.com/)**.  
- Includes data related to insurance premium determinants (e.g., age, income, health metrics, etc.).  

### 2. Data Preprocessing  
- Performed in **Jupyter Notebook** for:  
  - Handling missing values.  
  - Encoding categorical data.  
  - Scaling numerical features.  
  - Splitting the dataset into training and testing sets.  

### 3. Model Training and Evaluation  
- Tested various machine learning models, including:  
  - **Linear Regression**  
  - **Random Forest Regressor**  
  - Other regression models.  
- Selected the best-fit model based on metrics like RMSE and R².  

### 4. Web Application (Django)  
- Built a full-stack Django application:  
  - **Backend:** Implements the selected machine learning model for predictions.  
  - **Frontend:** Accepts user input for prediction and displays results in a clean interface.  

---

## Installation  

### Prerequisites  
Ensure the following tools are installed:  
- Python 3.8+  
- pip  
- virtualenv  

### Steps  
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/yourusername/premium-insurance-prediction.git
   cd premium-insurance-prediction

2. **Set up a Virtual Environment**:
   ```virtualenv env  
    source env/bin/activate  # For Linux/Mac
    env\Scripts\activate     # For Windows

 3. **Run the Application**:
    ```python manage.py runserver
    Open http://127.0.0.1:8000/ in your browser to access the app.
  

   

   
