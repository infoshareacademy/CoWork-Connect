# CoWork-Connect

CoWork-Connect is a Django-based web application designed for booking desks in a coworking space. This application allows users to view available desks, make reservations, and manage their bookings. The admin panel enables administrators to manage users, desks, reservations, contact information, terms of service, and the main page content.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Linux](#linux)
  - [Windows](#windows)
  - [Mac](#mac)
- [Importing Data](#importing-data)
- [Running the Application](#running-the-application)
- [Admin Panel](#admin-panel)
- [Usage](#usage)

## Prerequisites
- Python 3.10 or higher
- Celery 5.0.5 or higher
- Redis 3.5.3 or higher
- Git
- Virtualenv (recommended)

## Installation

### Linux

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/CoWork-Connect.git
    cd CoWork-Connect/Django-CoWork-Connect
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

### Windows

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/CoWork-Connect.git
    cd CoWork-Connect\Django-CoWork-Connect
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

### Mac

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/CoWork-Connect.git
    cd CoWork-Connect/Django-CoWork-Connect
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

## Importing Data

To import the initial set of desks, you need to run the `import_desk.py` script:

```bash
python manage.py runscript import_desk
```
## Running the Application

1. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

2. **Open another terminal and start the Celery worker:**
    ```bash
    celery -A CoWorkConnect worker --loglevel=info
    ```

## Admin Panel

The admin panel allows you to manage desks, users, reservations, contact information, terms of service, and the main page content.

1. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

2. **Access the admin panel:**

    Open your browser and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with your superuser credentials.

3. **Screenshots:**

    - Admin Login Page
    - Admin Dashboard
    - Managing Desks
    - Managing Users
    - Managing Reservations
    - Editing Contact Information
    - Editing Terms of Service
    - Editing Main Page Content

## Usage

1. **Home Page:**

    Unregistered and not logged-in users can view the home page and read about CoWork Connect.

    ![Home Page](screenshots/home_page.png)

2. **Offer Page:**

    Unregistered and not logged-in users can view available desks on the offer page.

    ![Offer Page](screenshots/offer_page.png)

3. **Registration and Login:**

    Users need to register and log in to make a reservation.

    ![Registration Page](screenshots/registration_page.png)
    ![Login Page](screenshots/login_page.png)

4. **Reservation:**

    After logging in, users can book a desk by selecting the desired time period.

    ![Reservation Form](screenshots/reservation_form.png)

5. **User Reservations:**

    Users can view their reservations on the 'My Reservations' page and cancel them if necessary.

    ![User Reservations Page](screenshots/user_reservations_page.png)

6. **Email Notifications:**

    Users receive email notifications upon registration, reservation, and cancellation.

    ![Email Confirmation](screenshots/email_confirmation.png)


