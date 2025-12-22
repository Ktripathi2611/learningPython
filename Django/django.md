# Module: Django – Detailed Notes with Examples

---

## 1. Introduction to Django

Django is a high-level Python web framework that enables rapid development of secure and maintainable web applications. It follows the **MVT (Model–View–Template)** architecture.

### Key Features

* Fast development
* Built-in admin panel
* ORM (Object Relational Mapper)
* Secure by default (CSRF, SQL injection protection)
* Scalable

---

## 2. Install Django

### Install using pip

```bash
pip install django
```

### Verify installation

```bash
django-admin --version
```

---

## 3. Django Project Structure

After creating a project, the structure looks like:

```text
myproject/
│── manage.py
│── myproject/
│   │── __init__.py
│   │── settings.py
│   │── urls.py
│   │── asgi.py
│   │── wsgi.py
```

### Purpose

* `manage.py`: Command-line utility
* `settings.py`: Configuration
* `urls.py`: URL routing
* `wsgi.py / asgi.py`: Deployment

---

## 4. Creating a New Django Project

```bash
django-admin startproject myproject
cd myproject
```

---

## 5. Understanding the Django Project

Django separates:

* **Project**: Overall configuration
* **Apps**: Functional modules (blog, users, etc.)

---

## 6. Start the Development Server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

## 7. Django Apps

Create an app:

```bash
python manage.py startapp blog
```

Register app in `settings.py`:

```python
INSTALLED_APPS = [
    'blog',
]
```

---

## 8. URLs & Views

### View (`views.py`)

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django")
```

### URL (`urls.py`)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]
```

---

## 9. Building a Blog Website

Main components:

* Posts
* Authors
* Comments
* Templates
* Static files

---

## 10. Adding Home Page and Other URLs & Views

```python
path('about/', views.about)
```

---

## 11. Dynamic Path Segments

```python
path('post/<id>/', views.post_detail)
```

---

## 12. Path Converters

```python
path('post/<int:id>/', views.post_detail)
```

Common converters:

* `int`
* `str`
* `slug`
* `uuid`

---

## 13. Slugs

Slug is URL-friendly text.

```python
path('post/<slug:slug>/', views.post_detail)
```

---

## 14. Returning HTML Content as Response

```python
return HttpResponse('<h1>Hello</h1>')
```

---

## 15. Making the Code More Dynamic

```python
def home(request):
    return HttpResponse(f"Time: {datetime.now()}")
```

---

## 16. Named URLs & `reverse()`

```python
path('posts/', views.posts, name='posts')
```

```python
from django.urls import reverse
reverse('posts')
```

---

## 17. Introduction to Templates

Templates separate HTML from Python logic.

---

## 18. Creating & Using Templates

```html
<h1>{{ title }}</h1>
```

---

## 19. Registering Templates

```python
TEMPLATES = [{
    'DIRS': [BASE_DIR / 'templates'],
}]
```

---

## 20. Rendering Templates – Best Practice

```python
from django.shortcuts import render

return render(request, 'home.html', context)
```

---

## 21–22. DTL & Variable Injection

```html
<p>{{ post.title }}</p>
```

---

## 23. Template Filters

```html
{{ post.title|upper }}
```

Common filters:

* `upper`
* `lower`
* `length`
* `truncatechars`

---

## 24. Template Tags – `for`

```html
{% for post in posts %}
  {{ post.title }}
{% endfor %}
```

---

## 25. URL Tag

```html
<a href="{% url 'post-detail' post.slug %}">Read</a>
```

---

## 26. The `if` Tag

```html
{% if posts %}
  Available
{% else %}
  No posts
{% endif %}
```

---

## 27–28. Template Inheritance

### Base Template

```html
{% block content %}{% endblock %}
```

### Child Template

```html
{% extends 'base.html' %}
{% block content %}
<h1>Home</h1>
{% endblock %}
```

---

## 29–30. Include Tag

```html
{% include 'includes/header.html' %}
```

---

## 31. 404 Template

Create:

```text
templates/404.html
```

---

## 32–33. Static Files

```bash
STATIC_URL = '/static/'
```

```html
{% load static %}
<link rel="stylesheet" href="{% static 'style.css' %}">
```

---

## 34–36. Adding Content & Images

```html
<img src="{% static 'images/post.jpg' %}">
```

---

## 37–43. Dynamic Blog Pages

Use:

* Context dictionaries
* Slugs
* URL generation

---

## 44. Data & Models

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
```

---

## 45. Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 46–47. Relationships

```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
```

---

## 48–50. Admin Panel

```python
admin.site.register(Post)
```

---

## 51. Auto-populating Slug Field

```python
slug = models.SlugField(unique=True)
```

---

## 52–54. Querying Data

```python
Post.objects.all()
Post.objects.filter(title__icontains='django')
```

---

## 55–58. Forms

```python
class CommentForm(forms.Form):
    text = forms.CharField()
```

---

## 59. CSRF Token

```html
{% csrf_token %}
```

---

## 60–62. Handling Submitted Data

```python
if request.method == 'POST':
    form = CommentForm(request.POST)
```

---

## 63. Displaying Comments

```html
{% for comment in comments %}
  {{ comment.text }}
{% endfor %}
```

---

## 64. Handling Comments via Admin & Conclusion

Django provides a complete ecosystem for building production-ready web applications with minimal effort and clean architecture.

---

**End of Module  – Django**
