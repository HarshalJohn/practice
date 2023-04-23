import mysql.connector

'''import time
from datetime import datetime


def welcome_msg():
    return "  HELLO JOHNY, "


def date_time():
    now = datetime.now()
    p = now.strftime('%d/%m/%Y %I:%M:%S %p')
    str(p)
    d = "\n  Today is " + p
    return d


t = time.strftime("%H")
t = int(t)


if 3 <= t < 12:

    print(welcome_msg() + "Good Morning" + date_time())

elif 12 <= t < 17:

    print(welcome_msg() + "Good Afternoon" + date_time())

elif 17 <= t < 20:

    print(welcome_msg() + "GOOD EVENING Sir" + date_time())
else:

    print(welcome_msg() + "Good Night" + date_time())

'''
mydb = mysql.connector.connect(host="localhost",user="root",password="johny", database="practice_user_details")
print(mydb)
if(mydb):
    print("connection successful")
else:
    print("connection unsuccessful")

my_cursor = mydb.cursor()

my_cursor.execute("Show tables")
for tb in my_cursor:
    print(tb)
sql_form = "Insert into user_details(user_first_name,user_last_name,user_email,user_phone_number,user_dob) Values(%s,%s,%s,%s,%s)"
user_details = [("Harshal","John","harshaljohn634@gmail.com",7305708860,"2006-09-16")]
my_cursor.executemany(sql_form,user_details)
mydb.commit()
