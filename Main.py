import tkinter as tk
from tkinter import messagebox
import sqlite3


# Database setup
def init_db():
    conn = sqlite3.connect('Library.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            members_id INTEGER PRIMARY KEY AUTOINCREMENT,
            membership_number TEXT NOT NULL UNIQUE,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            join_date TEXT NOT NULL,
            membership_type TEXT NOT NULL,
            status TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()