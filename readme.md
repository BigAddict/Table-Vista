# Table-Vista

The Table Banking System is a feature-rich Django web application created to oversee and simplify financial transactions in a neighborhood-based table banking program. This project addresses the financial needs of community members by offering a centralized platform to handle savings accounts, loan accounts, meeting minutes, and educational blogs.
The primary purpose of the Table Banking System is to empower community members with financial tools and knowledge, fostering economic growth and financial well-being.

## Table of Contents

- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
  - [How to Use](#how-to-use)
  - [Running the Development Server](#running-the-development-server)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Built With](#built-with)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

The Table Banking System is a comprehensive web application built using Django that serves as a financial management platform for a community-based table banking initiative. This project efficiently manages various aspects of financial activities and community engagement.

### Installation

Before you begin with the installation and usage of the Table Banking System, make sure you have the following prerequisites in place:

1. **Python:**
    - Ensure that Python is installed on your system. You can download Python from python.org. I personally used `Python 3.10.0rc2`
2. **Virtual Environment (Optional but Recommended):**
    - It is a good practice to use a virtual environment to isolate your project dependencies. Create a virtual environment using:
        ```bash
        # Replace myenv with the name for your enviroment
        python -m venv myenv
        ```
    - Activate the virtual enviroment:
        - On windows:
            ```bash
            # Replace myenv with the name of your enviroment
            myenv\Scripts\activate
            ```
        - On macOS/Linux
            ```bash
            # Replace myenv with the name of your enviroment
            source myenv/bin/activate
            ```
3. **Dependency packages:**
    - Install project-specific dependencies using the requirements file:
        ```bash
        pip install -r requirements.txt
        ```
4. **Database setup:**
    - Set up the database by running Django migrations:
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```
5. Static Files:
    - Collect static files for serving:
        ```bash
        python manage.py collectstatic
        ```
6. Django Superuser (Admin User):
    - Create a superuser for the Django admin panel:
        ```bash
        python manage.py createsuperuser
        ```

## Usage

### How to Use

- **User Registration and Authentication:**
    - Users can register accounts and log in securely.
    - Authentication ensures secure access to personal financial data.
- **Savings and Loan Management:**
    - Users can create, view, and manage their saving and loan accounts.
    - Intuitive interfaces for depositing, withdrawing, and applying for loans
- **Meeting Minutes:**
    - Access records of community meetings, decisions, and discussions.
    - Stay informed about community initiatives and decisions.

- **Educational Blogs:**
    -Read and engage with educational blog posts for financial literacy.
    -Empower community members with knowledge to make informed financial decisions.

## Contributing:

- Contributions are not yet allowed since i have not completed developing the website yet.

## License:

- This project is licenced under the <a href="LICENSE">MIT LICENSE</a>

### **Running the Development Server:**
    ```bash
    # Command to run the development server
    python manage.py runserver
    ```
