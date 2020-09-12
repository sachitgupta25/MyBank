
from mysql_engine import MySqlEngine
from bank_opertions.operations import Operations, Validation


def show_welcome_screen():
    print("******************************************************************************************")
    print("******************************************************************************************")
    print("*************************************WELCOME**********************************************")


def initialize():
    mysql = MySqlEngine()
    query = "create table if not exists customer(account_no int NOT NULL AUTO_INCREMENT primary key ," \
            "first_name varchar(10),last_name varchar(10),mobile_no char(10),email varchar(50))"
    query2 = "alter table customer AUTO_INCREMENT =1002001"
    try:
        mysql.execute_query(query)
        mysql.execute_query(query2)
    except Exception as e:
        print("Transaction Table Error", str(e))
    query3 = "create table if not exists transaction(trans_id int(10) not null auto_increment primary key, " \
             "trans_type varchar(10) ,amount int(10),date datetime,person varchar(10) ,account_no int not null ," \
             "FOREIGN KEY (account_no) REFERENCES customer(account_no))"
    query4 = "alter table transaction AUTO_INCREMENT =1002001"
    try:
        mysql.execute_query(query3)
        mysql.execute_query(query4)
    except Exception as e:
        print("balance Table Error", str(e))
    balance_query = "create table if not exists balance(bal_id int(10) not null auto_increment primary key," \
                    "date datetime,balance float(10) ,account_no int not null ,FOREIGN KEY (account_no) " \
                    "REFERENCES customer(account_no))"
    balance_id_update = "alter table balance AUTO_INCREMENT =10000000"
    mysql.execute_query(balance_query)
    mysql.execute_query(balance_id_update)


def display_menu():
    while True:
        print("1: Create New Account:")
        print("2: Deposit:")
        print("3: Withdraw:")
        print("4: Balance Enquiry:")
        print("5: Transaction's Reports:")
        print("6: Customer Details:")

        try:
            operation_choice = int(input("Enter option: "))
        except ValueError:
            print("Invalid option.")
            continue
        perform_operation(operation_choice)


def display_trans_menu():
    print("1: Transaction by Year")
    print("2: Transaction By Month")
    print("3: transaction by day")
    print("4: all transaction")


def perform_operation(operation_choice):
    operation = Operations()
    if operation_choice == 1:
        operation.open_new_account()
    elif operation_choice == 2:
        operation.deposit_amount()
    elif operation_choice == 3:
        operation.withdraw_amount()

    elif operation_choice == 4:
        valid = Validation()
        while True:
            account_no = int(input("Enter Account Number"))
            if not valid.check_account(account_no):
                print("Enter Valid Account Number")
            else:
                break
        result = operation.balance_enquiry(str(account_no))
        print("Your Balance is:", result)
    elif operation_choice == 5:
        operation.transaction_reports()
    elif operation_choice == 6:
        operation.customer_details()
    else:
        print("Enter Valid Option")
