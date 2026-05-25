import sqlite3


DB_NAME = "users.db"


# =========================================================
# DATABASE CONNECTION
# =========================================================
def connect_db():

    return sqlite3.connect(DB_NAME)


# =========================================================
# CREATE USERS TABLE
# =========================================================
def create_users_table():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL
    )
    """)

    conn.commit()

    conn.close()


# =========================================================
# REGISTER USER
# =========================================================
def register_user(name, email, password):

    conn = connect_db()

    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO users (
            name,
            email,
            password
        )
        VALUES (?, ?, ?)
        """, (name, email, password))

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


# =========================================================
# LOGIN USER
# =========================================================
def login_user(email):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT name, password
    FROM users
    WHERE email = ?
    """, (email,))

    user = cursor.fetchone()

    conn.close()

    return user

    