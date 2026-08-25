# Database Management System (Task 3) - InternGrow

A console-based Database Management System developed in Python using SQLite as part of the InternGrow Python Programming Internship.

---

## 📌 Project Overview

The Database Management System is a comprehensive, menu-driven Python application built to demonstrate core relational database management concepts, CRUD operations, user authentication, security standards, and administrative controls.

It features secure password hashing using SHA-256, Role-Based Access Control (RBAC) to protect sensitive database actions, automated dynamic reporting, and one-click database backups — all backed by robust error handling and absolute path management.

---

## ✨ Features

- **User Authentication:** Registration system and secure user login verification.
- **Complete CRUD Operations:** Create new users, Read registered accounts, Update user roles, and Delete database records.
- **Search & Filters:** Search records using partial username matching (`LIKE` query) and filter user lists by assigned roles (`Admin` / `User`).
- **Automated System Reports:** Generates live metrics calculating total registered users, admin distribution, and detailed record breakdowns.
- **Password Hashing:** Utilizes `hashlib` (SHA-256) to eliminate plain-text password storage in the database.
- **Role-Based Access Control (RBAC):** Administrative actions (Update Role, Delete User, Database Backup) are strictly restricted to `Admin` accounts.
- **Database Backup System:** Creates instant, safe clones (`database_backup.db`) using `shutil`.
- **Absolute Path Resolution:** Employs `os.path.abspath(__file__)` to guarantee reliable database file loading across all working directories.
- **Interactive Menu Workflow:** Modular function layout with clear error handling and session management.

---

## 🛠️ Technologies Used & Tools Required

- **Python 3.x** — Core programming language
- **SQLite 3** — Embedded relational database engine (Built-in via `sqlite3`)
- **VS Code** — Primary Integrated Development Environment (IDE)
- **SQLite Viewer** — Recommended VS Code Extension for visual database inspection
- **os, hashlib, shutil** — Built-in Standard Libraries (No external `pip` packages required)

---

## 📂 Project Structure

```text
InternGrow_Task3_DatabaseManagement/
│
├── database_management.py   # Main Python script containing DB logic, RBAC, & menu system
├── users.db                 # SQLite binary database file (Auto-generated on execution)
├── database_backup.db       # Cloned database backup file (Admin generated)
└── README.md                # Project documentation, features, installation, and usage guide
```

### File Breakdown

- **database_management.py** — Main execution script with SQLite connection queries, hashing routines, access controls, and interactive CLI menu.
- **users.db** — SQLite binary relational database storing encrypted user records.
- **database_backup.db** — Automated snapshot clone of `users.db` for recovery purposes.
- **README.md** — Comprehensive documentation and usage manual.

---

## 📊 Feature Capabilities Matrix

| Feature | Operations / Query | Module / Security | Key Output / Action |
|---|---|---|---|
| Authentication | INSERT, SELECT | hashlib (SHA-256) | Hashed user signup & credential validation |
| CRUD Lifecycle | SELECT, UPDATE, DELETE | sqlite3 | Record management with primary key mapping |
| Search & Filtering | LIKE, WHERE LOWER() | sqlite3 | Flexible partial string search & role filtering |
| Reporting System | COUNT(*) Metrics | sqlite3 | Automated database summary & counts breakdown |
| Role-Based Access | RBAC Session Guard | Python Logic | Restricts sensitive actions strictly to Admins |
| Data Backup | Binary Copying | shutil | Generates snapshot copy to database_backup.db |

---

## 🔍 How to Access & Inspect users.db

Because `users.db` is a binary SQLite database file, opening it directly in plain text editors like Notepad will show unreadable binary symbols.

To view and edit the database contents visually inside VS Code:

1. Open VS Code.
2. Navigate to the Extensions tab (`Ctrl + Shift + X`).
3. Search for and install **SQLite Viewer** (by Florian Kleinschmidt).
4. In the Explorer sidebar, right-click on `users.db`.
5. Select **Open With... → SQLite Viewer**.
6. View tables (`users`), columns (`id`, `username`, `password`, `role`), and SHA-256 password hashes in a clean interactive grid.

---

## ▶️ How to Run

**1. Install Python**
Ensure Python 3.x is installed on your operating system.

**2. Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/InternGrow_Task3_DatabaseManagement.git
```

**3. Open the Project Folder**
```bash
cd InternGrow_Task3_DatabaseManagement
```

**4. Run the Application**
```bash
python database_management.py
```

---

## 🖥️ System Pipeline

The program executes through the following operational menu flow:

1. **Database Initialization:** Automatically runs `CREATE TABLE IF NOT EXISTS users` on launch using absolute pathing.
2. **User Registration & Hashing:** Converts plain-text input password to a SHA-256 hash string before `INSERT`.
3. **Login Verification:** Validates incoming credentials against stored password hashes and assigns a session tuple `(id, username, role)`.
4. **RBAC Guard Enforcement:** Dynamically restricts menu choices #5 (Update), #6 (Delete), and #7 (Backup) based on the active session role.
5. **Database Backup:** Clones current binary state into `database_backup.db` via system-level copying.

---

## 🔐 Error Handling & Security Features

- **Sqlite3 Exception Catching:** Handles `sqlite3.IntegrityError` to block duplicate username registrations gracefully.
- **Path Resolution Safety:** Utilizes `os.path.dirname(os.path.abspath(__file__))` to prevent broken paths when executed from different working directories.
- **Cryptographic Security:** Eliminates plain-text passwords in persistent storage using standard SHA-256 hashing.
- **Access Control:** Enforces strict role validation preventing standard users from modifying database schemas or records.

---

## 🚀 Future Improvements

- Implementation of salted password hashing (e.g., bcrypt or argon2) for enhanced security.
- Migration option for multi-user client-server architecture using MySQL / PostgreSQL.
- Dynamic graphical user interface (GUI) built with Tkinter or PyQt6.
- Automated periodic database backup scheduling and ZIP compression.

---

## 🎓 Internship

This project was developed as **Task 3 — Database Management System** for the **InternGrow Python Programming Internship**.

## 👩‍💻 Author

**Irsa Attique**
Cybersecurity Undergraduate
