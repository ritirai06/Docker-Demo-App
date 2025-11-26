

# Multiplication Tables Trainer

A simple and interactive Flask web application designed to help learners practice multiplication tables effectively. Users can choose any base number and a custom range, and the app instantly generates a clean, easy-to-read table along with a helpful study tip.

## Features

* Enter any positive integer to generate its multiplication table
* Adjustable range for personalized learning
* Clean, responsive HTML layout for better readability
* Motivational tip displayed with every table
* Lightweight and easy to run locally

## Getting Started

### **Prerequisites**

* Python 3.10+
* pip

### **Installation**

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### **Run the Application**

```bash
flask --app app run
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

## Project Structure

```
app.py
static/
    style.css
templates/
    base.html
    table.html
requirements.txt
```

## Customization Ideas

* Add random quizzes for self-testing
* Track user performance or learning streaks
* Export printable worksheets
* Provide themes or accessibility-friendly color modes

## License

This project is shared for educational use. You may modify and adapt it freely for your learning needs.
