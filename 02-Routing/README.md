# Day 02 – Flask Routing

## Overview

Learned how Flask handles URLs through routing and how different URLs can be mapped to specific Python functions.

## Concepts Learned

- Flask Routing
- Static Routing
- Dynamic Routing

## 1. Static Routing

Static routing maps a fixed URL to a specific Python function.

For example:

```python
@app.route('/home')
def home():
    return "Welcome to Home Page"
```

Whenever a user visits `/home`, Flask executes the associated function.

## 2. Dynamic Routing

Dynamic routing allows us to capture values directly from a URL and pass them as arguments to a Python function.

For example:

```python
@app.route('/user/<username>')
def user(username):
    return f"Welcome {username}"
```

```python
@app.route('/student/<username>/<course>')
def student(username,course):
    return f"Welcome {username} to {course}"
```

Visiting `/user/Termi` passes `Termi` as the `username` argument.
Visiting `/student/Termi/Flask` passes `Termi` as the `username` and `Flask` as `course`argument.

## Implementation

Implemented static and dynamic routes in `app.py` to understand how Flask maps URLs to Python functions.

## Key Takeaway

Understood how Flask handles incoming URLs and how dynamic routing allows applications to work with values provided through URLs.
