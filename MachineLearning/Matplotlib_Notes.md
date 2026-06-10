# 📊 Matplotlib — Complete Beginner's Guide

> **Matplotlib** is Python's most popular library for creating **charts, graphs, and visualizations**.  
> If you've ever seen a line graph, bar chart, or scatter plot in a Python tutorial — it was probably made with Matplotlib!

---

## 📌 Table of Contents

1. [What is Matplotlib & Why Use It?](#1-what-is-matplotlib--why-use-it)
2. [Installation & Import](#2-installation--import)
3. [Your First Plot](#3-your-first-plot)
4. [Line Plot](#4-line-plot)
5. [Bar Chart](#5-bar-chart)
6. [Scatter Plot](#6-scatter-plot)
7. [Histogram](#7-histogram)
8. [Pie Chart](#8-pie-chart)
9. [Customizing Your Plots](#9-customizing-your-plots)
10. [Multiple Plots (Subplots)](#10-multiple-plots-subplots)
11. [Saving Plots](#11-saving-plots)
12. [Box Plot](#12-box-plot)
13. [Heatmap](#13-heatmap)
14. [Area Plot](#14-area-plot)
15. [Plotting with Pandas](#15-plotting-with-pandas)
16. [Styling & Themes](#16-styling--themes)
17. [Annotations & Text](#17-annotations--text)
18. [Real-World Mini Projects](#18-real-world-mini-projects)
19. [Quick Cheat Sheet](#19-quick-cheat-sheet)

---

## 1. What is Matplotlib & Why Use It?

### 🤔 Think of it this way...

You have data about student marks, sales revenue, or temperature readings. **Numbers alone are boring and hard to understand.** A chart makes the story in the data **instantly visible**.

```
Raw data:     [85, 90, 78, 92, 88]     → 🤷 Hard to compare
Bar chart:    █████████████████████████  → 📊 Easy to see patterns!
```

### ✅ Types of Charts You Can Make

| Chart Type | Best For | Example Use |
|-----------|---------|-------------|
| Line Plot | Trends over time | Stock prices, temperature |
| Bar Chart | Comparing categories | Marks per student |
| Scatter Plot | Relationships | Height vs Weight |
| Histogram | Distribution | Age distribution |
| Pie Chart | Proportions | Market share |
| Box Plot | Spread & outliers | Salary ranges |
| Heatmap | Correlation | Feature relationships |

---

## 2. Installation & Import

```bash
pip install matplotlib
```

```python
import matplotlib.pyplot as plt    # 'plt' is the universal shorthand
import numpy as np                  # Often used for generating data
```

> 💡 We import `matplotlib.pyplot` (not just `matplotlib`) because `pyplot` has all the plotting functions we need.

---

## 3. Your First Plot

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create the plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('My First Plot! 🎉')

# Display the plot
plt.show()
```

> 🧠 **The basic workflow is always:**
> 1. Prepare data (x and y values)
> 2. Create the plot (`plt.plot()`, `plt.bar()`, etc.)
> 3. Customize (title, labels, colors)
> 4. Show it (`plt.show()`)

---

## 4. Line Plot

Best for showing **trends over time**.

### 4.1 Simple Line Plot

```python
import matplotlib.pyplot as plt
import numpy as np

# Monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [120, 135, 148, 155, 170, 180, 165, 190, 200, 215, 230, 250]

plt.figure(figsize=(10, 5))    # Width=10, Height=5 inches
plt.plot(months, sales, color='#2196F3', linewidth=2, marker='o')

plt.title('Monthly Sales 2024', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales (units)', fontsize=12)
plt.grid(True, alpha=0.3)     # Light grid lines

plt.tight_layout()
plt.show()
```

### 4.2 Multiple Lines

```python
months = np.arange(1, 13)
product_a = [120, 135, 148, 155, 170, 180, 165, 190, 200, 215, 230, 250]
product_b = [90, 100, 110, 130, 140, 155, 150, 160, 170, 185, 195, 210]
product_c = [60, 75, 85, 90, 100, 110, 120, 130, 140, 150, 160, 175]

plt.figure(figsize=(10, 6))

plt.plot(months, product_a, 'o-', label='Product A', color='#E91E63', linewidth=2)
plt.plot(months, product_b, 's--', label='Product B', color='#4CAF50', linewidth=2)
plt.plot(months, product_c, '^:', label='Product C', color='#FF9800', linewidth=2)

plt.title('Product Sales Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.legend(fontsize=11)        # Show the legend
plt.grid(True, alpha=0.3)
plt.xticks(months)             # Show all month numbers

plt.tight_layout()
plt.show()
```

> 💡 **Marker & Line Style Shortcuts:**
> | Code | Meaning |
> |------|---------|
> | `'o-'` | Circle markers + solid line |
> | `'s--'` | Square markers + dashed line |
> | `'^:'` | Triangle markers + dotted line |
> | `'D-.'` | Diamond markers + dash-dot line |

---

## 5. Bar Chart

Best for **comparing categories**.

### 5.1 Vertical Bar Chart

```python
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
marks = [85, 90, 78, 92, 88]
colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF']

plt.figure(figsize=(8, 5))
bars = plt.bar(students, marks, color=colors, edgecolor='white', width=0.6)

# Add value labels on top of each bar
for bar, mark in zip(bars, marks):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(mark), ha='center', va='bottom', fontweight='bold')

plt.title('Student Marks Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.ylim(0, 100)

plt.tight_layout()
plt.show()
```

### 5.2 Horizontal Bar Chart

```python
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Go', 'Rust']
popularity = [30, 25, 20, 12, 8, 5]

plt.figure(figsize=(8, 5))
plt.barh(languages, popularity, color='#42A5F5', edgecolor='white')

plt.title('Programming Language Popularity', fontsize=16, fontweight='bold')
plt.xlabel('Popularity (%)')

plt.tight_layout()
plt.show()
```

### 5.3 Grouped Bar Chart

```python
import numpy as np

students = ['Alice', 'Bob', 'Charlie', 'David']
math_marks = [85, 90, 78, 92]
science_marks = [90, 88, 82, 86]
english_marks = [78, 95, 80, 88]

x = np.arange(len(students))    # [0, 1, 2, 3]
width = 0.25                     # Width of each bar

plt.figure(figsize=(10, 6))

plt.bar(x - width, math_marks, width, label='Math', color='#FF6384')
plt.bar(x, science_marks, width, label='Science', color='#36A2EB')
plt.bar(x + width, english_marks, width, label='English', color='#FFCE56')

plt.xticks(x, students)
plt.title('Marks by Subject', fontsize=16, fontweight='bold')
plt.ylabel('Marks')
plt.legend()
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

### 5.4 Stacked Bar Chart

```python
students = ['Alice', 'Bob', 'Charlie', 'David']
math = [85, 90, 78, 92]
science = [90, 88, 82, 86]
english = [78, 95, 80, 88]

plt.figure(figsize=(8, 6))
plt.bar(students, math, label='Math', color='#FF6384')
plt.bar(students, science, bottom=math, label='Science', color='#36A2EB')
plt.bar(students, english,
        bottom=[m+s for m,s in zip(math, science)],
        label='English', color='#FFCE56')

plt.title('Total Marks (Stacked)', fontsize=16, fontweight='bold')
plt.ylabel('Total Marks')
plt.legend()

plt.tight_layout()
plt.show()
```

---

## 6. Scatter Plot

Best for showing **relationships** between two variables.

```python
import numpy as np

# Student study hours vs marks
np.random.seed(42)
hours_studied = np.random.uniform(1, 10, 50)     # 50 students, 1-10 hours
marks = hours_studied * 8 + np.random.normal(0, 5, 50)  # Linear relationship + noise
marks = np.clip(marks, 0, 100)

plt.figure(figsize=(8, 6))

plt.scatter(hours_studied, marks,
            c=marks,              # Color by marks (higher = warmer)
            cmap='RdYlGn',        # Red-Yellow-Green colormap
            s=80,                 # Marker size
            alpha=0.7,            # Transparency
            edgecolors='white')

plt.colorbar(label='Marks')      # Color legend
plt.title('Study Hours vs Marks', fontsize=16, fontweight='bold')
plt.xlabel('Hours Studied', fontsize=12)
plt.ylabel('Marks Obtained', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### Scatter with Size Variation (Bubble Chart)

```python
# City data: population, GDP, area
cities = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata']
population = [19, 20, 12, 10, 14]      # millions
gdp = [300, 400, 250, 200, 180]        # billion $
area = [1500, 600, 700, 400, 1800]     # sq km

plt.figure(figsize=(8, 6))
plt.scatter(population, gdp,
            s=[a/3 for a in area],      # Size = area
            c=['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'],
            alpha=0.7, edgecolors='black')

for i, city in enumerate(cities):
    plt.annotate(city, (population[i], gdp[i]),
                 textcoords="offset points", xytext=(10, 5), fontsize=10)

plt.title('Indian Cities: Population vs GDP', fontsize=14, fontweight='bold')
plt.xlabel('Population (millions)')
plt.ylabel('GDP (billion $)')

plt.tight_layout()
plt.show()
```

---

## 7. Histogram

Best for showing **distributions** — how frequently values occur.

```python
import numpy as np

# Exam marks for 200 students
np.random.seed(42)
marks = np.random.normal(loc=70, scale=15, size=200)   # Mean=70, Std=15
marks = np.clip(marks, 0, 100)

plt.figure(figsize=(8, 5))

plt.hist(marks, bins=15,                # 15 bars
         color='#42A5F5',
         edgecolor='white',
         alpha=0.8)

# Add mean line
plt.axvline(np.mean(marks), color='#E91E63', linestyle='--', linewidth=2,
            label=f'Mean: {np.mean(marks):.1f}')

plt.title('Distribution of Student Marks', fontsize=16, fontweight='bold')
plt.xlabel('Marks', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.legend(fontsize=11)

plt.tight_layout()
plt.show()
```

### Overlapping Histograms

```python
np.random.seed(42)
class_a = np.random.normal(75, 10, 150)
class_b = np.random.normal(65, 12, 150)

plt.figure(figsize=(8, 5))
plt.hist(class_a, bins=15, alpha=0.6, label='Class A', color='#2196F3', edgecolor='white')
plt.hist(class_b, bins=15, alpha=0.6, label='Class B', color='#FF5722', edgecolor='white')

plt.title('Marks Distribution: Class A vs Class B', fontsize=14, fontweight='bold')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()
```

---

## 8. Pie Chart

Best for showing **proportions** (parts of a whole).

```python
# Time spent in a day
activities = ['Sleep', 'Study', 'Social Media', 'Exercise', 'Food', 'Other']
hours = [7, 6, 3, 1.5, 1.5, 5]
colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40']
explode = (0, 0.1, 0, 0, 0, 0)    # "Pull out" Study slice

plt.figure(figsize=(8, 8))

plt.pie(hours,
        labels=activities,
        colors=colors,
        explode=explode,
        autopct='%1.1f%%',        # Show percentage
        shadow=True,
        startangle=140,
        textprops={'fontsize': 12})

plt.title("How I Spend My Day 📅", fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()
```

### Donut Chart (Pie with a hole)

```python
plt.figure(figsize=(7, 7))

wedges, texts, autotexts = plt.pie(
    hours, labels=activities, colors=colors,
    autopct='%1.1f%%', startangle=140,
    pctdistance=0.85,           # Move % labels outward
    textprops={'fontsize': 11})

# Draw white circle in the center → creates donut effect
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
plt.gca().add_artist(centre_circle)

plt.title("Daily Activity Distribution", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

> ⚠️ **When NOT to use pie charts:** When you have more than 6-7 categories. Use a bar chart instead.

---

## 9. Customizing Your Plots

### 9.1 Figure Size

```python
plt.figure(figsize=(12, 6))    # Width=12, Height=6 (inches)
```

### 9.2 Colors

```python
# Named colors
plt.plot(x, y, color='red')
plt.plot(x, y, color='steelblue')

# Hex colors
plt.plot(x, y, color='#FF6384')
plt.plot(x, y, color='#2196F3')

# RGB tuple (0-1 range)
plt.plot(x, y, color=(0.2, 0.6, 0.8))
```

### 9.3 Line Styles & Markers

```python
plt.plot(x, y, linestyle='-')      # Solid (default)
plt.plot(x, y, linestyle='--')     # Dashed
plt.plot(x, y, linestyle='-.')     # Dash-dot
plt.plot(x, y, linestyle=':')     # Dotted

plt.plot(x, y, marker='o')        # Circle
plt.plot(x, y, marker='s')        # Square
plt.plot(x, y, marker='^')        # Triangle up
plt.plot(x, y, marker='D')        # Diamond
plt.plot(x, y, marker='*')        # Star
```

### 9.4 Grid, Legend & Axis Limits

```python
plt.grid(True, alpha=0.3, linestyle='--')   # Light grid
plt.legend(loc='upper left', fontsize=12)   # Position the legend
plt.xlim(0, 10)                              # X-axis range
plt.ylim(0, 100)                             # Y-axis range
plt.xticks(rotation=45)                      # Rotate x-labels
```

### 9.5 All-in-One Example

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)

plt.figure(figsize=(10, 6))

plt.plot(x, np.sin(x), 'r-', label='sin(x)', linewidth=2)
plt.plot(x, np.cos(x), 'b--', label='cos(x)', linewidth=2)
plt.plot(x, np.sin(x) + np.cos(x), 'g:', label='sin(x)+cos(x)', linewidth=2)

plt.title('Trigonometric Functions', fontsize=18, fontweight='bold', pad=15)
plt.xlabel('x (radians)', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.legend(fontsize=12, framealpha=0.9)
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='black', linewidth=0.5)   # x-axis line
plt.axvline(x=np.pi, color='gray', linestyle='--', alpha=0.5, label='π')

plt.tight_layout()
plt.show()
```

---

## 10. Multiple Plots (Subplots)

### 10.1 Basic Subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
# This creates a 2×2 grid of plots

# Top-left: Line plot
axes[0, 0].plot([1,2,3,4], [10,20,25,30], 'b-o')
axes[0, 0].set_title('Line Plot')
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('Y')

# Top-right: Bar chart
axes[0, 1].bar(['A', 'B', 'C'], [30, 50, 40], color=['#FF6384', '#36A2EB', '#FFCE56'])
axes[0, 1].set_title('Bar Chart')

# Bottom-left: Scatter
import numpy as np
axes[1, 0].scatter(np.random.rand(30), np.random.rand(30), c='#4CAF50', alpha=0.7)
axes[1, 0].set_title('Scatter Plot')

# Bottom-right: Histogram
axes[1, 1].hist(np.random.normal(50, 10, 200), bins=15, color='#FF9800', edgecolor='white')
axes[1, 1].set_title('Histogram')

plt.suptitle('Four Types of Plots', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()
```

### 10.2 Different Sized Subplots

```python
fig = plt.figure(figsize=(12, 6))

# Big plot on the left (takes 2/3 width)
ax1 = fig.add_subplot(1, 2, 1)        # 1 row, 2 cols, position 1
ax1.plot([1,2,3,4,5], [2,4,6,8,10], 'r-o')
ax1.set_title('Main Plot')

# Small plot on the right
ax2 = fig.add_subplot(1, 2, 2)
ax2.bar(['A', 'B', 'C'], [10, 20, 15], color='steelblue')
ax2.set_title('Side Plot')

plt.tight_layout()
plt.show()
```

---

## 11. Saving Plots

```python
plt.figure(figsize=(8, 5))
plt.plot([1,2,3], [10,20,30])
plt.title('Saved Plot')

# Save as PNG (most common)
plt.savefig('my_plot.png', dpi=150, bbox_inches='tight')

# Save as PDF (for papers/reports)
plt.savefig('my_plot.pdf', bbox_inches='tight')

# Save as SVG (scalable, for web)
plt.savefig('my_plot.svg', bbox_inches='tight')

# With transparent background
plt.savefig('my_plot.png', dpi=150, transparent=True, bbox_inches='tight')
```

> 💡 **`bbox_inches='tight'`** removes extra whitespace around the plot.  
> 💡 **`dpi=150`** means 150 dots per inch (higher = better quality, larger file).

---

## 12. Box Plot

Best for showing **spread, median, and outliers**.

```python
import numpy as np

np.random.seed(42)
class_a = np.random.normal(75, 8, 50)
class_b = np.random.normal(70, 12, 50)
class_c = np.random.normal(80, 6, 50)

data = [class_a, class_b, class_c]

plt.figure(figsize=(8, 6))

bp = plt.boxplot(data,
                 labels=['Class A', 'Class B', 'Class C'],
                 patch_artist=True,       # Fill boxes with color
                 notch=True)              # Add notch at median

# Color the boxes
colors = ['#FF6384', '#36A2EB', '#FFCE56']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

plt.title('Marks Distribution by Class', fontsize=16, fontweight='bold')
plt.ylabel('Marks')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

> 🧠 **How to read a box plot:**
> ```
>    ─── Maximum (top whisker)
>    ┬
>    │   Upper Quartile (Q3 = 75th percentile)
>    ├── Median (Q2 = 50th percentile)
>    │   Lower Quartile (Q1 = 25th percentile)
>    ┴
>    ─── Minimum (bottom whisker)
>    ●   Outliers (dots beyond whiskers)
> ```

---

## 13. Heatmap

Best for showing **correlations** or **matrix data**.

```python
import numpy as np

# Correlation-like data
subjects = ['Math', 'Science', 'English', 'History', 'Art']
data = np.array([
    [1.00, 0.85, 0.42, 0.55, 0.20],
    [0.85, 1.00, 0.38, 0.50, 0.15],
    [0.42, 0.38, 1.00, 0.72, 0.60],
    [0.55, 0.50, 0.72, 1.00, 0.45],
    [0.20, 0.15, 0.60, 0.45, 1.00]
])

plt.figure(figsize=(8, 7))
im = plt.imshow(data, cmap='RdYlBu_r', vmin=0, vmax=1)

# Add color bar
plt.colorbar(im, label='Correlation')

# Add labels
plt.xticks(range(5), subjects, rotation=45, ha='right')
plt.yticks(range(5), subjects)

# Add values on each cell
for i in range(5):
    for j in range(5):
        color = 'white' if data[i, j] > 0.7 else 'black'
        plt.text(j, i, f'{data[i,j]:.2f}', ha='center', va='center',
                 color=color, fontsize=11, fontweight='bold')

plt.title('Subject Correlation Matrix', fontsize=16, fontweight='bold', pad=15)

plt.tight_layout()
plt.show()
```

---

## 14. Area Plot

Best for showing **cumulative data** or **stacked quantities** over time.

```python
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
laptop = [50, 55, 60, 65, 70, 80]
phone = [80, 85, 75, 90, 95, 100]
tablet = [30, 35, 40, 38, 45, 50]

plt.figure(figsize=(10, 6))
plt.stackplot(months, laptop, phone, tablet,
              labels=['Laptop', 'Phone', 'Tablet'],
              colors=['#FF6384', '#36A2EB', '#FFCE56'],
              alpha=0.8)

plt.title('Product Sales Over Time (Stacked)', fontsize=16, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## 15. Plotting with Pandas

Pandas DataFrames have built-in plotting that uses Matplotlib!

```python
import pandas as pd
import numpy as np

# Create sample data
df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [120, 135, 148, 155, 170, 180],
    'Expenses': [100, 110, 115, 120, 130, 140],
    'Profit': [20, 25, 33, 35, 40, 40]
})

# Line plot directly from DataFrame
df.plot(x='Month', y=['Sales', 'Expenses', 'Profit'],
        figsize=(10, 6), marker='o', linewidth=2)
plt.title('Monthly Financial Summary', fontsize=16, fontweight='bold')
plt.ylabel('Amount ($)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Bar plot from DataFrame
df.plot(x='Month', y=['Sales', 'Expenses'], kind='bar',
        figsize=(10, 6), color=['#2196F3', '#FF5722'])
plt.title('Sales vs Expenses', fontsize=16, fontweight='bold')
plt.ylabel('Amount ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Histogram from DataFrame
marks_df = pd.DataFrame({'Marks': np.random.normal(70, 15, 200)})
marks_df['Marks'].plot(kind='hist', bins=20, color='#4CAF50',
                        edgecolor='white', figsize=(8, 5))
plt.title('Marks Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Marks')
plt.tight_layout()
plt.show()
```

---

## 16. Styling & Themes

### 16.1 Available Styles

```python
# See all available styles
print(plt.style.available)
# ['seaborn-v0_8', 'ggplot', 'dark_background', 'fivethirtyeight', ...]
```

### 16.2 Using Styles

```python
# Apply a style for all subsequent plots
plt.style.use('seaborn-v0_8-darkgrid')

# Or use temporarily
with plt.style.context('ggplot'):
    plt.plot([1,2,3], [4,5,6])
    plt.title('ggplot style')
    plt.show()
```

### 16.3 Popular Styles

```python
# Dark background (cool for presentations)
plt.style.use('dark_background')

# FiveThirtyEight style (clean, modern)
plt.style.use('fivethirtyeight')

# Seaborn style (beautiful defaults)
plt.style.use('seaborn-v0_8')

# ggplot style (R-like)
plt.style.use('ggplot')

# Reset to default
plt.style.use('default')
```

---

## 17. Annotations & Text

### 17.1 Adding Text

```python
plt.figure(figsize=(8, 5))
x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]

plt.plot(x, y, 'bo-', linewidth=2, markersize=8)

# Add text at a specific position
plt.text(2, 25, 'Peak!', fontsize=14, color='red', fontweight='bold')

plt.title('Plot with Annotations')
plt.tight_layout()
plt.show()
```

### 17.2 Annotations with Arrows

```python
plt.figure(figsize=(8, 5))
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, 'b-', linewidth=2)

# Arrow annotation pointing to the maximum
plt.annotate('Maximum\n(π/2, 1)',
             xy=(np.pi/2, 1),              # Point to annotate
             xytext=(np.pi/2 + 2, 0.7),    # Text position
             fontsize=12,
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             fontweight='bold',
             color='red')

# Arrow to minimum
plt.annotate('Minimum',
             xy=(3*np.pi/2, -1),
             xytext=(3*np.pi/2 + 1.5, -0.5),
             fontsize=12,
             arrowprops=dict(arrowstyle='->', color='blue', lw=2),
             color='blue')

plt.title('Sin Wave with Annotations', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 17.3 Shaded Regions

```python
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, 'b-', linewidth=2)

# Shade area under the curve (between x=0 and x=π)
plt.fill_between(x, y, where=(x <= np.pi), alpha=0.3, color='green', label='Positive area')
plt.fill_between(x, y, where=(x >= np.pi) & (x <= 2*np.pi), alpha=0.3, color='red', label='Negative area')

plt.title('Area Under the Curve', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='black', linewidth=0.5)
plt.tight_layout()
plt.show()
```

---

## 18. Real-World Mini Projects

### 🎯 Project 1: Student Performance Dashboard

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
math = [85, 90, 78, 92, 88]
science = [90, 88, 72, 86, 95]
english = [78, 95, 80, 88, 82]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Student Performance Dashboard 📊', fontsize=20, fontweight='bold')

# 1. Grouped Bar Chart
x = np.arange(len(students))
w = 0.25
axes[0, 0].bar(x - w, math, w, label='Math', color='#FF6384')
axes[0, 0].bar(x, science, w, label='Science', color='#36A2EB')
axes[0, 0].bar(x + w, english, w, label='English', color='#FFCE56')
axes[0, 0].set_xticks(x)
axes[0, 0].set_xticklabels(students)
axes[0, 0].set_title('Marks by Subject')
axes[0, 0].legend()
axes[0, 0].set_ylim(0, 100)

# 2. Average marks (horizontal bar)
avg = [(m+s+e)/3 for m,s,e in zip(math, science, english)]
colors = ['#4CAF50' if a >= 85 else '#FF9800' if a >= 75 else '#F44336' for a in avg]
axes[0, 1].barh(students, avg, color=colors)
axes[0, 1].set_title('Average Marks')
axes[0, 1].set_xlim(0, 100)
for i, v in enumerate(avg):
    axes[0, 1].text(v + 1, i, f'{v:.1f}', va='center', fontweight='bold')

# 3. Subject totals (Pie chart)
subject_totals = [sum(math), sum(science), sum(english)]
axes[1, 0].pie(subject_totals,
               labels=['Math', 'Science', 'English'],
               colors=['#FF6384', '#36A2EB', '#FFCE56'],
               autopct='%1.1f%%', startangle=140)
axes[1, 0].set_title('Subject-wise Total Distribution')

# 4. Line chart (student progress feeling)
axes[1, 1].plot(students, math, 'o-', label='Math', color='#FF6384', linewidth=2)
axes[1, 1].plot(students, science, 's--', label='Science', color='#36A2EB', linewidth=2)
axes[1, 1].plot(students, english, '^:', label='English', color='#FFCE56', linewidth=2)
axes[1, 1].set_title('Per-Student Trends')
axes[1, 1].legend()
axes[1, 1].set_ylim(60, 100)
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### 🎯 Project 2: Weather Data Visualization

```python
import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Delhi weather data (approximate)
max_temp = [21, 24, 30, 36, 40, 40, 35, 34, 34, 33, 28, 23]
min_temp = [7, 10, 15, 21, 26, 28, 27, 26, 25, 19, 12, 8]
rainfall = [17, 18, 13, 8, 13, 54, 210, 173, 117, 10, 1, 10]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Temperature plot
ax1.plot(months, max_temp, 'r-o', label='Max Temp', linewidth=2, markersize=8)
ax1.plot(months, min_temp, 'b-s', label='Min Temp', linewidth=2, markersize=8)
ax1.fill_between(months, min_temp, max_temp, alpha=0.15, color='orange')
ax1.set_title('Delhi Monthly Temperature 🌡️', fontsize=16, fontweight='bold')
ax1.set_ylabel('Temperature (°C)', fontsize=12)
ax1.legend(fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, 45)

# Rainfall plot
colors = ['#42A5F5' if r < 50 else '#1565C0' if r < 150 else '#0D47A1' for r in rainfall]
bars = ax2.bar(months, rainfall, color=colors, edgecolor='white', width=0.6)
ax2.set_title('Delhi Monthly Rainfall 🌧️', fontsize=16, fontweight='bold')
ax2.set_ylabel('Rainfall (mm)', fontsize=12)
ax2.grid(axis='y', alpha=0.3)

# Add value labels
for bar, val in zip(bars, rainfall):
    if val > 20:
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
                 f'{val}', ha='center', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()
```

---

## 19. Quick Cheat Sheet

```
BASIC:
  plt.figure(figsize=(w,h))   → set figure size
  plt.show()                   → display plot
  plt.savefig('file.png')      → save to file
  plt.tight_layout()           → fix overlapping

PLOT TYPES:
  plt.plot(x, y)               → line plot
  plt.bar(x, y)                → vertical bar chart
  plt.barh(x, y)               → horizontal bar chart
  plt.scatter(x, y)            → scatter plot
  plt.hist(data, bins=n)       → histogram
  plt.pie(sizes, labels=l)     → pie chart
  plt.boxplot(data)            → box plot
  plt.imshow(matrix)           → heatmap
  plt.stackplot(x, y1, y2)    → area chart

CUSTOMIZATION:
  plt.title('Title')           → add title
  plt.xlabel('X')              → x-axis label
  plt.ylabel('Y')              → y-axis label
  plt.legend()                 → show legend
  plt.grid(True)               → show grid
  plt.xlim(a, b)               → set x-axis range
  plt.ylim(a, b)               → set y-axis range
  plt.xticks(rotation=45)      → rotate x labels
  plt.colorbar()               → add color legend

SUBPLOTS:
  fig, axes = plt.subplots(rows, cols)
  axes[r, c].plot(x, y)       → plot on specific subplot
  fig.suptitle('Title')        → main title

STYLE:
  plt.style.use('seaborn-v0_8')
  plt.style.use('dark_background')
  plt.style.use('ggplot')

COLORS:
  Named: 'red', 'blue', 'steelblue', 'coral'
  Hex:   '#FF6384', '#36A2EB', '#4CAF50'
  Cmap:  'viridis', 'RdYlGn', 'coolwarm', 'Blues'

LINE STYLES:
  '-' solid  '--' dashed  '-.' dash-dot  ':' dotted

MARKERS:
  'o' circle  's' square  '^' triangle  'D' diamond  '*' star
```

---

> 🎉 **Congratulations!** You now know Matplotlib!  
> With **NumPy** + **Pandas** + **Matplotlib**, you have the complete toolkit for data analysis!
> 
> 📚 **Your Learning Path:**
> 1. ✅ [NumPy_Notes.md](./NumPy_Notes.md) — Numerical computing
> 2. ✅ [Pandas_Notes.md](./Pandas_Notes.md) — Data manipulation
> 3. ✅ Matplotlib_Notes.md — Data visualization
> 4. 🔜 Next: **Scikit-learn** for Machine Learning!
