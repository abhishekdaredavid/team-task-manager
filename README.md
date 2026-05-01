# Team Task Manager 🚀

A full-stack web application designed for seamless team collaboration, project tracking, and role-based task management. 

## 🌟 Features
- **Role-Based Access Control (RBAC):** Distinct dashboards for 'Admin' and 'Member' roles.
- **Secure Authentication:** JWT (JSON Web Tokens) based login with pure Bcrypt password hashing (Python 3.13 compatible).
- **Admin Capabilities:** Create new projects and assign tasks to specific team members.
- **Member Capabilities:** View assigned tasks and track personal workload.
- **Seamless Integration:** CORS enabled frontend-backend communication.
- **Responsive UI:** Clean and minimal interface built with Tailwind CSS.

## 🛠️ Tech Stack
- **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript (Fetch API)
- **Backend:** FastAPI (Python 3.13)
- **Database:** SQLite with SQLAlchemy ORM
- **Deployment:** Railway (Backend API)

## 🔗 Live Links
- **Backend API (Swagger UI):** https://team-task-manager-production-46fb.up.railway.app/docs
- **Frontend:** *(Run locally via VS Code Live Server)*

## 💻 How to Run Locally

### 1. Backend Setup
```bash
# Clone the repository
git clone <https://github.com/abhishekdaredavid/team-task-manager>

# Navigate to the project directory
cd team-task-manager

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
python main.py
