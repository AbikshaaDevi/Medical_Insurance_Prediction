# Medical Insurance Prediction

This repository contains a **Medical Insurance Prediction** project that applies machine learning techniques to predict individual medical insurance charges based on demographic and lifestyle factors such as age, gender, BMI, smoking habits, and region.

## Project Overview
Healthcare costs vary greatly depending on personal and lifestyle attributes.  
The objective of this project is to predict medical insurance expenses for individuals, which can help both insurers and policyholders understand cost drivers and make informed decisions.  
By analyzing patient data, this project identifies key features that influence insurance costs and builds predictive models to estimate charges.

## Features
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA) and visualization of insurance factors
- Feature engineering (encoding categorical variables, scaling numeric data)
- Model training using:
  - Linear Regression
  - Decision Trees & Random Forest
  - Gradient Boosting (XGBoost, LightGBM)
- Model evaluation using RMSE, MAE, and R² score

## Tech Stack
- **Python**
- **Pandas, NumPy, Matplotlib, Seaborn**
- **Scikit-learn, XGBoost, LightGBM**
- **Jupyter Notebook**

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AbikshaaDevi/Medical_Insurance_Prediction.git
   cd Medical_Insurance_Prediction
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Launch Jupyter notebooks for EDA and model training:
   ```bash
   jupyter notebook
   ```
2. Experiment with different models and tune hyperparameters for better performance.

## Dataset
- The dataset includes demographic and lifestyle information such as age, sex, BMI, number of children, smoking status, region, and medical charges.  
- Possible source: [Kaggle - Medical Cost Personal Dataset](https://www.kaggle.com/mirichoi0218/insurance).

## Folder Structure
```
Medical_Insurance_Prediction/
│-- data/               # Raw and processed datasets
│-- notebooks/          # Jupyter notebooks for EDA and modeling
│-- models/             # Trained models (if any)
│-- requirements.txt    # Dependencies
│-- README.md           # Project documentation
```

## Future Improvements
- Apply deep learning regression models for prediction
- Build a web app (Flask/Streamlit) for user interaction
- Provide personalized health insights based on predictions

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
