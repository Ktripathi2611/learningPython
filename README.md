# Python Learning Hub

Comprehensive hierarchical map and documentation for the Python Learning Hub workspace.

---

## Table of Contents

- Overview
- Tree Diagram
- Directory Documentation
  - ABasic_notes
  - AdvancePython
  - Assignments
  - AUTOMATION WITH SELENIUM
  - ChatApp
  - DataAnalysis
  - MachineLearning
  - Dev-ops
  - flask
  - Open CV
  - postgresql
  - project-automatic-facebook-poster
  - RestApi
  - SystemDesign
  - webScrapping
- Dependencies & Environment Setup
- Inter-Directory Dependencies
- Contributing & Best Practices

---

## Overview

This repository is a structured collection of Python learning materials, example projects, and experiments grouped by topic. It is intended as a learner-friendly workspace that spans fundamentals, intermediate topics, and practical projects (web, automation, data analysis, computer vision, and system design).

Recommended Python: 3.8+

---

## Tree Diagram

```
learningPython/
├── ABasic_notes/
│   ├── BasicOfpython.ipynb
│   ├── basicOfPython2.ipynb
│   ├── basicOfPython3.ipynb
│   ├── basicOfPython4.ipynb
│   ├── basicOfPython5.ipynb
│   ├── basicOfPython6.ipynb
│   ├── basicOfpython7.ipynb
│   ├── BasicOfpython_Notes.md
│   ├── FileHandling/
│   │   ├── fileHandling.ipynb
│   │   ├── demo.txt
│   │   ├── test.txt
│   │   ├── practice.txt
│   │   ├── user.json
│   │   └── data.pkl
│   └── Userdefine_module/
│       ├── arithmatic.py
│       └── mycode.py
├── AdvancePython/
│   ├── ObjectOrientedProgramming/BasicOfoop.ipynb
│   ├── RegularExpression/RegularExpression.ipynb
│   └── Tkinter/
│       ├── tkinter.ipynb
│       ├── calculator.py
│       └── Tkinter.md
├── Assignments/
│   ├── Assignment1.ipynb
│   ├── Assignment2.ipynb
│   ├── Assignment3.ipynb
│   ├── Assignment4.ipynb
│   ├── Assignment5.ipynb
│   └── Assignment6.py
├── AUTOMATION WITH SELENIUM/automation.py
├── ChatApp/
│   ├── server.py
│   └── client.py
├── DataAnalysis/DataAnalysis_Complete.ipynb
├── MachineLearning/
│   ├── Matplotlib_Notes.ipynb
│   ├── Matplotlib_Notes.md
│   ├── NumPy_Notes.ipynb
│   ├── NumPy_Notes.md
│   ├── Pandas_Notes.ipynb
│   ├── Pandas_Notes.md
│   └── LinearReggression/LinearRegression.ipynb
├── Dev-ops/
│   ├── dev-ops2.pdf
│   ├── grade_checker.py
│   ├── student_grades.py
│   ├── write_file.py
│   ├── read_file.py
│   └── output.txt
├── flask/
│   ├── app.py
│   ├── requirements.txt
   │   ├── static/style.css
│   └── template/
       ├── base.html
       ├── home.html
       ├── index.html
       ├── second.html
       ├── register.html
       ├── confirmation.html
       ├── login.html
       ├── login_success.html
       ├── gallery.html
       └── upload.html
├── Open CV/
│   ├── 01_setup_and_io.py
│   ├── 02_resize_and_flip.py
│   ├── 03_morphology.py
│   ├── 04_draw_transform.py
│   ├── 05_threshold_and_blur.py
│   ├── 06_edges.py
│   ├── 07_video_io.py
│   ├── 08_webcam.py
│   ├── requirements.txt
│   ├── README.md
│   ├── sample.jpg
│   └── output.jpg
├── postgresql/
│   ├── postgresql_1.py
│   ├── postgresql_2.py
│   ├── postgresql_3.py
│   ├── postgresql_4.py
│   └── postgresql_5.py
├── project-automatic-facebook-poster/facebook.py
├── RestApi/
│   └── blog/
│       ├── manage.py
│       ├── db.sqlite3
│       ├── blog/
│       │   ├── settings.py
│       │   ├── urls.py
│       │   ├── wsgi.py
│       │   └── asgi.py
│       └── helloworld/
│           ├── admin.py
│           ├── apps.py
│           ├── models.py
│           ├── permissions.py
│           ├── serializers.py
│           ├── tests.py
│           ├── views.py
│           └── migrations/
├── SystemDesign/
│   ├── README.md
│   ├── requirements.txt
│   ├── task1_url_shortener/app.py
│   ├── task1_url_shortener/urls.db
│   ├── task2_rate_limiter/app.py
│   └── task3_load_balancer/
│       ├── load_balancer.py
│       ├── server1.py
│       ├── server2.py
│       └── server3.py
└── webScrapping/pricetracker.py
```

---

## Directory Documentation

Below each top-level directory is documented with: Name & Purpose, Key Files, Dependencies, and Usage Notes.

### `ABasic_notes` — Python Fundamentals

Purpose: Foundational notebooks and simple examples to learn Python basics, file handling, and how to build modules.

Key Files:

| File                            | Description                                        |
| ------------------------------- | -------------------------------------------------- |
| BasicOfpython.ipynb             | Introductory notebook: variables, types, operators |
| BasicOfpython_Notes.md          | Quick-reference notes                              |
| FileHandling/fileHandling.ipynb | File I/O examples (text, JSON, pickle)             |
| Userdefine_module/arithmatic.py | Small utility module for arithmetic functions      |

Dependencies: none special; use `jupyter` for notebooks.

Usage:

```bash
pip install jupyter
jupyter notebook ABasic_notes/
```

---

### `AdvancePython` — Advanced Python Topics

Purpose: Intermediate topics including OOP, regex, and GUI programming with Tkinter.

Key Files:

| File                                       | Description                  |
| ------------------------------------------ | ---------------------------- |
| ObjectOrientedProgramming/BasicOfoop.ipynb | OOP patterns and examples    |
| RegularExpression/RegularExpression.ipynb  | Regex patterns and exercises |
| Tkinter/calculator.py                      | GUI calculator demo          |

Dependencies: none beyond standard library for OOP/regex; Tkinter is included with most Python installs.

Run the calculator:

```bash
python AdvancePython/Tkinter/calculator.py
```

---

### `Assignments`

Purpose: Practice assignments and exercises to reinforce learning.

Key Files: `Assignment1.ipynb` → `Assignment5.ipynb`, `Assignment6.py`

Usage: open notebooks and run cells sequentially.

---

### `AUTOMATION WITH SELENIUM`

Purpose: Selenium automation examples.

Key Files: `automation.py` — automates browser tasks.

Dependencies: `selenium`, appropriate WebDriver (ChromeDriver/GeckoDriver).

---

### `ChatApp`

Purpose: Simple TCP chat server and a Tkinter client demonstrating sockets and threading.

Key Files:

| File      | Description             |
| --------- | ----------------------- |
| server.py | Multi-client TCP server |
| client.py | Tkinter GUI client      |

Run:

```bash
python ChatApp/server.py
python ChatApp/client.py
```

---

### `DataAnalysis`

Purpose: End-to-end data analysis notebook.

Key Files: `DataAnalysis_Complete.ipynb` — data cleaning, visualization, stats.

Dependencies: `pandas`, `numpy`, `matplotlib`, `seaborn`.

Install:

```bash
pip install pandas numpy matplotlib seaborn
```

---

### `MachineLearning`

Purpose: Introductory notes and examples for NumPy, Matplotlib, and Pandas; a simple linear regression notebook.

Key Files:

| File                                         | Description                         |
| -------------------------------------------- | ----------------------------------- |
| NumPy_Notes.ipynb / NumPy_Notes.md           | NumPy fundamentals and examples     |
| Matplotlib_Notes.ipynb / Matplotlib_Notes.md | Plotting and visualization examples |
| Pandas_Notes.ipynb / Pandas_Notes.md         | Dataframes, grouping, aggregation   |
| LinearReggression/LinearRegression.ipynb     | Small linear regression example     |

Dependencies: `numpy`, `pandas`, `matplotlib`.

---

### `Dev-ops`

Purpose: Scripts demonstrating basic DevOps-style automation and file I/O.

Key Files: `grade_checker.py`, `student_grades.py`, `read_file.py`, `write_file.py`.

Usage: run scripts directly; `write_file.py` writes `output.txt` which `read_file.py` reads.

---

### `flask`

Purpose: Example Flask application demonstrating templates, static assets, forms, file upload, and routing.

Key Files:

| File             | Description                                |
| ---------------- | ------------------------------------------ |
| app.py           | Main app; demonstrates many Flask patterns |
| requirements.txt | Dependencies for the Flask app             |
| template/        | Jinja2 templates for pages                 |
| static/          | CSS and images used by the app             |

Run:

```bash
cd flask
pip install -r requirements.txt
python app.py
# Visit http://127.0.0.1:5000
```

---

### `Open CV`

Purpose: Computer vision scripts using OpenCV and NumPy.

Key Files: `01_setup_and_io.py` ... `08_webcam.py`, `requirements.txt`, `README.md`.

Install:

```bash
cd "Open CV"
pip install -r requirements.txt
python 01_setup_and_io.py
```

---

### `postgresql`

Purpose: PostgreSQL examples using `psycopg2`.

Key Files: `postgresql_1.py` → `postgresql_5.py`.

Prerequisites: Running PostgreSQL server; update DB credentials in scripts before running.

Install:

```bash
pip install psycopg2-binary
```

---

### `project-automatic-facebook-poster`

Purpose: Selenium-based automation for posting to Facebook (educational/demo).

Key Files: `facebook.py`.

Warning: Automating social platforms may violate terms of service; use for learning only.

Dependencies: `selenium`, `webdriver-manager`.

---

### `RestApi` (Django REST Framework)

Purpose: A small Django + DRF blog API demonstrating models, serializers, views, permissions, and migrations.

Key Files: `manage.py`, `db.sqlite3`, `blog/settings.py`, `helloworld/*`.

Run (example):

```bash
cd RestApi/blog
pip install django djangorestframework
python manage.py runserver
```

---

### `SystemDesign`

Purpose: Mini-projects for system design concepts: URL shortener, rate limiter, and load balancer.

Key Files: `task1_url_shortener/app.py`, `task2_rate_limiter/app.py`, `task3_load_balancer/load_balancer.py` and servers.

Run examples are included in that directory's `README.md`.

---

### `webScrapping`

Purpose: Web scraping examples using `requests` and `BeautifulSoup`.

Key Files: `pricetracker.py` — Amazon price-tracking example.

Dependencies: `requests`, `beautifulsoup4`.

---

## Dependencies & Environment Setup

Most subprojects include their own `requirements.txt` (e.g., `flask/requirements.txt`, `Open CV/requirements.txt`, `SystemDesign/requirements.txt`). For notebooks, install `jupyter` and the standard data stack.

Suggested global setup:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r flask/requirements.txt
pip install -r "Open CV"/requirements.txt
pip install jupyter pandas numpy matplotlib seaborn requests beautifulsoup4
```

Automated commands vary by OS; the examples above target Windows (adjust activation for macOS/Linux).

---

## Inter-Directory Relationships

- `ABasic_notes` provides foundational examples used throughout the repo.
- `AdvancePython` builds on fundamentals and is reused by `ChatApp`, `flask`, and `RestApi` examples.
- `AUTOMATION WITH SELENIUM` patterns are shared with `project-automatic-facebook-poster`.

---

## Contributing & Best Practices

- Follow PEP 8 and use descriptive commit messages (e.g., `feat:`, `fix:`, `docs:`).
- Add `requirements.txt` and a `README.md` for new directories.
- Clear Jupyter outputs before committing.

---

If you want, I can:

- Run quick dependency checks for each subproject (pip install dry-run)
- Add a `docs/` folder and split per-project READMEs into it
- Create CI checks (linting, notebook clearing) for the workspace

Happy to continue — tell me which of the follow-ups you want next.
