# California Housing Price Prediction 🏡
## Live Demo
🔗 https://your-streamlit-app-url.streamlit.app

<img width="1919" height="981" alt="image" src="https://github.com/user-attachments/assets/9f3e493c-e7c0-47e5-bb9f-185975373287" />


A machine learning project that predicts **median house values in California districts** using demographic and geographic features.
The project includes **data exploration, feature engineering, model training, and a deployed Streamlit web application**.

---

## 📌 Project Overview

This project uses the **California Housing Dataset** to train a regression model that predicts housing prices based on features such as:

* Median income
* Population
* Number of rooms and bedrooms
* Geographic location (latitude & longitude)
* Ocean proximity

The trained model is deployed as an interactive **Streamlit web application** where users can input features and obtain price predictions.

---

## 🚀 Features

* Interactive **Streamlit web interface**
* Real-time **house price prediction**
* Complete **data preprocessing pipeline**
* Custom **feature engineering transformer**
* End-to-end **machine learning workflow**
* Reproducible dataset download using a script

---

## 🧠 Machine Learning Workflow

1. **Data Exploration**

   * Dataset inspection
   * Correlation analysis
   * Geographic and income visualizations

2. **Feature Engineering**

   * Rooms per household
   * Population per household
   * Bedrooms per room

3. **Data Preprocessing**

   * Missing value imputation
   * Feature scaling
   * One-hot encoding for categorical variables

4. **Model Training**

   * Linear Regression
   * Decision Tree Regressor
   * Random Forest Regressor

5. **Hyperparameter Tuning**

   * GridSearchCV used to find optimal Random Forest parameters

6. **Final Model**

   * Best Random Forest model combined with preprocessing in a single **Scikit-learn Pipeline**

---

## 🏗 Project Structure

```
California-Housing-Prediction
│
├── datasets/
│
├── model/
│   └── housing_pipeline.pkl
│
├── notebooks/
│   └── housing.ipynb
│
├── src/
│   └── transformers.py
│
├── download_dataset.py
├── main.py
├── requirements.txt
└── README.md
```

### Folder Explanation

| Folder/File           | Purpose                                                |
| --------------------- | ------------------------------------------------------ |
| `datasets/`           | Contains the housing dataset (downloaded using script) |
| `model/`              | Saved trained pipeline                                 |
| `notebooks/`          | Exploratory analysis and model training                |
| `src/`                | Custom transformers and reusable ML components         |
| `download_dataset.py` | Script to download the dataset                         |
| `main.py`             | Streamlit application                                  |

---

## 📥 Downloading the Dataset

Instead of storing the dataset in the repository, it can be downloaded automatically.

Run the following command from the project root:

```
python download_dataset.py
```

This script will:

1. Download the **California Housing dataset**
2. Extract it
3. Save it to:

```
datasets/housing.csv
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/california-housing-prediction.git
cd california-housing-prediction
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment.

### Windows

```
venv\Scripts\activate
```

### Mac/Linux

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Download the dataset:

```
python download_dataset.py
```

---

## ▶️ Running the Streamlit App

From the project root directory run:

```
streamlit run main.py
```

The application will launch in your browser.

---

## 📊 Example Prediction

Users can input features such as:

* Longitude
* Latitude
* Median income
* Total rooms
* Population
* Ocean proximity

The application processes the inputs using the trained pipeline and outputs the **predicted median house value**.

---

## 🧩 Model Pipeline

The deployed model is a **Scikit-learn Pipeline** that includes both preprocessing and the trained model.

```
ColumnTransformer
   ├── Numeric Pipeline
   │      ├── Median Imputation
   │      ├── Feature Engineering
   │      └── Standard Scaling
   │
   └── Categorical Pipeline
          └── OneHotEncoding
               ↓
        RandomForestRegressor
```

This ensures **training and prediction use the exact same preprocessing steps**.

---

## 🧠 Custom Transformer

Feature engineering is implemented using a custom transformer located in:

```
src/transformers.py
```

The transformer creates additional features:

* `rooms_per_household`
* `population_per_household`
* `bedrooms_per_room`

---

## 🛠 Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Streamlit
* Matplotlib / Seaborn

---

## Model Performance

Final Model: Random Forest Regressor

RMSE on test set: 47,747


---
