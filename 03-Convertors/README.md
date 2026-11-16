# Day 03 – Flask URL Converters

## Overview

Learned about Flask URL converters, which allow us to capture values of specific data types from URLs.

## Concepts Learned

- String Converter
- Integer Converter
- Float Converter
- Path Converter

## 1. String Converter

Captures a string from the URL. It is the default converter when no converter is specified.

```python
@app.route('/user/<string:username>')
def user(username):
    return f"Username: {username}"
```

## 2. Integer Converter

Captures an integer value from the URL.

```python
@app.route('/user/<int:user_id>')
def user(user_id):
    return f"User ID: {user_id}"
```

## 3. Float Converter

Captures a floating-point number from the URL.

```python
@app.route('/price/<float:amount>')
def price(amount):
    return f"Price: {amount}"
```

## 4. Path Converter

Captures a string that can contain forward slashes, allowing us to capture multiple URL segments.

```python
@app.route('/files/<path:filename>')
def files(filename):
    return f"File path: {filename}"
```

## Implementation

Implemented different URL converters in `app.py` to understand how Flask captures and passes different types of values from URLs to Python functions.

## Key Takeaway

Understood how URL converters help validate and capture different types of data directly from URLs.
