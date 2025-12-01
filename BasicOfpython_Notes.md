# Python Basics - Study Notes

> [!NOTE]
> These notes are organized based on the concepts covered in `BasicOfpython.ipynb`. Each section includes explanations, syntax examples, and key points to remember.

---

## Table of Contents
1. [Basic Printing](#1-basic-printing)
2. [String Types and Quotation Marks](#2-string-types-and-quotation-marks)
3. [Boolean Operations](#3-boolean-operations)
4. [Variables](#4-variables)
5. [Python Keywords](#5-python-keywords)
6. [Primitive Data Types](#6-primitive-data-types)
7. [String Operations](#7-string-operations)
8. [Type Conversion and Type Casting](#8-type-conversion-and-type-casting)

---

## 1. Basic Printing

The `print()` function displays output to the console.

**Syntax:**
```python
print("hello world!")
```

**Examples:**
```python
print("hellow world !")  # Output: hellow world !
print(' hello world')     # Output:  hello world
print('''hello world''')  # Output: hello world
```

**Key Points:**
- `print()` can use double quotes `"`, single quotes `'`, or triple quotes `'''` or `"""`
- Triple quotes are useful for multi-line strings

---

## 2. String Types and Quotation Marks

Python allows different types of quotation marks for strings.

**Single vs Double vs Triple Quotes:**

| Quote Type | Example | Use Case |
|------------|---------|----------|
| Double `"` | `"hello"` | Standard strings |
| Single `'` | `'hello'` | Standard strings |
| Triple `'''` or `"""` | `"""multi-line"""` | Multi-line strings with newlines |

**Example with Multi-line String:**
```python
"""hellow   
   how are you"""
# This preserves the newline and spacing
```

---

## 3. Boolean Operations

Boolean values are `True` or `False` and can be combined using logical operators.

**Logical Operators:**

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `and` | Returns True if both operands are True | `True and False` | `False` |
| `or` | Returns True if at least one operand is True | `True or False` | `True` |
| `not` | Returns the opposite boolean value | `not True` | `False` |

**Examples:**
```python
True and False  # Output: False
True or False   # Output: True
```

---

## 4. Variables

Variables store data values and can be reassigned.

### Variable Assignment
```python
a = 1
print(a)  # Output: 1

b = 2
print(b)  # Output: 2

c = a + b
print(c)  # Output: 3
```

### Variable Deletion
Use the `del` keyword to remove a variable:
```python
del b
print(b)  # NameError: name 'b' is not defined
```

### Variable Reassignment
Variables can be reassigned with different values:
```python
x = 5
print(x)  # Output: 5

x = 36
print(x)  # Output: 36
```

### Variable Operations
```python
x = 36
y = 1
x = x * y
print(x)  # Output: 36
```

### String Variables
```python
a = "kushal"
print(a)          # Output: kushal
print(a.upper())  # Output: KUSHAL
```

> [!IMPORTANT]
> Variable names are case-sensitive: `name`, `Name`, and `NAME` are different variables.

---

## 5. Python Keywords

Keywords are reserved words in Python that have special meanings and cannot be used as variable names.

**View All Keywords:**
```python
import keyword
print(keyword.kwlist)
```

**Common Keywords List:**
```
False, None, True, and, as, assert, async, await, break, class, continue, 
def, del, elif, else, except, finally, for, from, global, if, import, in, 
is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

> [!CAUTION]
> Never use Python keywords as variable names—it will cause syntax errors!

---

## 6. Primitive Data Types

Python has several built-in data types for storing different kinds of values.

### Integer (`int`)
Whole numbers without decimal points.

```python
age = 25
print(age)        # Output: 25
print(type(age))  # Output: <class 'int'>
```

### Float (`float`)
Numbers with decimal points.

```python
age = 25.5
print(age)        # Output: 25.5
print(type(age))  # Output: <class 'float'>
```

### String (`str`)
Text data enclosed in quotes.

```python
name = "sachin"
print(name)        # Output: sachin
print(type(name))  # Output: <class 'str'>
```

### Boolean (`bool`)
True or False values.

```python
name = True
print(name)        # Output: True
print(type(name))  # Output: <class 'bool'>
```

### NoneType (`None`)
Represents the absence of a value.

```python
name = None
print(name)        # Output: None
print(type(name))  # Output: <class 'NoneType'>
```

**Data Type Summary Table:**

| Type | Example | Description |
|------|---------|-------------|
| `int` | `25` | Integer numbers |
| `float` | `25.5` | Decimal numbers |
| `str` | `"sachin"` | Text strings |
| `bool` | `True` / `False` | Boolean values |
| `NoneType` | `None` | Null/empty value |

---

## 7. String Operations

Strings are sequences of characters and support various operations.

### Creating Strings
```python
s1 = "hello world !"
s2 = " i m learning python"
s3 = """we are looking at multiline string
chalo bye tke careokay bye """
```

### String Length
Use `len()` to find the length of a string:
```python
len(s2)  # Output: 20
```

### String Indexing
Access individual characters using their index position (0-based):

```python
s1[1]   # Output: 'e'  (second character)
s1[-1]  # Output: '!'  (last character)
s1[-4]  # Output: 'l'  (fourth from end)
```

**Indexing Diagram:**
```
String: h  e  l  l  o     w  o  r  l  d     !
Index:  0  1  2  3  4  5  6  7  8  9 10 11 12
Rev:  -13-12-11-10-9 -8 -7 -6 -5 -4 -3 -2 -1
```

### String Slicing
Extract a substring using `[start:end]` (end is exclusive):

```python
s1[1:4]  # Output: 'ell'  (characters at index 1, 2, 3)
```

**Slicing Syntax:**
```
string[start:end:step]
- start: starting index (inclusive)
- end: ending index (exclusive)
- step: increment (default is 1)
```

### String Concatenation (Joining)
Use the `+` operator to join strings:

```python
s1 + s2  
# Output: 'hello world ! i m learning python'

s1 + ' ' + s2 + ' ' + s3
# Output: 'hello world !  i m learning python we are looking at multiline string\nchalo bye tke careokay bye '
```

**String Methods Summary:**

| Method/Operation | Syntax | Description |
|------------------|--------|-------------|
| Length | `len(string)` | Returns number of characters |
| Index | `string[i]` | Access character at position i |
| Negative Index | `string[-i]` | Access character from end |
| Slice | `string[start:end]` | Extract substring |
| Concatenate | `string1 + string2` | Join strings |
| Upper | `string.upper()` | Convert to uppercase |
| Type | `type(string)` | Returns `<class 'str'>` |

---

## 8. Type Conversion and Type Casting

> [!TIP]
> This section is planned for future expansion with examples of converting between different data types (e.g., `int()`, `float()`, `str()`).

Type conversion allows you to convert values from one data type to another:

**Examples to be covered:**
- Converting strings to integers: `int("123")`
- Converting integers to strings: `str(123)`
- Converting to float: `float("12.5")`
- Converting to boolean: `bool(1)`

---

## Quick Reference Card

### Common String Operations
```python
# Create
s = "hello"

# Length
len(s)          # 5

# Access
s[0]            # 'h'
s[-1]           # 'o'

# Slice
s[1:4]          # 'ell'

# Join
s1 + s2         # concatenation

# Methods
s.upper()       # 'HELLO'
s.lower()       # 'hello'
```

### Common Variable Operations
```python
# Assign
x = 10

# Reassign
x = 20

# Delete
del x

# Check type
type(x)
```

### Boolean Logic
```python
True and True   # True
True and False  # False
True or False   # True
False or False  # False
not True        # False
```

---

## Practice Exercises

1. **Variables**: Create three variables with different data types and print their types
2. **String Manipulation**: Create a string, find its length, access the 3rd character, and slice the first 5 characters
3. **Boolean Logic**: Write expressions using `and`, `or`, and `not` operators
4. **String Concatenation**: Join multiple strings with spaces between them

---

## Additional Resources

- [Official Python Documentation](https://docs.python.org/3/)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python Data Types](https://docs.python.org/3/library/stdtypes.html)

---

