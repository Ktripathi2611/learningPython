# 📘 NumPy — Complete Beginner's Guide

> **NumPy** = **Num**erical **Py**thon  
> It is the fundamental library for numerical computing in Python.  
> Almost every data science / ML library (Pandas, Matplotlib, Scikit-learn, TensorFlow) is built **on top of NumPy**.

---

## 📌 Table of Contents

1. [What is NumPy & Why Use It?](#1-what-is-numpy--why-use-it)
2. [Installation](#2-installation)
3. [Importing NumPy](#3-importing-numpy)
4. [Creating Arrays](#4-creating-arrays)
5. [Array Attributes](#5-array-attributes)
6. [Indexing & Slicing](#6-indexing--slicing)
7. [Reshaping Arrays](#7-reshaping-arrays)
8. [Array Operations (Math)](#8-array-operations-math)
9. [Broadcasting](#9-broadcasting)
10. [Useful NumPy Functions](#10-useful-numpy-functions)
11. [Stacking & Splitting](#11-stacking--splitting)
12. [Boolean Indexing & Filtering](#12-boolean-indexing--filtering)
13. [Random Numbers](#13-random-numbers)
14. [Copying vs Viewing](#14-copying-vs-viewing)
15. [Real-World Mini Projects](#15-real-world-mini-projects)
16. [Quick Cheat Sheet](#16-quick-cheat-sheet)

---

## 1. What is NumPy & Why Use It?

### 🤔 Think of it this way...

Imagine you have a list of 1 million exam scores and you want to add 5 bonus marks to each student.

**With plain Python:**
```python
scores = [78, 85, 92, 67, ...]  # 1 million values
new_scores = []
for s in scores:
    new_scores.append(s + 5)  # 😴 Slow loop!
```

**With NumPy:**
```python
import numpy as np
scores = np.array([78, 85, 92, 67, ...])
new_scores = scores + 5  # 🚀 Done! No loop needed!
```

### ✅ Why NumPy?

| Feature | Python List | NumPy Array |
|---------|------------|-------------|
| Speed | Slow (loops) | 50-100x faster |
| Memory | More memory | Less memory |
| Math Operations | Manual loops | Built-in vectorized |
| Multi-dimensional | Nested lists (messy) | Clean ndarray |
| Used in ML/AI | ❌ Not directly | ✅ Foundation |

---

## 2. Installation

```bash
# Using pip
pip install numpy

# Using conda
conda install numpy
```

---

## 3. Importing NumPy

```python
import numpy as np   # 'np' is the standard shorthand everyone uses
```

> 💡 **Why `np`?** It's a universal convention. When you see `np.` in any tutorial, book, or StackOverflow answer, they mean NumPy.

---

## 4. Creating Arrays

### 4.1 From a Python List

```python
# 1-D Array (like a single row of data)
marks = np.array([85, 90, 78, 92, 88])
print(marks)
# Output: [85 90 78 92 88]

# 2-D Array (like a table — rows and columns)
student_marks = np.array([
    [85, 90, 78],    # Student 1: Math, Science, English
    [92, 88, 95],    # Student 2
    [67, 72, 80]     # Student 3
])
print(student_marks)
# Output:
# [[85 90 78]
#  [92 88 95]
#  [67 72 80]]
```

> 🧠 **Think of it like Excel:**  
> 1-D array = one row  
> 2-D array = a table with rows and columns  
> 3-D array = multiple tables (like sheets in Excel)

### 4.2 Using Built-in Functions

```python
# All zeros — useful for initializing
zeros = np.zeros((2, 3))
print(zeros)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]

# All ones
ones = np.ones((3, 3))
print(ones)
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

# A specific value everywhere
fives = np.full((2, 4), 5)
print(fives)
# Output:
# [[5 5 5 5]
#  [5 5 5 5]]

# Identity matrix (1s on diagonal, 0s elsewhere)
# Used a LOT in linear algebra and ML
identity = np.identity(3)
print(identity)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
```

### 4.3 Ranges and Sequences

```python
# arange: like Python's range() but returns an array
numbers = np.arange(0, 10, 2)   # start=0, stop=10, step=2
print(numbers)
# Output: [0 2 4 6 8]

# linspace: evenly spaced numbers between start and end
temperature = np.linspace(0, 100, 5)  # 5 values from 0 to 100
print(temperature)
# Output: [  0.  25.  50.  75. 100.]
```

> 💡 **When to use which?**
> - `arange` → you know the **step size** (e.g., count by 2s)
> - `linspace` → you know **how many values** you want (e.g., 5 evenly spaced)

### 4.4 Empty & Empty-like

```python
# empty: creates array with whatever values are in memory (NOT zeros!)
empty = np.empty((2, 3))
print(empty)   # Will show random garbage values — just allocates memory

# empty_like: same shape/type as another array
template = np.array([1.0, 2.0, 3.0])
new_arr = np.empty_like(template)
print(new_arr)  # Same shape as template, but random values
```

> ⚠️ **Warning:** `np.empty()` does NOT give you zeros! It's faster than `np.zeros()` because it skips initialization, but the values are unpredictable.

---

## 5. Array Attributes

```python
student_marks = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [67, 72, 80]
])

# Shape: (rows, columns)
print(student_marks.shape)     # (3, 3) → 3 students, 3 subjects

# Number of dimensions
print(student_marks.ndim)      # 2 → it's a 2D array (table)

# Total elements
print(student_marks.size)      # 9 → 3 × 3 = 9 values

# Data type
print(student_marks.dtype)     # int64 → 64-bit integers

# Bytes per element
print(student_marks.itemsize)  # 8 → each int64 takes 8 bytes
```

### Quick Reference Table

| Attribute | What it tells you | Example |
|-----------|------------------|---------|
| `.shape` | Dimensions (rows, cols) | `(3, 3)` |
| `.ndim` | Number of dimensions | `2` |
| `.size` | Total element count | `9` |
| `.dtype` | Data type | `int64` |
| `.itemsize` | Bytes per element | `8` |

---

## 6. Indexing & Slicing

### 6.1 Basic Indexing (like picking items from a shelf)

```python
marks = np.array([85, 90, 78, 92, 88])

# First element (index starts at 0!)
print(marks[0])    # 85

# Last element
print(marks[-1])   # 88

# Second element
print(marks[1])    # 90
```

### 6.2 2-D Array Indexing

```python
table = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Element at row 0, column 1
print(table[0, 1])    # 20

# Element at row 2, column 2
print(table[2, 2])    # 90

# Modify a value
table[0, 1] = 25
print(table[0, 1])    # 25
```

> 🧠 **Remember:** `array[row, column]` — Row first, then column!

### 6.3 Slicing (getting a chunk of data)

```python
marks = np.array([85, 90, 78, 92, 88, 76, 95])

# First 3 elements
print(marks[0:3])     # [85 90 78]
print(marks[:3])      # [85 90 78]  (same thing, 0 is optional)

# From index 2 to end
print(marks[2:])      # [78 92 88 76 95]

# Every other element
print(marks[::2])     # [85 78 88 95]

# Reverse the array
print(marks[::-1])    # [95 76 88 92 78 90 85]
```

### 6.4 2-D Slicing

```python
table = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

# First two rows, first two columns
print(table[:2, :2])
# Output:
# [[10 20]
#  [50 60]]

# All rows, last column
print(table[:, -1])    # [40 80 120]

# Second row only
print(table[1, :])     # [50 60 70 80]
```

---

## 7. Reshaping Arrays

### 7.1 reshape() — Change the shape without changing data

```python
arr = np.arange(12)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Reshape to 3 rows × 4 columns
table = arr.reshape(3, 4)
print(table)
# Output:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Reshape to 4 rows × 3 columns
table2 = arr.reshape(4, 3)
print(table2)
# Output:
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]
```

> ⚠️ **Rule:** Total elements must match!  
> 12 elements → can reshape to (3,4), (4,3), (2,6), (6,2), (12,1), (1,12)  
> 12 elements → CANNOT reshape to (3,5) because 3×5=15 ≠ 12

### 7.2 Using -1 (let NumPy figure it out)

```python
arr = np.arange(12)

# "I want 3 rows, figure out the columns"
print(arr.reshape(3, -1))
# Output: shape (3, 4) — NumPy calculated 4 columns

# "I want 2 columns, figure out the rows"
print(arr.reshape(-1, 2))
# Output: shape (6, 2) — NumPy calculated 6 rows
```

### 7.3 Flatten & Ravel — Convert back to 1-D

```python
table = np.array([[1, 2, 3], [4, 5, 6]])

# flatten: returns a COPY (original unchanged)
flat = table.flatten()
print(flat)    # [1 2 3 4 5 6]

# ravel: returns a VIEW (changes affect original!)
flat_view = table.ravel()
print(flat_view)   # [1 2 3 4 5 6]
```

### 7.4 Transpose — Swap rows and columns

```python
table = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(table.T)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]
```

---

## 8. Array Operations (Math)

### 8.1 Element-wise Operations

```python
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print(a + b)     # [11 22 33 44]
print(a - b)     # [ 9 18 27 36]
print(a * b)     # [ 10  40  90 160]
print(a / b)     # [10. 10. 10. 10.]
print(a ** 2)    # [ 100  400  900 1600]  (square each element)
print(a % 3)     # [1 2 0 1]  (modulo — remainder)
```

> 🧠 **Key Insight:** Operations happen **element by element** — no loops needed!

### 8.2 Scalar Operations (one number applied to all)

```python
marks = np.array([78, 85, 92, 67, 73])

# Add 5 bonus marks to everyone
new_marks = marks + 5
print(new_marks)   # [83 90 97 72 78]

# Scale marks to percentage (out of 100 → out of 10)
scaled = marks / 10
print(scaled)      # [7.8 8.5 9.2 6.7 7.3]
```

### 8.3 Comparison Operations

```python
marks = np.array([78, 85, 92, 67, 73])

print(marks > 80)       # [False  True  True False False]
print(marks == 92)       # [False False  True False False]
print(marks >= 73)       # [ True  True  True False  True]
```

---

## 9. Broadcasting

Broadcasting is NumPy's way of handling arrays with **different shapes** during operations.

```python
# Example: Adding a column-wise bonus to a marks table
marks = np.array([
    [78, 85, 92],   # Student 1
    [67, 73, 88],   # Student 2
    [91, 84, 76]    # Student 3
])

# Different bonus for each subject: Math=5, Science=3, English=2
bonus = np.array([5, 3, 2])

# Broadcasting: bonus (1×3) is applied to each row (3×3)
new_marks = marks + bonus
print(new_marks)
# Output:
# [[83 88 94]
#  [72 76 90]
#  [96 87 78]]
```

> 🧠 **Rule of Broadcasting:**  
> NumPy compares shapes from the **right**. Dimensions are compatible if they are equal OR one of them is 1.

---

## 10. Useful NumPy Functions

### 10.1 Aggregation (Summary Statistics)

```python
marks = np.array([78, 85, 92, 67, 73, 88, 91])

print(np.sum(marks))     # 574  — total of all marks
print(np.mean(marks))    # 82.0 — average
print(np.median(marks))  # 85.0 — middle value
print(np.std(marks))     # 9.07 — standard deviation
print(np.min(marks))     # 67   — lowest mark
print(np.max(marks))     # 92   — highest mark
print(np.argmin(marks))  # 3    — INDEX of lowest mark
print(np.argmax(marks))  # 2    — INDEX of highest mark
```

### 10.2 Axis — Row-wise vs Column-wise

```python
table = np.array([
    [85, 90, 78],   # Student 1
    [92, 88, 95],   # Student 2
    [67, 72, 80]    # Student 3
])

# Sum of each column (axis=0 → move down rows)
print(np.sum(table, axis=0))   # [244 250 253]
# Meaning: Total Math=244, Total Science=250, Total English=253

# Sum of each row (axis=1 → move across columns)
print(np.sum(table, axis=1))   # [253 275 219]
# Meaning: Student 1 total=253, Student 2 total=275, Student 3 total=219
```

> 🧠 **Memory Trick for Axis:**
> - `axis=0` → operation goes **DOWN** (collapses rows)
> - `axis=1` → operation goes **ACROSS** (collapses columns)

### 10.3 Sorting

```python
arr = np.array([42, 15, 88, 3, 67])

print(np.sort(arr))          # [ 3 15 42 67 88]  — ascending
print(np.sort(arr)[::-1])    # [88 67 42 15  3]  — descending

# Sort indices (useful to find rank positions)
print(np.argsort(arr))       # [3 1 0 4 2]  — indices that would sort it
```

### 10.4 Unique Values

```python
grades = np.array(['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C'])

print(np.unique(grades))                       # ['A' 'B' 'C' 'D']
print(np.unique(grades, return_counts=True))    # (['A','B','C','D'], [3,2,2,1])
```

### 10.5 Mathematical Functions

```python
angles = np.array([0, 30, 45, 60, 90])
radians = np.radians(angles)    # Convert degrees to radians

print(np.sin(radians))   # [0.   0.5  0.707 0.866 1.  ]
print(np.cos(radians))   # [1.   0.866 0.707 0.5   0.  ]
print(np.sqrt(np.array([4, 9, 16, 25])))   # [2. 3. 4. 5.]
print(np.log(np.array([1, 10, 100])))       # [0.   2.3  4.6]  (natural log)
```

---

## 11. Stacking & Splitting

### 11.1 Stacking (Combining Arrays)

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Vertical stack (stack as rows)
print(np.vstack((a, b)))
# Output:
# [[1 2 3]
#  [4 5 6]]

# Horizontal stack (stack side by side)
print(np.hstack((a, b)))
# Output: [1 2 3 4 5 6]
```

### 11.2 Splitting (Breaking Arrays Apart)

```python
arr = np.array([10, 20, 30, 40, 50, 60])

# Split into 3 equal parts
parts = np.split(arr, 3)
print(parts)   # [array([10, 20]), array([30, 40]), array([50, 60])]

# Split at specific positions
parts2 = np.split(arr, [2, 4])
print(parts2)  # [array([10, 20]), array([30, 40]), array([50, 60])]
```

---

## 12. Boolean Indexing & Filtering

This is one of NumPy's **superpowers** — filter data without loops!

```python
marks = np.array([78, 85, 92, 67, 73, 88, 91, 55, 60])

# Find all marks above 80
high_scores = marks[marks > 80]
print(high_scores)    # [85 92 88 91]

# Find marks between 70 and 90
mid_range = marks[(marks >= 70) & (marks <= 90)]
print(mid_range)      # [78 85 73 88]

# Count how many students scored above 80
print(np.sum(marks > 80))    # 4

# Replace failing marks (below 60) with 60
marks[marks < 60] = 60
print(marks)   # [78 85 92 67 73 88 91 60 60]
```

### np.where() — If-Else for arrays

```python
marks = np.array([78, 85, 45, 92, 38, 88])

# Pass/Fail based on marks
result = np.where(marks >= 50, 'Pass', 'Fail')
print(result)   # ['Pass' 'Pass' 'Fail' 'Pass' 'Fail' 'Pass']
```

---

## 13. Random Numbers

```python
# Random float between 0 and 1
print(np.random.rand())          # e.g., 0.7342

# Random array (2×3) between 0 and 1
print(np.random.rand(2, 3))

# Random integers
print(np.random.randint(1, 100, size=5))    # 5 random ints from 1-99
# e.g., [42 17 83 91  6]

# Random from normal distribution (mean=0, std=1)
print(np.random.randn(5))
# e.g., [-0.23  1.15 -0.87  0.42  0.03]

# Shuffle an array (in-place)
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)   # e.g., [3 1 5 2 4]

# Reproducible results (same random numbers every time)
np.random.seed(42)
print(np.random.rand(3))   # Always: [0.37454012 0.95071431 0.73199394]
```

---

## 14. Copying vs Viewing

### ⚠️ This is a common source of bugs!

```python
original = np.array([1, 2, 3, 4, 5])

# VIEW — shares the same data
view = original[1:4]
view[0] = 99
print(original)   # [1 99  3  4  5]  ← Original CHANGED! 😱

# COPY — independent copy
original = np.array([1, 2, 3, 4, 5])
copy = original[1:4].copy()
copy[0] = 99
print(original)   # [1 2 3 4 5]  ← Original SAFE! ✅
```

> 💡 **Rule of Thumb:** Use `.copy()` when you want to modify sliced data without affecting the original.

---

## 15. Real-World Mini Projects

### 🎯 Project 1: Student Grade Calculator

```python
import numpy as np

# 5 students, 4 subjects
marks = np.array([
    [85, 90, 78, 88],   # Alice
    [92, 88, 95, 91],   # Bob
    [67, 72, 80, 75],   # Charlie
    [55, 60, 45, 50],   # David
    [98, 95, 92, 97]    # Eve
])

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
subjects = ['Math', 'Science', 'English', 'History']

# Average marks per student
avg_per_student = np.mean(marks, axis=1)
print("Average per student:", avg_per_student)

# Highest scorer
best_student_idx = np.argmax(avg_per_student)
print(f"Topper: {students[best_student_idx]} with {avg_per_student[best_student_idx]:.1f} avg")

# Subject with highest average
avg_per_subject = np.mean(marks, axis=0)
best_subject_idx = np.argmax(avg_per_subject)
print(f"Easiest subject: {subjects[best_subject_idx]} (avg: {avg_per_subject[best_subject_idx]:.1f})")

# Students who passed all subjects (passing = 50)
all_passed = np.all(marks >= 50, axis=1)
print("Passed all subjects:", [s for s, p in zip(students, all_passed) if p])
```

### 🎯 Project 2: Simple Image as Array

```python
import numpy as np

# A grayscale image is just a 2D array of pixel values (0=black, 255=white)
image = np.random.randint(0, 256, size=(100, 100))

# Make it brighter (increase all pixel values by 50)
brighter = np.clip(image + 50, 0, 255)   # clip to stay in valid range

# Invert the image (like a negative)
inverted = 255 - image

print(f"Original brightness: {np.mean(image):.1f}")
print(f"Brighter version: {np.mean(brighter):.1f}")
print(f"Inverted version: {np.mean(inverted):.1f}")
```

---

## 16. Quick Cheat Sheet

```
CREATION:
  np.array([1,2,3])          → from list
  np.zeros((r,c))            → all zeros
  np.ones((r,c))             → all ones
  np.full((r,c), value)      → all same value
  np.arange(start,stop,step) → sequence
  np.linspace(start,stop,n)  → n evenly spaced
  np.identity(n)             → identity matrix
  np.random.rand(r,c)        → random 0-1

INSPECTION:
  arr.shape   arr.dtype   arr.size   arr.ndim

MANIPULATION:
  arr.reshape(r,c)   arr.flatten()   arr.ravel()   arr.T

MATH:
  np.sum()  np.mean()  np.std()  np.min()  np.max()
  np.sqrt()  np.abs()  np.exp()  np.log()

FILTERING:
  arr[arr > 5]              → boolean indexing
  np.where(condition, x, y) → if-else

COMBINING:
  np.vstack((a,b))  np.hstack((a,b))  np.concatenate()

SORTING:
  np.sort(arr)  np.argsort(arr)  np.unique(arr)
```

---

> 🎉 **Congratulations!** You now know the essentials of NumPy!  
> **Next up:** Learn **Pandas** for working with tables and datasets → [Pandas_Notes.md](./Pandas_Notes.md)
