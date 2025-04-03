# CAP4770-Project Setup

This guide walks you through creating a virtual environment, installing dependencies from `requirements.txt`, and starting Jupyter Lab.

## 1. Create and Activate the Virtual Environment

### On macOS/Linux:
```bash
python -m venv venv
```
```bash
source venv/bin/activate
```

### On Windows: 
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```

## 2. Install Dependencies:
```bash
pip install -r requirements.txt
```

## 3. Register venv as Jupyter Kernel
```bash
python -m ipykernel install --user --name=myenv --display-name "Python (venv)"
```

## 4. Start Jupyter Lab
```bash
jupyter lab
```

## 5. Verify Python (venv) being used as Jupyter Lab kernel
