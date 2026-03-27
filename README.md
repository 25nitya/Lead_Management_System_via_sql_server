# Lead Management System (FastAPI + MySQL)

A simple backend API built using **FastAPI** and **MySQL** to manage business leads.
This project supports creating, viewing, and deleting leads through REST APIs.

---

##Features

✅ Create new leads
✅ Store leads in MySQL database
✅ Delete leads by ID
✅ Automatic request validation using Pydantic
✅ Interactive Swagger API documentation


---

## Tech Stack

* Python 3
* FastAPI
* MySQL
* Pydantic
* Uvicorn

---

## 📂 Project Structure

```
project_folder/
│── main.py
│── database.py
│── model.py
│── README.md
│── .gitignore
│── venv/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/25nitya/Lead_Management_System_via_sql_server.git
cd Lead_Management_System_via_sql_server
```

---

### 2️⃣ Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

(Windows → `venv\Scripts\activate`)

---

### 3️⃣ Install dependencies

```
pip install fastapi uvicorn mysql-connector-python pydantic
```

---

### 4️⃣ Configure database

Open **database.py** and update:

```
host="localhost"
user="root"
password="YOUR_PASSWORD"
database="YOUR_DB_NAME"
```

---

### 5️⃣ Run the server

```
uvicorn main:app --reload
```

---

## 🌐 Open API Docs

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📮 Example API Requests

### ➜ Create Lead

POST `/leads`

```
{
  "name": "John",
  "email": "john@email.com",
  "industry": "IT",
  "status": "New"
}
```

---

### ➜ Delete Lead

DELETE `/delete_lead/{id}`

Example:

```
DELETE /delete_lead/2
```

---

## 🎯 Learning Purpose

This project was built to practice:

* FastAPI backend development
* Database integration
* REST API design
* Python project structuring

---

## 👩‍💻 Author

**Nitya Gupta**

---

⭐ If you like this project, consider giving it a star!
