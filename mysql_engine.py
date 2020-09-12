import mysql.connector
import os


class MySqlEngine:
    def __init__(self):
        host = os.environ["DB_HOST"]
        user = os.environ["DB_user"]
        password = os.environ["DB_PASSWORD"]
        database = os.environ["DB_NAME"]
        try:
            self.con = mysql.connector.connect(host=host, user=user, password=password, database=database,
                                               auth_plugin='mysql_native_password')

        except Exception as e:
            print("connecting error", e)

    def execute_query(self, query):
        cur = self.con.cursor()
        try:
            cur.execute(query)
        except Exception as e:
            print("Execute query error",e)
        if query[:6] == "select":
            result = cur.fetchall()
            return result
        else:
            self.con.commit()

    def close_conn(self):
        cur = self.con.cursor()
        cur.close()

    def get_data(self, table_name,  columns="*", condition=None):
        self.condition = condition
        self.table_name=table_name
        self.columns=columns


        query="select {} from {}".format(self.columns,self.table_name)
        if condition:
            query += condition
        result = self.execute_query(query)
        return result


    def create_record(self, table_name, data=None):
        if table_name[:8]=="customer":
            query="insert into customer(first_name,last_name,mobile_no,email) values('{}','{}','{}','{}')".format(data[0],data[1],data[2],data[3])
        elif table_name[:11]=="transaction":
            query = "insert into transaction(trans_type,amount,date,person,account_no) values('{}',{},curdate(),'{}',{})".format(data[0],data[1],data[2],data[3],)
        else:
            query = "insert into balance(date,account_no) values(curdate(),{})".format( data)
        try:
            self.execute_query(query)
        except Exception as e:
            print("create record Error :",e)

    def update_record(self, table_name,column, data=None, condition=None):
        query = "update {} set {} ={}".format(table_name,column, data)
        if condition:
            query += condition
        self.execute_query(query)

    def delete(self, table_name, condition=None):
        query="delete from {}".format(table_name)
        if condition:
            query += condition
            self.execute_query(query)
