# FeatureList

A full-stack web application built with **Django (Python)** for the backend and **Next.js** for the frontend.

## 📂 Project Structure
```
FeatureList/
│
├── backend/           # Django backend
│   ├── features/      # App for managing features (API)
│   ├── db.sqlite3     # SQLite database
│   ├── manage.py      # Django management script
│
├── Frontend/          # Next.js frontend
│   ├── pages/         # Next.js pages
│   ├── public/        # Static assets
│   ├── package.json   # Frontend dependencies
│
├── venv/              # Python virtual environment (ignored in git)
└── README.md          # Project documentation
```

## 🚀 Tech Stack

**Frontend:**  
- Next.js
- React
- Tailwind CSS

**Backend:**  
- Django
- Django REST Framework
- django-cors-headers

**Database:**  
- SQLite (Development)
- PostgreSQL (Production-ready)

---

## 🔧 Setup Instructions

### 1️⃣ Backend (Django)
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 2️⃣ Frontend (Next.js)
```bash
cd Frontend
npm install
npm run dev
```

---

## 📌 Features
- API endpoints for feature management
- CORS enabled for Next.js frontend
- Responsive frontend with Tailwind CSS

---

## 📜 License
This project is licensed under the MIT License.
