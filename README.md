# 📌 **Todo App — Django + Asthetic/Modern UI + Authentication**

A clean, modern, and fully functional **Todo Application** built using **Django**, designed with an aesthetic and user-friendly UI.
It allows users to **create, edit, and delete tasks** while ensuring privacy and security with **built-in Django authentication**.

---

## 🚀 **Features**

### ✅ **User Authentication**

* Secure **signup**, **login**, and **logout**
* Django's in-built auth system ensures safe access
* Each user sees **only their own tasks**

### 📝 **Todo Management**

* Add new tasks
* Edit existing tasks
* Delete tasks
* Track tasks with clean UI indicators
* Tasks are saved with timestamps & sorted nicely

### 🎨 **Modern & Aesthetic UI**

* Fully responsive
* Clean layout with elegant typography
* Designed to be simple, minimal, and visually appealing
* Smooth color usage for completed/uncompleted tasks

---

## 🛠️ **Tech Stack**

| Component      | Technology            |
| -------------- | --------------------- |
| Backend        | Django (Python)       |
| Frontend       | HTML, CSS             |
| Icons          | Font Awesome          |
| Authentication | Django Auth System    |
| Database       | SQLite (default)      |

---

## 📂 **Project Structure**

```
/todoapp
    ├── templates/
    │     ├── signup.html
    │     ├── login.html
    │     └── todo.html
    ├── static/
    │     ├── css/
    │     ├── js/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── ...
```

---

## ⚙️ **How to Run Locally**

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Todo_app.git
cd Todo_app
```

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
source venv/Scripts/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py migrate
```

### 5️⃣ Start the server

```bash
python manage.py runserver
```

---

## 🔒 **Why Django Authentication?**

Using Django’s built-in authentication system gives:

* Secure user login & signup
* Password hashing by default
* Session-based login
* Protects user-specific data
* Eliminates need to build your own auth logic

---

## ⭐ **Future Enhancements (Optional)**

* Add task categories (Work, Personal, etc.)
* Add dark mode
* Add task completion toggle
* Add pagination for long lists

---

## 📜 **License**

This project is open-source and available under the **MIT License**.
