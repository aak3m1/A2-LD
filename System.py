from tkinter import *
from tkinter import ttk  # Import ttk for themed widgets
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import StringVar
import sqlite3
import tkinter.messagebox
from tkinter import Label, Entry, Button, Toplevel, messagebox
from collections import deque


#system class
class System:
    def __init__(self, root):
        """
        this class represents the system object with the provided root (Tkinter Window)
        the root: Tk object
        the main window of the hospital management system
        """
        self.root = root #assigning the tkniter root window to the instance variable
        self.root.title("Welcome to Hospital Management System") #setting title
        self.root.geometry("450x300") #setting the frame
        self.root.configure

        self.conn = sqlite3.connect('Hospital.system.db') #connect to the database for the Hospital Management
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''') # Creating the employees table if it doesn't exist

        self.conn.commit()

        #login frame
        self.login_frame = Frame(self.root, bd=5, relief=RIDGE)
        self.login_frame.pack(pady=20)

        #username entering
        self.lblUsername = Label(self.login_frame, text="Username:")
        self.lblUsername.grid(row=0, column=0)
        self.entryUsername = Entry(self.login_frame)
        self.entryUsername.grid(row=0, column=1)

        #password entering
        self.lblPassword = Label(self.login_frame, text="Password:")
        self.lblPassword.grid(row=1, column=0)
        self.entryPassword = Entry(self.login_frame, show='*')
        self.entryPassword.grid(row=1, column=1)

        #login button
        self.btnLogin = Button(self.login_frame, text="Login", command=self.login)
        self.btnLogin.grid(row=2, column=0, columnspan=2)

    def login(self):
        username = self.entryUsername.get()
        password = self.entryPassword.get()

        self.cursor.execute('SELECT * FROM employees WHERE username = ? AND password = ?', (username, password))
        user = self.cursor.fetchone() #if the username and password match in the database

        if user:
            messagebox.showinfo("Login Successful", "Welcome to the Hospital Management System!")
            self.open_hospital_system()# Open the Hospital Management System window after successful login
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_hospital_system(self):# Open the hospital management system GUI here
        self.root.destroy()  # closing the login window
        root = Tk()
        application = Hospital(root)
        root.mainloop()

