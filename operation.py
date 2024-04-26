import mysql.connector as connector
class DBHelper:
    def __init__(self):
        self.con = connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='Nobita@123',
            database='pythontest'
        )
        query = 'CREATE TABLE IF NOT EXISTS user (userId INT PRIMARY KEY, userName VARCHAR(300), phone VARCHAR(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Table created successfully.")
    #insert
    def insert_user(self,userid,username,phone):
        query="insert into user(userId,userName,phone) values({},'{}','{}')".format(userid,username,phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to db")
    #fetch all
    def fetch_all(self):
        query="select *from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Userid: ",row[0])
            print("Username: ",row[1])
            print("Phone: ",row[2])
            print()
            #delete
    def delete_user(self,userId):
        query="delete from user where userId={}".format(userId)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")
    def update_user(self,userId,newName,newPhone):
        query="update user set userName='{}', phone='{}' where userId={}".format(newName,newPhone,userId)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")
        