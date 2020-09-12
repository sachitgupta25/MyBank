"""
Class representing customer table in database.
"""
from mysql_engine import *


class Customer:
    account_number = None
    first_name = None
    last_name = None
    email = None
    contact_number = None

    def create_new_account(self, first_name, last_name, contact_no, email):
        new_obj = MySqlEngine()
        new_obj.create_record("customer", (first_name, last_name, contact_no, email))
        result = self.show_account_no(contact_no, first_name)
        print("Your Account Number:", result)
        new_obj.create_record("balance", result)

    def update_customer_details(self):
        new_obj = MySqlEngine()
        new_obj.update_record("customer",)

    def get_customer_details(self, account_no):
        new_obj = MySqlEngine()
        condition=" where account_no={}".format(account_no)
        result = new_obj.get_data("customer", "*", condition)
        return result

    def show_account_no(self, mobile_no, first_name):
        new_obj = MySqlEngine()
        condition = " where mobile_no={} and first_name='{}'".format(mobile_no, first_name)
        result = new_obj.get_data("customer", "account_no", condition)
        for i in result:
            return i[0]
    def is_valid_account_number(self, account_number):
        new_obj = MySqlEngine()
        result = new_obj.get_data("customer", "account_no", " where account_no = {}".format(account_number))
        return result
class Update:
    new_obj = MySqlEngine()

    def update_first_name(self, first_name, condition):
        self.new_obj.update_record("customer", "first_name", first_name, condition)
    def update_last_name(self, last_name, condition):
        new_obj.update_record("customer", "last_name", last_name, condition)
    def update_email(self, email, condition):
        new_obj.update_record("customer", "email", email, condition)
    def update_mobile_no(self, mobile_no, condition):
        new_obj.update_record("customer", "mobile_no", mobile_no, condition)

class AccountBalance:

    def get_balance(self, account_number):
        new_obj = MySqlEngine()
        condition = " where account_no = {}".format(account_number)
        result = new_obj.get_data("balance", "balance", condition)
        for i in result:
            return i[0]

    def deposit_amount(self, account_no, name, new_amount, balance):
        condition = " where account_no={}".format(account_no)
        new_obj = MySqlEngine()
        type = 'Deposit'
        new_obj.create_record("transaction", (type, new_amount, name, account_no))
        new_obj.update_record("balance", "balance", balance, condition)
        print("Deposit successful:")
        print("Your balance is: ", balance)

    def withdraw_amount(self, amount, name, account_no, balance):
        condition = " where account_no={}".format(account_no)
        new_obj = MySqlEngine()
        type = "Withdraw"
        new_obj.create_record("transaction", (type, amount, name, account_no))
        new_obj.update_record("balance","balance",balance, condition)
        print("Withdraw successful:")
        print("Your balance is: ", balance)

