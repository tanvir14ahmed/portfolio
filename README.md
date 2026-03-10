# 🚀 Professional Django Portfolio - Tanvir Ahmed Joy

A modern, high-performance, and visually stunning portfolio website built with **Django 5.2**. Designed for AI/ML developers and full-stack engineers.

![Portfolio Preview](https://raw.githubusercontent.com/tanvir14ahmed/portfolio/main/main/static/images/profile.jpg)

## ✨ Features

- **Soothing UI/UX**: Dark-teal theme with premium cubic-bezier transitions and blur effects.
- **Dynamic Content**: Manage Skills, Projects, Blog, and Testimonials via Django Admin.
- **AJAX Contact Form**: Instant message delivery with real-time validation.
- **Pre-generated Resume**: Easy static PDF download functionality.
- **Responsive Design**: Optimized for all devices (Mobile, Tablet, Desktop).
- **SEO Optimized**: Semantic HTML5 and meta-tag structures.

## 🛠️ Tech Stack

- **Backend**: Django 5.2, Python 3.12
- **Frontend**: Vanilla HTML5, CSS3 (Glassmorphism), JavaScript (ES6)
- **Database**: PostgreSQL (Production), SQLite (Development)
- **Styling**: Custom CSS with smooth scroll and reveal animations
- **Production**: Gunicorn, WhiteNoise, CPanel (Git-hooks)

## 📂 Project Structure

```bash
├── main/               # Main Portfolio App
│   ├── static/         # CSS, JS, Images, and Resume PDF
│   ├── templates/      # HTML Templates
│   ├── models.py       # DB Schema (Skill, Project, Blog, etc.)
│   └── views.py        # Logic for AJAX and Page Loading
├── portfolio_project/  # Project Settings
└── requirements.txt    # Dependencies
```

## 🚀 Local Setup

1. **Clone the repo**:
   ```bash
   git clone https://github.com/tanvir14ahmed/portfolio.git
   cd portfolio
   ```

2. **Setup Virtual Environment**:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start Server**:
   ```bash
   python manage.py runserver
   ```

## 🌐 Deployment (CPanel)

This project is configured for direct **GitHub to CPanel deployment**. 

1. Ensure your CPanel supports Python Apps (Phusion Passenger).
2. Configure your `passenger_wsgi.py` in the root.
3. Use the `.cpanel.yml` for automated file deployment.

## 📄 License

Author: **Tanvir Ahmed Joy**
Contact: [tanvir14ahmed@gmail.com](mailto:tanvir14ahmed@gmail.com)
