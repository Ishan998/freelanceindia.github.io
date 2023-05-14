import sqlite3
from sqlite3 import OperationalError
# connection=sqlite3.connect("hastext.db")
# cur=connection.cursor()
#
# # cur.execute("CREATE TABLE Persons (PersonID int, LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255));")
# cur.execute("INSERT INTO Persons (PersonID, LastName, FirstName, Address, City) VALUES (100,'Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger');")
# connection.commit()

class database:

    def create(self):
        connection = sqlite3.connect("hastext.db")
        cur=connection.cursor()
        cmd="""CREATE TABLE Auth2 (PersonID INTEGER PRIMARY KEY AUTOINCREMENT, LastName varchar(255),UserName varchar(255),Phonenumber varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255),Password varchar(255));"""
        cur.execute(cmd)
        connection.close()
        return True
    def Adddata(self):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        cmd="""INSERT INTO Auth2 (LastName,UserName,Phonenumber, FirstName, Address, City,Password) VALUES ('Cardinal','Cardinal_0111','1234567789', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger','Sugar7@best');"""
        connection.execute(cmd)
        connection.commit()
        return True
    def showdata(self):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        # store=cur.fetchall()
        #show all data
        store=cur.execute("SELECT * from Auth2")


        return store
    def delrowrecod(self,username):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        del_row=f"delete Password from Auth2 where Username={username}"
        cur.execute(del_row)
        return True
    def deletetable(self):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        del_table="DROP TABLE Auth2"
        cur.execute(del_table)
        cur.close()
        return True
    def deletecol(self,colname):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        cmd=f"ALTER TABLE Auth2 DROP COLUMN {colname}"
        cur.execute(cmd)
        cur.close()
        return True
    def addcol(self,colname):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        cmd=f"ALTER TABLE Auth2 ADD {colname} varchar(150)"
        cur.execute(cmd)
        cur.close()
        return True








#
# if __name__=="__main__":
#     point=database()
    # if  point.create() == True:
    #     print("Table Is Created")
    # if point.Adddata() == True:
    #     print("Data Added")
    #     u=point.showdata()
    #     for i in u:
    #         print(i)
    # if point.delrowrecod(username='') == True:
    #     print("ready for password reset")
    # if point.deletetable()==True:
    #     print("table Deleted")
    # if point.deletecol('City') == True:
    #     print("Coloum City is deleted")
    # if point.addcol('City')==True:
    #     print("Coloumn City is added")



