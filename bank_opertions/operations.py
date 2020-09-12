"""
Bank operations' functionality like open an account, deposit, withdrawn etc.
Get input from user, validate inputs and pass further.
"""
from validate_email import validate_email
from models.customer import *
from models.transactions import *


class Operations:
    balance = ''
       
    def open_new_account(self):
        while True:
            first_name=input("Enter First Name :")
            if not valid.is_name_valid(first_name):
                print("Enter Valid First Name")
            else:
                break
        while True:
            last_name = input("Enter Last Name :")
            if not valid.is_name_valid(last_name):
                print("Enter Valid Last Name")
            else:
                break
        while True:
            email = input("Enter Email :")
            if not validate_email(email):
                print("Enter Valid email")
            else:
                break

        while True:
            mobile_no = input("Enter mobile number :")
            if not valid.is_mobile_valid(mobile_no):
                print("Enter Valid Mobile Number")
            else:
                new_obj=Customer()
                new_obj.create_new_account(first_name,last_name,mobile_no,email)
                break

    def deposit_amount(self):
        while True:
            account_no = input("Enter Account Number:")
            if not account_no.isnumeric():
                print("Enter Valid Account Number:")
            else:
                if not valid.check_account(int(account_no)):
                    print("Enter Valid Account Number:")
                    continue
                else:
                    break
        bal = self.balance_enquiry(account_no)
        if not bal:
            bal = 0

        while True:
            name = input("Enter Name :")
            if not valid.is_name_valid(name):
                print("Enter Valid Name")
            else:
                break
        while True:
            new_amount = 0.0
            try:
                new_amount = float(input("Enter Amount"))
                break
            except ValueError:
                print("Please enter valid amount.")

        balance =bal+new_amount
        new_obj = AccountBalance()
        new_obj.deposit_amount(account_no,name,new_amount,balance)

    def withdraw_amount(self):
        while True:
            account_no = input("Enter Account Number:")
            if not account_no.isnumeric():
                print("Enter Valid Account Number:")
                continue
            else:
                if not valid.check_account(int(account_no)):
                    print("Enter Valid Account Number:")
                    continue
                else:
                    break
        while True:
            name = input("Enter Name :")
            if not valid.is_name_valid(name):
                print("Enter Valid Name")
            else:
                break
        account_balance=self.balance_enquiry(account_no)
        while True:
            new_amount = int(input("Enter Amount"))
            if not new_amount<account_balance:
                print("Enter valid Amount:")
            else:
                break
        balance = account_balance - new_amount
        new_obj = AccountBalance()
        new_obj.withdraw_amount(new_amount,name,account_no,balance)


    def balance_enquiry(self,account_no):
        balance=AccountBalance()
        result=balance.get_balance(account_no)
        return result

    def mini_statement(self):
        pass
    def customer_details(self):
        while True:
            account_no = int(input("Enter account_no:"))
            if not valid.check_account(account_no):
                print("Enter Valid Account No:")
            else:
                break
        new_obj=Customer()
        result=new_obj.get_customer_details(account_no)
        for i in result:
            print("Account Number:",i[0],end="")
            print("  First Name:", i[1],end="")
            print("  Last Name", i[2],end="")
            print("  Mobile Number:", i[3],end="")
            print("  Email:", i[4])


    def transaction_reports(self):
        while True:
            print("1: Transaction by Year")
            print("2: Transaction By Month")
            print("3: transaction by day")
            print("4: all transaction")
            trans_check = int(input("Enter opton:"))
            if trans_check == 1:
                new_obj=Transactions()
                type="year"
                year=int(input("Enter year"))
                if year == 2020:
                    new_obj.get_transactions(type,year)
                else:
                    print("No Transaction Found")
                break

            elif trans_check == 2:
                new_obj = Transactions()
                type = "month"
                month = int(input("Enter month"))
                if month == 9:
                    new_obj.get_transactions(type, month)
                else:
                    print("No Transaction Found")
                break
            elif trans_check == 3:
                new_obj = Transactions()
                type = "day"
                day = int(input("Enter Day"))
                new_obj.get_transactions(type, day)
                break
            elif trans_check == 4:
                new_obj = Transactions()
                new_obj.get_all_transactions()
                break
            else:
                print("Enter Valid Number")
                continue


class Update_cus_detail:
    def update_first_name(self):
        while True:
            first_name = input("Enter First Name :")
            if not valid.is_name_valid(first_name):
                print("Enter Valid First Name")
            else:
                break
        while True:
            account_no = int(input("Enter account_no:"))
            if not valid.check_account(account_no):
                print("Enter Valid Account No:")
            else:
                break
        condition=" where account_no={}".format(account_no)
        new_obj=Update()
        new_obj.update_first_name(first_name,condition)
    def update_last_name(self):
        pass
    def update_mobile_no(self):
        pass
    def mobile_no(self):
        pass

class Validation():

    def __init__(self):
        pass
    def check_account(self,account_no):
        new_obj=Customer()
        result=new_obj.is_valid_account_number(account_no)
        for i in result:
            if i[0]==account_no:
                return True
        return False

    def is_mobile_valid(self,mobile_no):
        if len(mobile_no) == 10:
            if mobile_no.isnumeric():
                return True
            else:
                return False
        else:
            return False
    def is_name_valid(self,name):
        if name.isalpha():
            return True
        else:
            return False

    def is_amount_valid(self, amount):
        if str(amount).isalpha():
            return False
        else:
            if amount == float(amount):
                return True
            else:
                return False
    def is_number_valid(self,number):
        if number.isnumeric():
            return True
        else:
            return False

valid=Validation()
