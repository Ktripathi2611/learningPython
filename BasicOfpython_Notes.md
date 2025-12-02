# 🐍 Interactive Python Basics Guide

**Welcome!** This guide is designed to be interactive. Use the checkboxes to track your progress and click the arrows (▶) to reveal answers and solutions.

---

## 📋 Table of Contents
1. [Foundations (Literals, Variables, Keywords)](#1-foundations)
2. [Data Types & Type Casting](#2-data-types--casting)
3. [Strings & Input/Output](#3-strings--inputoutput)
4. [Operators & Math](#4-operators--math)
5. [Coding Challenges](#5-coding-challenges)

---

## 1. Foundations
*Covers: Literals, Variables, Keywords*

### 📚 Core Concepts
* **Literals:** Raw data like `25`, `"Hello"`, `25.5`.
* **Variables:** Containers to store data. Created on assignment (e.g., `x = 5`).
* **Keywords:** Reserved words (like `if`, `while`, `True`) you cannot use as variable names.

### 🧠 Quick Quiz
**Q1:** What happens if you run `del b` and then try to `print(b)`?

<details>
<summary>▶ Click to reveal answer</summary>

> **Error!** It raises a `NameError` because the variable `b` is deleted from memory.
</details>

**Q2:** Can you name a variable `class`?

<details>
<summary>▶ Click to reveal answer</summary>

> **No.** `class` is a reserved keyword in Python.
</details>

### ✅ Progress Check
- [ ] I understand what a Literal is.
- [ ] I know how to assign and delete variables.
- [ ] I know how to view keywords using `import keyword`.

---

## 2. Data Types & Casting
*Covers: Primitives, Type Conversion (Int, Float, Bool)*

### 📚 Core Concepts
| Type | Description | Example |
| :--- | :--- | :--- |
| `int` | Whole numbers | `age = 25` |
| `float` | Decimal numbers | `price = 25.5` |
| `str` | Text | `name = "sachin"` |
| `bool` | Logical | `True`, `False` |

### 🧪 Experiment: Truthy vs Falsy
Guess the output of `bool()` for the following values:

1. `bool(0)`
2. `bool("Hello")`
3. `bool("")`
4. `bool(None)`

<details>
<summary>▶ Click to see results</summary>

1. `False`
2. `True`
3. `False` (Empty strings are Falsy)
4. `False`
</details>

### ✅ Progress Check
- [ ] I can identify `int`, `float`, and `str`.
- [ ] I understand how to use `int()` and `str()` to convert data.

---

## 3. Strings & Input/Output
*Covers: Print, Input, Indexing, Slicing*

### 📚 Core Concepts
* **Printing:** `print("Hello")` or `print('''Multi-line''')`.
* **Indexing:** `s[0]` is the first char. `s[-1]` is the last.
* **Slicing:** `s[start:end]` (End is excluded!).

### 🧩 Puzzle: String Slicing
Given: `s1 = "hello world !"`

**Q1:** What does `s1[1:4]` output?
<details>
<summary>▶ Reveal Answer</summary>

`'ell'`
*(It takes index 1, 2, and 3. It stops before 4.)*
</details>

**Q2:** What does `s1[-1]` output?
<details>
<summary>▶ Reveal Answer</summary>

`'!'`
*(Negative indexing starts from the end.)*
</details>

### ✅ Progress Check
- [ ] I can use `input()` to get user data.
- [ ] I understand that `input()` always returns a **string**.
- [ ] I can slice a string using `[:]`.

---

## 4. Operators & Math
*Covers: Arithmetic, Comparison, Logical, Precedence*

### 📚 Core Concepts
* **Math:** `+`, `-`, `*`, `/`, `//` (Floor Div), `%` (Remainder), `**` (Power).
* **Logic:** `and` (Both true), `or` (One true), `not` (Reverse).
* **Precedence:** Parentheses `()` first, then Power `**`, then Mult/Div, then Add/Sub.

### 🧮 Math Challenge
Calculate the result of these expressions in your head, then check:

**Expression A:** `True and False`
<details>
<summary>▶ Answer</summary>
`False`
</details>

**Expression B:** `10 // 3`
<details>
<summary>▶ Answer</summary>
`3` (Floor division removes the decimal)
</details>

**Expression C:** `5 + 2 * 3`
<details>
<summary>▶ Answer</summary>
`11` (Multiplication happens before Addition!)
</details>

### ✅ Progress Check
- [ ] I know the difference between `/` and `//`.
- [ ] I understand logical `and` vs `or`.

---

## 5. Coding Challenges
*Write code to solve these problems. Check the solution only after trying!*

### 🟢 Challenge 1: The Greeter
**Task:** Ask the user for their name and age. Print a message saying: "Hello [Name], next year you will be [Age+1]."

<details>
<summary>▶ Show Solution Code</summary>

```python
name = input("Enter your name: ")
age = input("Enter your age: ")

# Critical Step: Convert age to int!
age_int = int(age) 

print("Hello", name, "next year you will be", age_int + 1)