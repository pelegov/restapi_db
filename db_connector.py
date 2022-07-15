import pymysql
import json

# Establish connection with DB
conn = pymysql.connect(host='sql11.freemysqlhosting.net', port=3306, user='sql11506470', passwd='QwjD6b64t9', db='sql11506470')
conn.autocommit(True)
cursor = conn.cursor()

### SELECT for GET methods (get data)
def get_value(user_id):
    cursor.execute("SELECT * FROM sql11506470.users WHERE (user_id) = " + user_id + ";")
    user_name = ""
    for row in cursor:
        print(row)
        user_name = row[1]
    #cursor.close()
    #conn.close()
    return user_name

### Insert for POST methods
def post_value(id,name,creation):
    cursor.execute("INSERT into sql11506470.users (user_id, user_name, creation_date) VALUES ({}, '{}','{}')".format(id, name, creation))
    cursor.close()
    conn.close()
    return

### update for PUT methods
def put_value():
    cursor.execute("UPDATE sql11506470.users SET user_name = 'naveupdated' WHERE user_id = '1'")
    cursor.close()
    conn.close()
    return

### DELETE for DELETE methods
def delete_value(id):
    cursor.execute("DELETE FROM sql11506470.users WHERE (user_id) = ({})".format(id))
    cursor.close()
    conn.close()
    return
