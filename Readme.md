# FastAPI🚀

This repository demonstrates how to build a **FastAPI web application** using core Python concepts, **Pydantic models**, and **template rendering** with HTML and CSS. It's a great starting point to understand how FastAPI handles routing, validation, and frontend integration.

---

## 📁 Project Structure

```
v41bh4vr4jput-fastapi/
├── Readme.md                  # Project documentation
├── app.py                     # Alternate app runner file
├── index.py                   # Route definitions and logic
├── main.py                    # Main entry point for FastAPI server
├── Pydantic_models.py         # Data validation models using Pydantic
├── PythonTypes.py             # Examples demonstrating FastAPI with Python types
├── static/
│   └── style.css              # Styling for the HTML template
└── templates/
    └── index.html             # Jinja2 template rendered on the frontend
```

---

## 🚀 Features

* 📦 **FastAPI Server** – Lightweight, fast web framework using ASGI
* ✅ **Data Validation** – Leverages **Pydantic** for request/response validation
* 🧠 **Python Type Hints** – Demonstrates strong typing in API parameters and return values
* 🎨 **HTML Template Rendering** – Uses Jinja2 templates to build frontend
* 💅 **Static Files Support** – Integrates CSS for styling

---

## 🛠️ How to Run the App

### Step 1: Install Dependencies

```bash
pip install fastapi uvicorn jinja2
```

### Step 2: Start the FastAPI Server

```bash
uvicorn main:app --reload
```

### Step 3: Open in Browser

Navigate to:

```
http://127.0.0.1:8000/
```

To access the **interactive API docs**:

```
http://127.0.0.1:8000/docs
```

---

## 📄 File Descriptions

* `main.py` – Entry point with `FastAPI()` instance and route mounting
* `index.py` – Contains route logic and request handling
* `Pydantic_models.py` – Defines models for request validation
* `PythonTypes.py` – Demonstrates FastAPI capabilities with Python's built-in type annotations
* `app.py` – Alternate run file for experimentation or development
* `templates/index.html` – Basic HTML page rendered by FastAPI using Jinja2
* `static/style.css` – CSS file linked to the HTML template

---


