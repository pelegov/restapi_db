import pymysql
import json

# Establish connection with DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='tZsOURTiTL', passwd='kjgwPi1fPd', db='tZsOURTiTL')
conn.autocommit(True)
cursor = conn.cursor()

# ## SELECT for GET methods (get data)
def get_value(user_id):
    cursor.execute("SELECT * FROM tZsOURTiTL.users WHERE (user_id) = " + user_id + ";")
    user_name = ""
    for row in cursor:
        print(row)
        user_name = row[1]
    #cursor.close()
    #conn.close()
    return user_name

def post_value(id,name,creation):
    cursor.execute("INSERT into tZsOURTiTL.users (user_id, user_name, creation_date) VALUES ({}, '{}','{}')".format(id, name, creation))
    cursor.close()
    conn.close()
    return

def put_value():
    cursor.execute("UPDATE tZsOURTiTL.users SET user_name = 'naveupdated' WHERE user_id = '1'")
    cursor.close()
    conn.close()
    return

def delete_value(id):
    cursor.execute("DELETE FROM tZsOURTiTL.users WHERE (user_id) = ({})".format(id))
    cursor.close()
    conn.close()
    return



#print(get_value('1'))