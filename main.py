import sqlite3

conn = sqlite3.connect("Bank.db")
cursor = conn.cursor()

#CREATING DATABASE

cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        email     TEXT    NOT NULL UNIQUE,
        password  TEXT    NOT NULL,
        name      TEXT    NOT NULL,
        age       INTEGER NOT NULL,
        balance   REAL    DEFAULT 0.0,
        created_at TEXT   DEFAULT (datetime('now'))
    )
""")

# Transaction history table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id  INTEGER NOT NULL,
        type        TEXT    NOT NULL,  -- 'deposit', 'withdraw', 'loan_taken', 'loan_paid'
        amount      REAL    NOT NULL,
        date        TEXT    DEFAULT (datetime('now')),
        FOREIGN KEY (account_id) REFERENCES accounts(id)
    )
""")

# Loans table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS loans (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id  INTEGER NOT NULL,
        amount      REAL    NOT NULL,
        is_paid     INTEGER DEFAULT 0,  -- 0 = unpaid, 1 = paid
        taken_at    TEXT    DEFAULT (datetime('now')),
        FOREIGN KEY (account_id) REFERENCES accounts(id)
    )
""")


class Sign_Menu:
    def __init__(self, email, password):
        self.email = email
        self.password = password



class User(Sign_Menu):

    def __init__(self,email, password, name, age, balance, history, loans):
        super.__init__(email,password)
        self.name = name
        self.age = age
        self.balance = balance
        self.history = history
        self.loans = loans

    def menu():
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Loans")
        print("4. Profile")
        print("5. Quit")

    def __str__(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Balance: {self.balance}")
        print("History:")
        for key, value in self.history:
            print(f"{key}: {value}")
        print("Ongoing Loans:")
        for key1, value1 in self.loans:
            print(f"{key1}: {value1}$")

    def __ge__(self, amount):
        return self.balance >= amount
    



    



