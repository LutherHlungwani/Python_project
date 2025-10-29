# Python_project
A group project dedicated to Programming 512 module

# Main.py
This is the file where all our code will be housed. (details to be added later on the code)

## init_db()
The initialization of the database (Library.db) 

## Library.db
contains *members* table where the following information on the library members is stored
-members_id INTEGER PRIMARY KEY AUTOINCREMENT,
 membership_number TEXT NOT NULL UNIQUE,
 first_name TEXT NOT NULL,
 last_name TEXT NOT NULL,
 email TEXT NOT NULL UNIQUE,
 phone TEXT NOT NULL,
 address TEXT NOT NULL,
 join_date TEXT NOT NULL,
 membership_type TEXT NOT NULL,
 status TEXT NOT NULL,
            