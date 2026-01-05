## Views & URLs Basics

### Topics Covered

* Introduction to Views & URLs
* Create a Simple View
* Configure URLs in App
* Link App URLs in Project
* Final Output

---

## What is a View?

A **View** can be a **function** or a **class**.
It handles the request and returns a response.

---

## Step 1: Create a Django Project

```bash
django-admin startproject URL_Views
```

---

## Step 2: Create an App

```bash
python manage.py startapp blog
```

---

## Step 3: Create a Function-Based View

Go inside:

```
blog/views.py
```

Add a simple view and required import:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi Welcome to my blog home page")
```

---

## Step 4: Configure URLs (Project Level)

Go to:

```
URL_Views/urls.py
```

Import the view and create routes:

```python
from django.contrib import admin
from django.urls import path
from blog.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', home, name="home"),
]
```

---

## Step 5: Register App in Settings

Go to:

```
URL_Views/settings.py
```

Add your app inside `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',
]
```

---

## Final Output

Open browser and visit:

```
http://127.0.0.1:8000/blog/
```

You will see:

```
Hi Welcome to my blog home page
```

---
