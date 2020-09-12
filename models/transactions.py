"""
Class representing transactions in Bank System.
"""
from mysql_engine import *


class Transactions:
    transaction_type = None
    date = None
    amount = None
    account_number = None
    person = None

    def create_transaction(self):
        pass

    def get_all_transactions(self):
        mysql_obj=MySqlEngine()
        result=mysql_obj.get_data("transaction")
        for i in result:
            print("Account Number:", i[5],end="")
            print("Transaction Type:", i[1],end="")
            print("Amount", i[2],end="")
            print("Date", i[3],end="")
            print("Person", i[4],end="")
            print("Transaction Id Is:", i[0])

    def get_transactions(self,search,filter):
        mysql_obj=MySqlEngine()
        condition=" where {}(date)={}".format(search,filter)
        result=mysql_obj.get_data("transaction","*",condition)
        if result == None:
            print("No Transaction Found")
        else:
            for i in result:
                print("Account Number:", i[5],end="")
                print("  Transaction Type:", i[1],end="")
                print("  Amount:", i[2],end="")
                print("  Date:", i[3],end="")
                print("  Person:", i[4],end="")
                print("  Transaction Id Is:", i[0])

