# 🐼 Pandas — Complete Beginner's Guide

> **Pandas** = **Pan**el **Da**ta (from econometrics)  
> It is the most popular Python library for **data analysis and manipulation**.  
> If NumPy is for numbers, Pandas is for **tables** (like Excel/Google Sheets but in Python).

---

## 📌 Table of Contents

1. [What is Pandas & Why Use It?](#1-what-is-pandas--why-use-it)
2. [Installation & Import](#2-installation--import)
3. [Series — 1-D Data](#3-series--1-d-data)
4. [DataFrame — 2-D Data (Tables)](#4-dataframe--2-d-data-tables)
5. [Reading & Writing Data Files](#5-reading--writing-data-files)
6. [Viewing & Inspecting Data](#6-viewing--inspecting-data)
7. [Selecting Data](#7-selecting-data)
8. [Filtering Data](#8-filtering-data)
9. [Adding & Removing Columns/Rows](#9-adding--removing-columnsrows)
10. [Handling Missing Data](#10-handling-missing-data)
11. [Sorting Data](#11-sorting-data)
12. [Grouping & Aggregation](#12-grouping--aggregation)
13. [Merging & Joining DataFrames](#13-merging--joining-dataframes)
14. [String Operations](#14-string-operations)
15. [Apply & Lambda Functions](#15-apply--lambda-functions)
16. [Pivot Tables](#16-pivot-tables)
17. [Date & Time](#17-date--time)
18. [Real-World Mini Projects](#18-real-world-mini-projects)
19. [Quick Cheat Sheet](#19-quick-cheat-sheet)

---

## 1. What is Pandas & Why Use It?

### 🤔 Think of it this way...

You have a CSV file with 10,000 rows of student data. You want to:
- Find the average marks per class
- Filter students who scored above 90
- Add a new column for grades (A, B, C, D)

**Without Pandas:** You'd write 50+ lines of Python with file reading, loops, and manual calculations. 😰  
**With Pandas:** You do it in 5 lines! 🚀

### ✅ Why Pandas?

| Task | Without Pandas | With Pandas |
|------|---------------|-------------|
| Read a CSV file | `open()`, loops, split | `pd.read_csv('file.csv')` |
| Filter rows | Manual loops | `df[df['marks'] > 90]` |
| Group by category | Dict + loops | `df.groupby('class').mean()` |
| Handle missing data | if-else checks | `df.fillna(0)` |
| Export to Excel | External libraries | `df.to_excel('file.xlsx')` |

---

## 2. Installation & Import

```bash
pip install pandas
```

```python
import pandas as pd    # 'pd' is the universal shorthand
import numpy as np     # Often used together with NumPy
```

---

## 3. Series — 1-D Data

A **Series** is like a single column of data with labels (index).

```python
# From a list
marks = pd.Series([85, 90, 78, 92, 88])
print(marks)
# Output:
# 0    85
# 1    90
# 2    78
# 3    92
# 4    88
# dtype: int64

# With custom labels (index)
marks = pd.Series(
    [85, 90, 78, 92, 88],
    index=['Alice', 'Bob', 'Charlie', 'David', 'Eve']
)
print(marks)
# Output:
# Alice      85
# Bob        90
# Charlie    78
# David      92
# Eve        88
# dtype: int64

# Access by label
print(marks['Bob'])         # 90
print(marks[['Alice', 'Eve']])  # Alice=85, Eve=88

# From a dictionary
ages = pd.Series({'Alice': 20, 'Bob': 22, 'Charlie': 21})
print(ages)
```

> 🧠 **Think of Series as:** A numbered (or labeled) list — like one column from an Excel sheet.

---

## 4. DataFrame — 2-D Data (Tables)

A **DataFrame** is a table with rows and columns. This is what you'll use 90% of the time!

### 4.1 Creating a DataFrame

```python
# From a dictionary (most common way)
data = {
    'Name':    ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age':     [20, 22, 21, 23, 20],
    'City':    ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai'],
    'Marks':   [85, 90, 78, 92, 88],
    'Grade':   ['A', 'A+', 'B+', 'A+', 'A']
}
df = pd.DataFrame(data)
print(df)
# Output:
#       Name  Age     City  Marks Grade
# 0    Alice   20    Delhi     85     A
# 1      Bob   22   Mumbai     90    A+
# 2  Charlie   21    Delhi     78    B+
# 3    David   23  Chennai     92    A+
# 4      Eve   20   Mumbai     88     A
```

### 4.2 From a list of lists

```python
data = [
    ['Alice', 20, 85],
    ['Bob', 22, 90],
    ['Charlie', 21, 78]
]
df = pd.DataFrame(data, columns=['Name', 'Age', 'Marks'])
print(df)
```

### 4.3 From a NumPy array

```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df)
#    A  B  C
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9
```

---

## 5. Reading & Writing Data Files

### 5.1 Reading Files

```python
# CSV file (most common)
df = pd.read_csv('students.csv')

# Excel file
df = pd.read_excel('students.xlsx')

# JSON file
df = pd.read_json('students.json')

# From a URL
df = pd.read_csv('https://example.com/data.csv')

# With options
df = pd.read_csv('students.csv',
    sep=',',              # delimiter
    header=0,             # which row has column names (0 = first row)
    index_col='Roll_No',  # use a column as the index
    usecols=['Name', 'Marks', 'Grade'],  # read only specific columns
    nrows=100,            # read only first 100 rows
    encoding='utf-8'      # character encoding
)
```

### 5.2 Writing Files

```python
# To CSV
df.to_csv('output.csv', index=False)   # index=False to skip row numbers

# To Excel
df.to_excel('output.xlsx', index=False)

# To JSON
df.to_json('output.json')
```

---

## 6. Viewing & Inspecting Data

```python
# Sample data
data = {
    'Name':   ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age':    [20, 22, 21, 23, 20, 24, 22],
    'City':   ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai', 'Delhi', 'Chennai'],
    'Marks':  [85, 90, 78, 92, 88, 67, 95]
}
df = pd.DataFrame(data)

# First 5 rows (peek at data)
print(df.head())

# Last 3 rows
print(df.tail(3))

# Shape (rows, columns)
print(df.shape)       # (7, 4)

# Column names
print(df.columns)     # Index(['Name', 'Age', 'City', 'Marks'])

# Data types of each column
print(df.dtypes)
# Name     object  (string)
# Age      int64
# City     object
# Marks    int64

# Quick summary of everything
print(df.info())
# Shows: column names, non-null counts, data types, memory usage

# Statistical summary (numbers only)
print(df.describe())
#              Age      Marks
# count   7.000000   7.000000
# mean   21.714286  85.000000
# std     1.496026  10.000000
# min    20.000000  67.000000
# 25%    20.500000  81.500000
# 50%    22.000000  88.000000
# 75%    22.500000  91.000000
# max    24.000000  95.000000

# Number of unique values per column
print(df.nunique())

# Value counts for a column
print(df['City'].value_counts())
# Delhi      3
# Mumbai     2
# Chennai    2
```

---

## 7. Selecting Data

### 7.1 Select Columns

```python
# Single column (returns Series)
print(df['Name'])

# Multiple columns (returns DataFrame)
print(df[['Name', 'Marks']])
```

### 7.2 Select Rows by Position — iloc (integer location)

```python
# First row
print(df.iloc[0])

# Rows 0 to 2 (exclusive of 3)
print(df.iloc[0:3])

# Specific rows and columns by position
print(df.iloc[0:3, 0:2])    # First 3 rows, first 2 columns

# Last row
print(df.iloc[-1])
```

### 7.3 Select Rows by Label — loc (label-based)

```python
# By index label
print(df.loc[0])             # Row with index 0

# By index and column name
print(df.loc[0, 'Name'])    # 'Alice'

# Multiple rows and specific columns
print(df.loc[0:2, ['Name', 'Marks']])
#       Name  Marks
# 0    Alice     85
# 1      Bob     90
# 2  Charlie     78
```

> 🧠 **iloc vs loc:**
> - `iloc` → **i**nteger position (like array index: 0, 1, 2...)
> - `loc`  → **l**abel-based (uses column names and index labels)

---

## 8. Filtering Data

### 8.1 Basic Filtering

```python
# Students with marks above 85
print(df[df['Marks'] > 85])
#     Name  Age     City  Marks
# 1    Bob   22   Mumbai     90
# 3  David   23  Chennai     92
# 4    Eve   20   Mumbai     88
# 6  Grace   22  Chennai     95

# Students from Delhi
print(df[df['City'] == 'Delhi'])

# Students aged 20 OR 22
print(df[df['Age'].isin([20, 22])])
```

### 8.2 Multiple Conditions

```python
# AND condition: marks > 85 AND city is Mumbai
print(df[(df['Marks'] > 85) & (df['City'] == 'Mumbai')])

# OR condition: marks > 90 OR age < 21
print(df[(df['Marks'] > 90) | (df['Age'] < 21)])
```

> ⚠️ **Important:** Use `&` (not `and`) and `|` (not `or`) for Pandas filtering. Always wrap each condition in `()`.

### 8.3 Query Method (cleaner syntax)

```python
# Same as above but more readable
print(df.query('Marks > 85 and City == "Mumbai"'))
```

---

## 9. Adding & Removing Columns/Rows

### 9.1 Adding Columns

```python
# New column with a formula
df['Percentage'] = df['Marks'] / 100 * 100   # already percentage here

# New column based on condition
df['Result'] = df['Marks'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')

# New column with a fixed value
df['School'] = 'ABC High School'

print(df.head())
```

### 9.2 Removing Columns

```python
# Drop one column
df = df.drop('School', axis=1)

# Drop multiple columns
df = df.drop(['Percentage', 'Result'], axis=1)
```

### 9.3 Adding Rows

```python
# Add a new row
new_student = pd.DataFrame({'Name': ['Henry'], 'Age': [21], 'City': ['Pune'], 'Marks': [82]})
df = pd.concat([df, new_student], ignore_index=True)
```

### 9.4 Removing Rows

```python
# Drop by index
df = df.drop(0)           # Drop row at index 0
df = df.drop([1, 3, 5])   # Drop multiple rows

# Drop rows matching a condition
df = df[df['Marks'] >= 60]   # Keep only passing students
```

---

## 10. Handling Missing Data

Missing data is very common in real datasets (empty cells, NaN, null).

```python
# Create sample data with missing values
data = {
    'Name':  ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age':   [20, None, 21, 23, None],
    'Marks': [85, 90, None, 92, 88]
}
df = pd.DataFrame(data)
print(df)
#       Name   Age  Marks
# 0    Alice  20.0   85.0
# 1      Bob   NaN   90.0     ← Age is missing
# 2  Charlie  21.0    NaN     ← Marks is missing
# 3    David  23.0   92.0
# 4      Eve   NaN   88.0     ← Age is missing
```

### 10.1 Detecting Missing Values

```python
# Check for missing values
print(df.isnull())           # True where NaN
print(df.isnull().sum())     # Count NaN per column
# Age      2
# Marks    1

# Total missing values
print(df.isnull().sum().sum())   # 3
```

### 10.2 Handling Missing Values

```python
# Option 1: DROP rows with any missing value
df_clean = df.dropna()
print(df_clean)   # Only Alice and David remain

# Option 2: DROP rows where a SPECIFIC column is missing
df_clean = df.dropna(subset=['Marks'])

# Option 3: FILL missing values with a number
df_filled = df.fillna(0)

# Option 4: FILL with mean/median
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Option 5: FILL with forward/backward fill
df['Age'] = df['Age'].ffill()    # Forward fill (use previous value)
df['Age'] = df['Age'].bfill()    # Backward fill (use next value)
```

---

## 11. Sorting Data

```python
# Sort by Marks (ascending)
print(df.sort_values('Marks'))

# Sort by Marks (descending) — highest first
print(df.sort_values('Marks', ascending=False))

# Sort by multiple columns
print(df.sort_values(['City', 'Marks'], ascending=[True, False]))
# First sort by City (A-Z), then by Marks (high to low) within each city

# Sort by index
print(df.sort_index())

# Get the rank
df['Rank'] = df['Marks'].rank(ascending=False)
print(df)
```

---

## 12. Grouping & Aggregation

GroupBy is one of Pandas' most powerful features — like pivot tables in Excel!

### 12.1 Basic GroupBy

```python
data = {
    'Name':    ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'City':    ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai', 'Delhi'],
    'Subject': ['Math', 'Math', 'Science', 'Math', 'Science', 'Science'],
    'Marks':   [85, 90, 78, 92, 88, 67]
}
df = pd.DataFrame(data)

# Average marks per city
print(df.groupby('City')['Marks'].mean())
# Chennai    92.0
# Delhi      76.67
# Mumbai     89.0

# Multiple aggregations
print(df.groupby('City')['Marks'].agg(['mean', 'min', 'max', 'count']))
#          mean  min  max  count
# Chennai  92.0   92   92      1
# Delhi    76.7   67   85      3
# Mumbai   89.0   88   90      2
```

### 12.2 Group by Multiple Columns

```python
# Average marks per city per subject
print(df.groupby(['City', 'Subject'])['Marks'].mean())
# City     Subject
# Chennai  Math       92.0
# Delhi    Math       85.0
#          Science    72.5
# Mumbai   Math       90.0
#          Science    88.0
```

### 12.3 Named Aggregations (Clean Output)

```python
result = df.groupby('City').agg(
    avg_marks=('Marks', 'mean'),
    top_marks=('Marks', 'max'),
    student_count=('Name', 'count')
).reset_index()

print(result)
#      City  avg_marks  top_marks  student_count
# 0  Chennai      92.0         92              1
# 1    Delhi      76.7         85              3
# 2   Mumbai      89.0         90              2
```

---

## 13. Merging & Joining DataFrames

Like SQL JOINs — combine tables based on a common column.

### 13.1 Merge (SQL-style Join)

```python
# Student info
students = pd.DataFrame({
    'ID':   [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

# Student marks
marks = pd.DataFrame({
    'ID':    [1, 2, 3, 5],
    'Marks': [85, 90, 78, 95]
})

# Inner join (only matching IDs)
inner = pd.merge(students, marks, on='ID', how='inner')
print(inner)
#    ID     Name  Marks
# 0   1    Alice     85
# 1   2      Bob     90
# 2   3  Charlie     78

# Left join (all students, marks if available)
left = pd.merge(students, marks, on='ID', how='left')
print(left)
#    ID     Name  Marks
# 0   1    Alice   85.0
# 1   2      Bob   90.0
# 2   3  Charlie   78.0
# 3   4    David    NaN    ← David has no marks in the marks table

# Outer join (all from both)
outer = pd.merge(students, marks, on='ID', how='outer')
print(outer)
```

### 13.2 Concat (Stack DataFrames)

```python
# Stack vertically (add more rows)
df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Marks': [85, 90]})
df2 = pd.DataFrame({'Name': ['Charlie', 'David'], 'Marks': [78, 92]})

combined = pd.concat([df1, df2], ignore_index=True)
print(combined)
#      Name  Marks
# 0   Alice     85
# 1     Bob     90
# 2 Charlie     78
# 3   David     92

# Stack horizontally (add more columns)
info = pd.DataFrame({'Age': [20, 22], 'City': ['Delhi', 'Mumbai']})
combined_h = pd.concat([df1, info], axis=1)
print(combined_h)
```

---

## 14. String Operations

Pandas has built-in string methods through `.str` accessor!

```python
df = pd.DataFrame({
    'Name':  ['alice smith', 'BOB JONES', 'Charlie Brown', '  david  '],
    'Email': ['alice@gmail.com', 'bob@yahoo.com', 'charlie@gmail.com', 'david@outlook.com']
})

# Case conversion
print(df['Name'].str.upper())       # ALICE SMITH, BOB JONES, ...
print(df['Name'].str.lower())       # alice smith, bob jones, ...
print(df['Name'].str.title())       # Alice Smith, Bob Jones, ...

# Strip whitespace
print(df['Name'].str.strip())       # Removes leading/trailing spaces

# Contains (search within strings)
print(df['Email'].str.contains('gmail'))  # [True, False, True, False]

# Split
print(df['Email'].str.split('@'))   # [['alice', 'gmail.com'], ...]

# Extract domain
df['Domain'] = df['Email'].str.split('@').str[1]
print(df['Domain'])   # gmail.com, yahoo.com, gmail.com, outlook.com

# Replace
print(df['Name'].str.replace('smith', 'SMITH'))

# Length
print(df['Name'].str.len())   # Character count
```

---

## 15. Apply & Lambda Functions

Apply lets you run **any function** on your data — ultimate flexibility!

### 15.1 Apply on a Column (Series)

```python
df = pd.DataFrame({
    'Name':  ['Alice', 'Bob', 'Charlie'],
    'Marks': [85, 45, 78]
})

# Simple function
def get_grade(marks):
    if marks >= 90: return 'A+'
    elif marks >= 80: return 'A'
    elif marks >= 70: return 'B'
    elif marks >= 60: return 'C'
    else: return 'F'

df['Grade'] = df['Marks'].apply(get_grade)
print(df)
#       Name  Marks Grade
# 0    Alice     85     A
# 1      Bob     45     F
# 2  Charlie     78     B
```

### 15.2 Lambda Functions (quick one-liners)

```python
# Double the marks
df['Double'] = df['Marks'].apply(lambda x: x * 2)

# Pass/Fail
df['Result'] = df['Marks'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')

# Apply to entire DataFrame (row-wise)
df['Summary'] = df.apply(
    lambda row: f"{row['Name']} scored {row['Marks']}", axis=1
)
print(df)
```

### 15.3 Map (for simple value replacement)

```python
# Replace values using a dictionary
grade_map = {'A+': 10, 'A': 9, 'B': 8, 'C': 7, 'F': 0}
df['Grade_Points'] = df['Grade'].map(grade_map)
print(df)
```

---

## 16. Pivot Tables

Like Excel pivot tables — summarize data in a cross-tabulation format.

```python
data = {
    'Student': ['Alice', 'Alice', 'Bob', 'Bob', 'Charlie', 'Charlie'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Marks':   [85, 90, 78, 82, 92, 88]
}
df = pd.DataFrame(data)

# Pivot table
pivot = df.pivot_table(
    values='Marks',       # What to aggregate
    index='Student',      # Rows
    columns='Subject',    # Columns
    aggfunc='mean'        # Aggregation function
)
print(pivot)
# Subject  Math  Science
# Student
# Alice      85       90
# Bob        78       82
# Charlie    92       88

# Cross-tabulation (counts)
data2 = {
    'City':   ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai', 'Delhi'],
    'Grade':  ['A', 'A+', 'B', 'A+', 'A', 'A']
}
df2 = pd.DataFrame(data2)
print(pd.crosstab(df2['City'], df2['Grade']))
```

---

## 17. Date & Time

```python
# Create date column
df = pd.DataFrame({
    'Date': ['2024-01-15', '2024-02-20', '2024-03-25', '2024-04-10'],
    'Sales': [150, 200, 180, 220]
})

# Convert string to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract parts
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day_Name'] = df['Date'].dt.day_name()     # Monday, Tuesday, etc.
df['Quarter'] = df['Date'].dt.quarter

print(df)
#         Date  Sales  Year  Month  Day  Day_Name  Quarter
# 0 2024-01-15    150  2024      1   15    Monday        1
# 1 2024-02-20    200  2024      2   20   Tuesday        1
# 2 2024-03-25    180  2024      3   25    Monday        1
# 3 2024-04-10    220  2024      4   10 Wednesday        2

# Filter by date range
mask = (df['Date'] >= '2024-02-01') & (df['Date'] <= '2024-03-31')
print(df[mask])

# Date arithmetic
df['Next_Month'] = df['Date'] + pd.DateOffset(months=1)
```

---

## 18. Real-World Mini Projects

### 🎯 Project 1: Student Report Card Generator

```python
import pandas as pd

# Student data
data = {
    'Name':    ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Math':    [85, 90, 78, 45, 92],
    'Science': [90, 88, 72, 55, 95],
    'English': [78, 95, 80, 60, 88],
    'History': [88, 82, 76, 40, 91]
}
df = pd.DataFrame(data)

# Calculate total and average
subjects = ['Math', 'Science', 'English', 'History']
df['Total'] = df[subjects].sum(axis=1)
df['Average'] = df[subjects].mean(axis=1).round(2)

# Assign grades
def assign_grade(avg):
    if avg >= 90: return 'A+'
    elif avg >= 80: return 'A'
    elif avg >= 70: return 'B'
    elif avg >= 60: return 'C'
    else: return 'F'

df['Grade'] = df['Average'].apply(assign_grade)

# Assign rank
df['Rank'] = df['Average'].rank(ascending=False).astype(int)

# Sort by rank
df = df.sort_values('Rank')
print(df)
print(f"\n🏆 Topper: {df.iloc[0]['Name']} with {df.iloc[0]['Average']}% average!")
```

### 🎯 Project 2: Sales Data Analysis

```python
import pandas as pd
import numpy as np

# Create sample sales data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100, freq='D')
data = {
    'Date': dates,
    'Product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones'], 100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'Units': np.random.randint(1, 20, 100),
    'Price': np.random.choice([999, 699, 499, 149], 100)
}
df = pd.DataFrame(data)
df['Revenue'] = df['Units'] * df['Price']

# Total revenue per product
print("Revenue by Product:")
print(df.groupby('Product')['Revenue'].sum().sort_values(ascending=False))

# Best performing region
print("\nRevenue by Region:")
print(df.groupby('Region')['Revenue'].sum().sort_values(ascending=False))

# Monthly trends
df['Month'] = df['Date'].dt.month_name()
monthly = df.groupby('Month')['Revenue'].sum()
print("\nMonthly Revenue:")
print(monthly)
```

---

## 19. Quick Cheat Sheet

```
CREATION:
  pd.Series([1,2,3])                → 1-D data
  pd.DataFrame({'col': [1,2,3]})    → 2-D table
  pd.read_csv('file.csv')           → from CSV

INSPECTION:
  df.head()   df.tail()   df.shape   df.info()   df.describe()
  df.dtypes   df.columns  df.nunique()  df['col'].value_counts()

SELECTION:
  df['col']           → single column
  df[['col1','col2']] → multiple columns
  df.iloc[0]          → by position
  df.loc[0, 'col']    → by label

FILTERING:
  df[df['col'] > 5]                     → condition
  df[(df['A'] > 5) & (df['B'] < 10)]   → multiple conditions
  df.query('col > 5')                   → query string

MODIFICATION:
  df['new'] = values        → add column
  df.drop('col', axis=1)    → remove column
  df.drop(0)                → remove row
  df.rename(columns={})     → rename columns

MISSING DATA:
  df.isnull().sum()     → count NaN
  df.dropna()           → drop rows with NaN
  df.fillna(value)      → fill NaN

GROUPING:
  df.groupby('col').mean()              → group and aggregate
  df.groupby('col').agg(['mean','sum']) → multiple aggregations

MERGING:
  pd.merge(df1, df2, on='key')     → SQL-style join
  pd.concat([df1, df2])            → stack DataFrames

SORTING:
  df.sort_values('col')                    → sort by column
  df.sort_values('col', ascending=False)   → descending

EXPORT:
  df.to_csv('file.csv', index=False)
  df.to_excel('file.xlsx', index=False)
```

---

> 🎉 **Congratulations!** You now know Pandas!  
> **Next up:** Learn **Matplotlib** for creating beautiful visualizations → [Matplotlib_Notes.md](./Matplotlib_Notes.md)
