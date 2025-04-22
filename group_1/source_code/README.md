# CAP4770 Project Setup and Walkthrough

This guide walks you through the environment setup and the steps used to replicate the project's results.

# Setup Environment

## 1. Create and Activate the Virtual Environment (Optional)

### On macOS/Linux:
```bash
python -m venv venv
```
```bash
source venv/bin/activate
```

### On Windows: (with Powershell)
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```

### On Windows: (with Bash)
```bash
python -m venv venv
```
```bash
venv/Scripts/activate
```

## 2. Install Dependencies:
```bash
pip install -r requirements.txt
```

## 3. (If using a virtual environment) Register venv as Jupyter Kernel
```bash
python -m ipykernel install --user --name=myenv --display-name "Python (venv)"
```

## 4. Start Jupyter Lab
```bash
jupyter lab
```

## 5. (If using a virtual environment) Verify Python (venv) being used as Jupyter Lab kernel

# Replicate Results

### 1. Navigate to source_code directory

### 2. Run all cells in RandomForestClassification1.ipynb, RandomForestClassification2.ipynb, and XGBoost.ipynb. This uses the cleaned data from PreprocessGlucoseInstances.ipynb to develop a two different Random Forest Classification models and an XGBoost model that classifies sample data points as diabetic (1) or non-diabetic. It is important to note that these models classify specific instances of glucose levels per user as diabetic or non-diabetic, rather than classifying the user as a whole. In modern medicine, a patient is diagnosed with diabetes after they show elevated blood glucose on two different tests. Therefore, these models use activity measurements to classify glucose levels based on the user's baseline, which allows a supervised diabetic vs non-diabetic prediction for the user. 

### 3. Run all cells in UserClassificationModels.ipynb. This uses the cleaned data from PreProcessUserClassification.ipynb to develop two Random Forest Classification Models, one XGBoost model, and one HistGradient Boost model. These models differ from those previously mentioned because they use a different dataset and classify users as a whole, rather than classifying individual user data points. PreProcessUserClassification.ipynb uses NHANES data to expand upon the small 15 user Glucdict dataset. Data points for each user are aggregated and the models are than able classify the user as diabetic vs non-diabetic. 

### 4. Analyze results in each of the aforementioned Notebook files. The UserClassificationModels results can be found additionally in results_df.csv. This output shows that the HistGradient Boost model performs best, achieving an F-1 score of approximately 50. These models perform better than the initial models that predict individual instances of elevated blood sugar as well.

### 5. We have developed a Shiny app for further result visualization. In your command prompt, navigate to group_1/source_code/shiny and run 
```bash
python .\glucdict_dashboard_app.py
```
### Navigate to http://127.0.0.1:8000 or the
