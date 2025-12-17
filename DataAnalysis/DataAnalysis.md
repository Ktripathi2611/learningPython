# Data Analysis – Detailed Notes

---

## 1. Data Analysis

Data Analysis is the process of inspecting, cleaning, transforming, and modeling data to discover useful information, draw conclusions, and support decision-making.

**Key steps:**

* Data collection
* Data cleaning
* Exploratory Data Analysis (EDA)
* Modeling
* Evaluation
* Interpretation

**Tools commonly used:** Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

---

## 2. Installing Anaconda

Anaconda is a Python distribution that includes most data science libraries.

**Steps:**

1. Visit [https://www.anaconda.com](https://www.anaconda.com)
2. Download Anaconda (Python 3.x)
3. Install and check using:

```bash
conda --version
```

**Advantages:**

* Preinstalled libraries
* Conda environment management
* Jupyter Notebook support

---

## 3. Libraries and Important Properties

### NumPy

* Used for numerical computation
* Core object: ndarray

### Pandas

* Used for data manipulation
* Core objects: Series, DataFrame

Important properties:

```python
df.shape      # rows, columns
df.dtypes     # data types
df.columns    # column names
df.index      # row index
```

---

## 4. Importing CSV File

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

Common parameters:

* `sep` – delimiter
* `header`
* `encoding`

---

## 5. Methods to View File

```python
df.head()
df.tail()
df.info()
df.describe()
```

Used to understand structure and statistics of data.

---

## 6. Data Cleaning

Process of fixing or removing incorrect, incomplete, or irrelevant data.

### Handling missing values

```python
df.isnull().sum()
df.dropna()
df.fillna(0)
```

---

## 7. Data Formatting

Ensures data types are correct.

```python
df["price"] = df["price"].astype(int)
df["date"] = pd.to_datetime(df["date"])
```

---

## 8. Data Normalization

Brings values into a common scale.

### Min-Max Normalization

```python
df["x_norm"] = (df["x"] - df["x"].min()) / (df["x"].max() - df["x"].min())
```

---

## 9. Data Normalization 2

### Z-score Normalization

```python
df["x_z"] = (df["x"] - df["x"].mean()) / df["x"].std()
```

---

## 10. Binning

Binning converts numeric data into categorical bins.

```python
bins = [0, 50, 100, 150]
labels = ["Low", "Medium", "High"]
df["category"] = pd.cut(df["value"], bins, labels=labels)
```

---

## 11. Binning 2

### Equal Frequency Binning

```python
df["bin"] = pd.qcut(df["value"], q=4)
```

---

## 12. Value Counts

Used to count frequency of unique values.

```python
df["brand"].value_counts()
```

---

## 13. Boxplot and Scatterplot

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x=df["price"])
sns.scatterplot(x=df["engine"], y=df["price"])
```

---

## 14. GroupBy

Used for split-apply-combine operations.

```python
df.groupby("brand")["price"].mean()
```

---

## 15. Pivot

Creates spreadsheet-style pivot tables.

```python
pd.pivot_table(df, values="price", index="brand", columns="fuel")
```

---

## 16. Heat Map 1

Visual representation of data using colors.

```python
sns.heatmap(df.corr(), annot=True)
```

---

## 17. Heat Map 2

Heatmap after groupby or pivot.

```python
pivot = df.pivot("brand", "fuel", "price")
sns.heatmap(pivot)
```

---

## 18. ANOVA (Analysis of Variance)

Used to compare means of multiple groups.

```python
from scipy import stats
stats.f_oneway(group1, group2, group3)
```

---

## 19. Correlation

Measures relationship between variables.

```python
df.corr()
```

---

## 20. Correlation 2

### Pearson Correlation

```python
stats.pearsonr(df["x"], df["y"])
```

---

## 21. Simple Linear Regression

Relationship between one independent and one dependent variable.

Formula:

```
y = b0 + b1x
```

---

## 22. Multiple Linear Regression

Multiple independent variables.

Formula:

```
y = b0 + b1x1 + b2x2 + ...
```

---

## 23. Simple Linear Regression using Python

```python
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X, y)
pred = lm.predict(X)
```

---

## 24. Multiple Linear Regression using Python

```python
X = df[["engine", "horsepower"]]
y = df["price"]

lm.fit(X, y)
```

---

## 25. Regression Plot

```python
sns.regplot(x="engine", y="price", data=df)
```

---

## 26. Residual Plot

Shows difference between actual and predicted values.

```python
sns.residplot(x=df["engine"], y=df["price"])
```

---

## 27. Distribution Plot 1

```python
sns.distplot(df["price"], hist=True)
```

---

## 28. Distribution Plot 2

Compare actual vs predicted.

```python
sns.kdeplot(y, label="Actual")
sns.kdeplot(pred, label="Predicted")
```

---

## 29. Polynomial Regression 1

Used when relationship is non-linear.

```python
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
```

---

## 30. Polynomial Regression 2

```python
lm.fit(X_poly, y)
```

---

## 31. In-Sample Evaluation

Evaluation using training data.

```python
lm.score(X, y)
```

---

## 32. Mean Squared Error (MSE)

Measures average squared difference between actual and predicted.

```python
from sklearn.metrics import mean_squared_error
mean_squared_error(y, pred)
```

---

## 33. R Squared (R²) – Concept

Explains how much variance is explained by the model.

* R² = 1 → perfect fit
* R² = 0 → no explanatory power

---

## 34. R Squared 2 (With Example)

```python
r2 = lm.score(X, y)
print(r2)
```

**Example:**

* R² = 0.82 means 82% of variation in output is explained by input variables.

---

**End of Notes**
