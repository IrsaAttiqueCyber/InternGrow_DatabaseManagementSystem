import sqlite3
import hashlib
import shutil
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_NAME = os.path.join(BASE_DIR, "users.db")

# Password Hashing Helper
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create database and users table
def create_database():
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        """)
        connection.commit()
        connection.close()
        print("Database and users table created successfully!")
    except sqlite3.Error as e:
        print("Database error:", e)

# User Registration (with Password Hashing)
def register_user():
    print("\n----- User Registration -----")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    role = input("Enter role (Admin/User): ").strip()
    
    if not username:
        print("Username cannot be empty!")
        return
    if not password:
        print("Password cannot be empty!")
        return
    if role.lower() not in ["admin", "user"]:
        print("Invalid role! Please enter Admin or User.")
        return
        
    role = role.capitalize()
    hashed_pw = hash_password(password)

    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        """, (username, hashed_pw, role))
        connection.commit()
        connection.close()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists!")
    except sqlite3.Error as e:
        print("Database error:", e)

# Login Session Helper for Main Menu
def login_user_session():
    print("\n----- User Login -----")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not username or not password:
        print("Username and password are required!")
        return None

    hashed_pw = hash_password(password)

    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, username, role
            FROM users
            WHERE username = ? AND password = ?
        """, (username, hashed_pw))

        user = cursor.fetchone()
        connection.close()

        if user:
            print(f"\nLogin successful! Welcome {user[1]} ({user[2]})")
            return user
        else:
            print("\nInvalid username or password!")
            return None
    except sqlite3.Error as e:
        print("Database error:", e)
        return None

# Read Operation
def view_users():
    print("\n----- Registered Users List -----")
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT id, username, role FROM users")
        users = cursor.fetchall()
        connection.close()
        if users:
            print(f"{'ID':<5} | {'Username':<15} | {'Role':<10}")
            print("-" * 35)
            for user in users:
                print(f"{user[0]:<5} | {user[1]:<15} | {user[2]:<10}")
        else:
            print("No users found in the database.")
    except sqlite3.Error as e:
        print("Database error:", e)

# Update Operation
def update_user():
    print("\n----- Update User Role -----")
    user_id = input("Enter User ID to update: ").strip()
    new_role = input("Enter new role (Admin/User): ").strip()
    if not user_id or not new_role:
        print("User ID and New Role are required!")
        return
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
        if not cursor.fetchone():
            print(f"No user found with ID {user_id}")
            connection.close()
            return
        cursor.execute("UPDATE users SET role = ? WHERE id = ?", (new_role.capitalize(), user_id))
        connection.commit()
        connection.close()
        print(f"User ID {user_id} role updated to '{new_role.capitalize()}' successfully!")
    except sqlite3.Error as e:
        print("Database error:", e)

# Delete Operation
def delete_user():
    print("\n----- Delete User -----")
    user_id = input("Enter User ID to delete: ").strip()
    if not user_id:
        print("User ID is required!")
        return
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
        if not cursor.fetchone():
            print(f"No user found with ID {user_id}")
            connection.close()
            return
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        connection.commit()
        connection.close()
        print(f"User ID {user_id} deleted successfully!")
    except sqlite3.Error as e:
        print("Database error:", e)

# Search User
def search_user():
    print("\n----- Search User -----")
    search_term = input("Enter username to search: ").strip()
    if not search_term:
        print("Search term cannot be empty!")
        return
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, username, role 
            FROM users 
            WHERE username LIKE ?
        """, (f"%{search_term}%",))
        users = cursor.fetchall()
        connection.close()
        if users:
            print(f"\nFound {len(users)} record(s):")
            print(f"{'ID':<5} | {'Username':<15} | {'Role':<10}")
            print("-" * 35)
            for user in users:
                print(f"{user[0]:<5} | {user[1]:<15} | {user[2]:<10}")
        else:
            print(f"No user found matching '{search_term}'.")
    except sqlite3.Error as e:
        print("Database error:", e)

# Filter Users 
def filter_users_by_role():
    print("\n----- Filter Users by Role -----")
    role = input("Enter role to filter (Admin/User): ").strip()
    if not role:
        print("Role is required!")
        return
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, username, role 
            FROM users 
            WHERE LOWER(role) = LOWER(?)
        """, (role,))
        users = cursor.fetchall()
        connection.close()
        if users:
            print(f"\nUsers with role '{role}':")
            print(f"{'ID':<5} | {'Username':<15} | {'Role':<10}")
            print("-" * 35)
            for user in users:
                print(f"{user[0]:<5} | {user[1]:<15} | {user[2]:<10}")
        else:
            print(f"No users found with role '{role}'.")
    except sqlite3.Error as e:
        print("Database error:", e)

# Database Reports
def generate_reports():
    print("\n==================================")
    print("      DATABASE SYSTEM REPORT      ")
    print("==================================")
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM users")
        total_users = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM users WHERE LOWER(role) = 'admin'")
        admin_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM users WHERE LOWER(role) = 'user'")
        regular_user_count = cursor.fetchone()[0]
        
        print(f"Total Registered Users : {total_users}")
        print(f"Total Admins           : {admin_count}")
        print(f"Total Regular Users    : {regular_user_count}")
        print("-" * 35)
        
        cursor.execute("SELECT id, username, role FROM users")
        users = cursor.fetchall()
        connection.close()
        
        if users:
            print("\nDetailed Breakdown:")
            print(f"{'ID':<5} | {'Username':<15} | {'Role':<10}")
            print("-" * 35)
            for user in users:
                print(f"{user[0]:<5} | {user[1]:<15} | {user[2]:<10}")
        else:
            print("No detailed records found.")
        print("==================================\n")
    except sqlite3.Error as e:
        print("Database error:", e)

# Database Backup
def backup_database():
    print("\n----- Database Backup -----")
    backup_file = os.path.join(BASE_DIR, "database_backup.db")
    try:
        if os.path.exists(DATABASE_NAME):
            shutil.copyfile(DATABASE_NAME, backup_file)
            print(f"Backup created successfully: {backup_file}")
        else:
            print("Main database file does not exist yet!")
    except Exception as e:
        print("Backup failed:", e)

# Main Interactive Menu with Role-Based Access Control
def main():
    create_database()
    current_user = None

    while True:
        if not current_user:
            print("\n==================================")
            print("  DATABASE MANAGEMENT SYSTEM MENU ")
            print("==================================")
            print("1. Register User")
            print("2. Login")
            print("3. Exit")
            
            choice = input("Select an option (1-3): ").strip()

            if choice == '1':
                register_user()
            elif choice == '2':
                current_user = login_user_session()
            elif choice == '3':
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice! Try again.")
        else:
            user_id, username, role = current_user
            print(f"\n--- Logged in as: {username} ({role}) ---")
            print("1. View Profile / All Users")
            print("2. Search User")
            print("3. Filter Users by Role")
            print("4. Generate Reports")
            
            if role.lower() == 'admin':
                print("5. Update User Role (Admin Only)")
                print("6. Delete User (Admin Only)")
                print("7. Create Database Backup (Admin Only)")

            print("8. Logout")

            choice = input("Select an option: ").strip()

            if choice == '1':
                view_users()
            elif choice == '2':
                search_user()
            elif choice == '3':
                filter_users_by_role()
            elif choice == '4':
                generate_reports()
            elif choice == '5' and role.lower() == 'admin':
                update_user()
            elif choice == '6' and role.lower() == 'admin':
                delete_user()
            elif choice == '7' and role.lower() == 'admin':
                backup_database()
            elif choice == '8':
                print(f"Logging out {username}...")
                current_user = None
            else:
                print("Invalid choice or Unauthorized access!")

if __name__ == "__main__":
    main()