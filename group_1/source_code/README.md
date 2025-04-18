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

## 1. Navigate to source_code directory

## 2. Run Preprocess.ipynb to preprocess and clean data. This will save usable data to glucose_steps.csv in the Datasets folder of the root directory.

## 3. Run Classification.ipynb. This uses the cleaned data to develop a Random Forest Classification model that classifies sample data points as diabetic (1) or non-diabetic. 

## 4. 
