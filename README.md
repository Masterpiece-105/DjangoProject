# DjangoProject

Django Advance Blog Project built using Django. This project allows users to create, edit, and manage blog posts with authentication and media support.

---

# Features

* User Registration and Login
* Create, Update, Delete Blog Posts
* Media/Image Upload Support
* Admin Panel
* Responsive UI
* SQLite Database
* Ready for Deployment on Render

---

# Tech Stack

* Python 3
* Django
* HTML, CSS, Bootstrap, Tailwind css
* SQLite3
* Gunicorn
* Whitenoise

---

# Project Structure

```text
DjangoProject/
│
├── blog/
├── config/
├── media/
├── manage.py
├── requirements.txt
├── build.sh
├── Procfile
└── README.md
```

---

# Installation

 1. Clone the Repository

```bash
git clone https://github.com/your-username/DjangoProject.git
cd DjangoProject
```

 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

# Windows

```bash
venv\Scripts\activate
```

# Linux / Mac

```bash
source venv/bin/activate
```

---

 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

 4. Apply Migrations

```bash
python manage.py migrate
```

---

 5. Create Superuser

```bash
python manage.py createsuperuser
```

---

 6. Run the Project

```bash
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

---

# Environment Variables

If you are using production deployment, create a `.env` file:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

# Deployment on Render

This project can be deployed for free on Render.

Required files:

* `requirements.txt`
* `build.sh`
* `Procfile`

Build Command:

```text
./build.sh
```

Start Command:

```text
gunicorn config.wsgi
```



# Future Improvements

* Add User Profile Page
* Add Comment System
* Add Search Functionality
* Add Categories and Tags
* Use PostgreSQL in Production

---

# Author

Shubham Yadav

GitHub: [https://github.com/Masterpiece-105](https://github.com/Masterpiece-105)

---

# License

This project is open source and available under the MIT License.
