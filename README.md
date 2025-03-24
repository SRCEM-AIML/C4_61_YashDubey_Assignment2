# 🎓 StudentProject

A simple Django project with two apps (`app1` and `app2`) using static views and templates.

---

## 📚 Project Overview

- `app1` – Homepage with navigation links.
- `app2` – Sample page with project-related information.
- No database or models used, only static content.

---

## 🚀 How to Run the Project

# Clone the Repository
git clone https://github.com/YOUR_GITHUB_USERNAME/StudentProject.git
cd StudentProject

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
# OR
venv\Scripts\activate      # On Windows

# Install dependencies
pip install django

# Run the development server
python manage.py runserver

# Build Docker image
docker build -t studentproject .

# Run Docker container
docker run -p 8000:8000 studentproject

```bash
