# breast-cancer-decisiontree
Breast Cancer Prediction using Decision Tree Classifier | Python, scikit-learn, EDA, Visualization
# 🧠 Breast Cancer Prediction using Decision Tree Classifier

This project aims to detect whether a tumor is **malignant** or **benign** using a **Decision Tree Classifier** trained on breast cancer data. The dataset contains various features related to cell nuclei measured from digitized images of a breast mass.

---

## 📌 Features Used (Sample Columns)

- radius_mean, texture_mean, perimeter_mean, area_mean
- smoothness_mean, compactness_mean, concavity_mean
- concave points_mean, symmetry_mean, fractal_dimension_mean
- *_se and *_worst versions of the above for standard error and worst-case values

**Target column**: `diagnosis` (`M` = Malignant, `B` = Benign)

---

## ⚙️ Algorithms Used

- 🎯 **Decision Tree Classifier** (`sklearn.tree.DecisionTreeClassifier`)
- Criteria: Gini or Entropy (tested during tuning)
- Hyperparameter tuning and model evaluation included

---

##  Steps in the Notebook

1. **Data Loading & Cleaning**
2. **Exploratory Data Analysis (EDA)** with Seaborn & Matplotlib
3. **Feature Selection**
4. **Train/Test Split**
5. **Model Training with Decision Tree**
6. **Evaluation**: Accuracy, Confusion Matrix, Classification Report
7. **Model Export (Pickle)**

---

## 🛠️ Tools & Libraries

- Python
- Pandas, NumPy
- Scikit-learn
- Seaborn, Matplotlib
- Pickle

---

## 📁 Folder Structure

```
breast-cancer-decisiontree/
├── templates/
│   ├── form.html
│   └── index.html
├── app.py
├── breastcancerCLF.ipynb
├── DTreg.pkl
├── LICENSE
├── README.md
└── requirements.txt
```


