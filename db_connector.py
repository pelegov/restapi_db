import pymysql
import json

# Establish connection with DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='tZsOURTiTL', passwd='kjgwPi1fPd', db='tZsOURTiTL')
conn.autocommit(True)
cursor = conn.cursor()

# ## SELECT for GET methods (get data)
def get_value(id):
    cursor.execute("SELECT * FROM tZsOURTiTL.users WHERE (user_id) =  ({})".format(id))
    cursor.close()
    conn.close()
    return

def post_value(id,name,creation):
    cursor.execute("INSERT into tZsOURTiTL.users (user_id, user_name, creation_date) VALUES ({}, '{}','{}')".format(id, name, creation))
    cursor.close()
    conn.close()
    return

def put_value(id,name):
    dict = {'id': id, 'name': name}
    x = dict.get('id')
    y = dict.get('name')
    uid = dict[x]
    dict[y] = uname
    cursor.execute("UPDATE tZsOURTiTL.users SET (user_name) = 'uname' WHERE (user_id) = uid")
    cursor.close()
    conn.close()
    return

def delete_value(id):
    cursor.execute("DELETE FROM tZsOURTiTL.users WHERE (user_id) = ({})".format(id))
    cursor.close()
    conn.close()
    return

put_value(2, 'naveupdated')