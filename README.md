# Django Calculator Project

This project is a web-based calculator built with Django. It features a modern design and supports basic arithmetic operations, powers, square roots, Pi, and trigonometric functions (sine, cosine, tangent).

## Features

-   **Basic Arithmetic:** Addition, subtraction, multiplication, division.
-   **Advanced Operations:** Power (`pow(x,y)`), Square Root (`sqrt(x)`).
-   **Constants:** Pi (`pi`).
-   **Trigonometric Functions:** Sine (`sin(x)`), Cosine (`cos(x)`), Tangent (`tan(x)`).
    *   **Note:** Trigonometric functions expect input in **radians**.
-   **User-friendly Interface:** Clean and responsive web interface.
-   **Error Handling:** Displays "Error" for invalid expressions or mathematical errors.

## Technologies Used

-   **Backend:** Django (Python Web Framework)
-   **Expression Evaluation:** `asteval` library (for safe mathematical expression evaluation)
-   **Frontend:** HTML, CSS, JavaScript (for interactive UI and asynchronous communication)

## Setup and Installation

Follow these steps to set up and run the project locally:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Kilbka68/test-gemini.git
    cd test-gemini
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install Django asteval
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start the Django development server:**
    ```bash
    python manage.py runserver
    ```

6.  **Access the calculator:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Project Structure

```
.
├── mycalculatorproject/        # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Project settings
│   ├── urls.py               # Project URL configurations
│   └── wsgi.py
├── calculator_app/             # Django application for the calculator
│   ├── migrations/
│   ├── static/               # Static files (CSS, JS)
│   │   └── calculator_app/
│   │       ├── script.js
│   │       └── style.css
│   ├── templates/            # HTML templates
│   │   └── calculator_app/
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py              # Application views (logic for pages and API)
├── manage.py                   # Django's command-line utility
└── README.md                   # Project documentation
```

## Usage

-   Click the number and operator buttons to build your expression in the display.
-   Use `C` to clear the display.
-   Use `<--` to delete the last character.
-   Click `=` to evaluate the expression.
-   Functions like `sin(`, `cos(`, `tan(`, `sqrt(`, `pow(` require you to input the argument(s) inside the parentheses.
    -   Example: `sin(pi/2)`, `sqrt(81)`, `pow(2,3)`

## Contributing

Feel free to fork the repository and submit pull requests.