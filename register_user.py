import sqlite3
import random


class BankAccount:
    """A class which will have few functions in order to create and operate a bank account."""

    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance
        try:
            self.db = sqlite3.connect("bankAccounts.sqlite")
            self.cursor = self.db.cursor()
            print("Connecting to database .....Done!")
        except sqlite3.Error as err:
            print('Sql error: %s' % (' '.join(err.args)))
            print("Exception class is: ", err.__class__)

    # 1 -Register user
    def register_user(self):
        """
        A function which creates a SQLite database and accepts user input to create a bank account.
        :param self
        :return: None
        """
        try:
            create_table = "CREATE TABLE IF NOT EXISTS bankAccounts (username TEXT ,password TEXT , user_id " \
                           "INTEGER, balance INTEGER) "
            self.username = str(input("Choose a Username:"))
            self.password = str(input("Choose a Password:"))
            user_id = random.randint(1, 100000)
            add_data_to_db = "INSERT INTO bankAccounts(username,password,user_id,balance) VALUES(?,?,?,?)"
            self.cursor.execute(create_table)
            self.cursor.execute(add_data_to_db, (self.username, self.password, user_id, self.balance))
            self.db.commit()
            print(
                "User Username  {} with  user_ID -{} and a balance of :  {} $ was created ".format(
                    self.username, user_id, self.balance))
        except sqlite3.Error as err:
            print('Sql error: %s ' % (' '.join(err.args)))
            print("Exception class is :", err.__class__)
        except ValueError:
            print("Please input only alphabetical characters, no numbers...")

    # 2 Deposit money into account
    def deposit(self):
        """A function which updates the user balance based on his input"""
        try:
            self.username = str(input("Enter your username: "))
            amount = int(input("Enter the amount you want to DEPOSIT: "))
            self.balance += amount
            deposit_money = "UPDATE bankAccounts SET balance = ? WHERE username = ?"
            self.cursor.execute(deposit_money, (self.balance, self.username))
            self.db.commit()
        except sqlite3.Error as err:
            print('Sql error: %s ' % (' '.join(err.args)))
            print("Exception class is :", err.__class__)
        except ValueError:
            print("Please input only characters, no numbers! ")

    # 3 Withdraw money from account
    def withdraw(self):
        """A function which updates the user balance based on his input"""
        try:
            self.username = input("Enter your username: ")
            amount = int(input("Enter the amount you want to WITHDRAW: "))
            self.balance = self.balance - amount
            deposit_money = "UPDATE bankAccounts SET balance = ? WHERE username = ?"
            self.cursor.execute(deposit_money, (self.balance, self.username))
            self.db.commit()
        except sqlite3.Error as err:
            print('Sql error: %s ' % (' '.join(err.args)))
            print("Exception class is :", err.__class__)
        except ValueError:
            print("Please input only characters, no numbers! ")

    # 4 Show balance of each user
    def show_user_balance(self):
        """A function which shows a specific user's balance """
        try:
            name_to_search = input("Enter the username ")
            self.cursor.execute("SELECT balance FROM bankAccounts WHERE username =? ",
                                [name_to_search])  # this needs to have a list as second argument
            show_balance = self.cursor.fetchone()
            print(" Your balance is {} $ ".format(show_balance))

        except sqlite3.Error as err:
            print('Sql error: %s ' % (' '.join(err.args)))
            print("Exception class is :", err.__class__)

    # 5 Delete a user from the database
    def remove_user(self):
        """ A function which removes a user from the database based on user input.
        param self
        """
        try:
            user_delete = str(input("Please enter the name of the user you want to DELETE: "))
            delete_user = "DELETE FROM bankAccounts WHERE username=?"
            self.cursor.execute(delete_user, (user_delete,))
            self.db.commit()
        except sqlite3.Error as err:
            print('Sql error: %s ' % (' '.join(err.args)))
            print("Exception class is :", err.__class__)

    # 6 Delete the database
    def delete_db(self):
        delete_users_in_db = "DROP TABLE bankAccounts"
        self.cursor.execute(delete_users_in_db)

    # User options for the user
    @staticmethod
    def show_menu():
        menu = ["1.Register User",
                "2.Deposit Money",
                "3.Withdraw money",
                "4.Show my balance",
                "5.Delete User",
                "6.DELETE DATABASE",
                "0.Quit"]
        for x, items in enumerate(menu):
            print(items)
