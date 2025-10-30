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

## Registration Form
The RegistrationForm class is a simple graphical user interface (GUI) program made with Tkinter that helps register new members. 
It creates a form where users can type in information such as member number, first name, last name, email, phone number, address, membership type, and status.
The program is written using an object-oriented approach, meaning the code is organised inside a class. 
The __init__ method sets up the main window by creating all the labels, entry boxes, and the register button. Each box is used to collect a specific piece of information from the user. 
The register_member method checks that all the important fields — member number, first name, last name, and email — are filled in before registering. 
If any of these boxes are empty, the program shows an error message to warn the user. This helps make sure that all member records are complete and accurate.
