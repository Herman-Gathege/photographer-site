# 📸 Photographer Website CMS (Flask + HTML/CSS/JS)

A full-featured content-managed website for photographers — built with Flask (Python), HTML/CSS/JS, and SQLite/PostgreSQL support.  
This project allows the site owner to manage blog posts and client bookings via a secure admin dashboard.

---

## 🔧 Local Setup for Collaborators

### ✅ 1. Clone the Repo

```bash
git clone https://github.com/your-username/photographer-site.git
cd photographer-site/site/backend

# 📸 Photographer Website CMS (Flask + HTML/CSS/JS)

A full-featured content-managed website for photographers — built with Flask (Python), HTML/CSS/JS, and SQLite/PostgreSQL support.  
This project allows the site owner to manage blog posts and client bookings via a secure admin dashboard.

---

## 🔧 Local Setup for Collaborators

### ✅ 1. Clone the Repo

```bash
git clone https://github.com/your-username/photographer-site.git
cd photographer-site/site/backend
✅ 2. Create & Activate Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate
✅ 3. Install Python Dependencies
bash
Copy code
pip install -r requirements.txt
✅ 4. Set Environment Variables
Create a .env file in the backend folder:

env
Copy code
SECRET_KEY=your-secret-key
SQLALCHEMY_DATABASE_URI=sqlite:///../database/site.db
✅ 5. Initialize the Database
bash
Copy code
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
✅ 6. Run the App
bash
Copy code
export FLASK_APP=run.py
flask run
App will be available at: http://localhost:5000

✅ Features So Far
👤 Admin Authentication
Secure login/logout with Flask-Login

Password hashing

Only admin can access /admin routes

📝 Blog Management (Admin Dashboard)
Create, edit, and delete blog posts

Blog posts include title, content, slug, and date

CSRF protection on all forms

Admin interface built with Flask templates

📅 Booking System (Data Model Ready)
Users submit booking form (to be wired)

Admin sees/manage bookings from dashboard (coming soon)

🔒 Security
CSRF protection via Flask-WTF

Authenticated admin routes

.env support for secrets

📁 Project Structure Overview
bash
Copy code
photographer-site/
│
├── backend/
│   ├── app/
│   │   ├── models.py          # User, BlogPost, Booking models
│   │   ├── config.py          # Environment configuration
│   │   ├── routes/            # Route Blueprints (auth, admin, blog)
│   │   ├── templates/         # Jinja templates
│   │   ├── static/            # CSS/JS for admin views
│   │   └── forms/             # WTForms
│   ├── migrations/            # Flask-Migrate auto-generated
│   ├── run.py                 # Flask app entry point
│   ├── requirements.txt       # Dependencies
│   └── .env                   # (not tracked)
│
└── frontend/                  # Static front-facing HTML pages (coming soon)
🚧 Coming Soon
 Public-facing blog: /blog and /blog/<slug>

 Booking form connected to database

 Admin booking dashboard

 Portfolio image upload + gallery manager

 Deploy-ready structure (Render, Railway, etc.)

🤝 Contribution Guidelines
Use feature branches for each module (feature/blog-crud, feature/booking-admin, etc.)

Run flask db migrate & flask db upgrade after editing models

Keep commits clean and scoped to one feature

📝 License
This project is open-source and MIT-licensed.

