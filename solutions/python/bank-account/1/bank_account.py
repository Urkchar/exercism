import threading


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.status = "closed"
        self.lock = threading.Lock()

    def get_balance(self):
        """Returns the balance of self"""
        if self.status == "open":
            return self.balance
        else:
            raise ValueError("You cannot check the balance of a closed account")

    def open(self):
        """Opens the account, if closed"""
        if self.status == "closed":
            self.balance = 0
            self.status = "open"
        else:
            raise ValueError("You cannot open an already open account")

    def deposit(self, amount):
        """Increases the value of the account by amount"""
        if self.status == "open":
            if amount > 0:
                with self.lock:
                    self.balance += amount
            else:
                raise ValueError("You cannot deposit a negative amount")
        else:
            raise ValueError("You cannot deposit money into a closed account")

    def withdraw(self, amount):
        """Decreases the value of acount by amount"""
        if self.status == "open":
            if amount <= self.balance:
                if amount > 0:
                    with self.lock:
                        self.balance -= amount
                else:
                    raise ValueError("You cannot withdraw a negative amount")
            else:
                raise ValueError("You cannot withdraw more than balance")
        else:
            raise ValueError("You cannot withdraw money from a closed account")

    def close(self):
        """Closes the acount, if open"""
        if self.status == "open":
            self.status = "closed"
        else:
            raise ValueError("You cannot close a closed account")
