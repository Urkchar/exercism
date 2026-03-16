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
            raise ValueError("account not open")

    def open(self):
        """Opens the account, if closed"""
        if self.status == "closed":
            self.balance = 0
            self.status = "open"
        else:
            raise ValueError("account already open")

    def deposit(self, amount):
        """Increases the value of the account by amount"""
        if self.status == "open":
            if amount > 0:
                with self.lock:
                    self.balance += amount
            else:
                raise ValueError("amount must be greater than 0")
        else:
            raise ValueError("account not open")

    def withdraw(self, amount):
        """Decreases the value of acount by amount"""
        if self.status == "open":
            if amount <= self.balance:
                if amount > 0:
                    with self.lock:
                        self.balance -= amount
                else:
                    raise ValueError("amount must be greater than 0")
            else:
                raise ValueError("amount must be less than balance")
        else:
            raise ValueError("account not open")

    def close(self):
        """Closes the acount, if open"""
        if self.status == "open":
            self.status = "closed"
        else:
            raise ValueError("account not open")
