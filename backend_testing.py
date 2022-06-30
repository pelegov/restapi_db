import requests
import json
import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='tZsOURTiTL', passwd='kjgwPi1fPd', db='tZsOURTiTL')
conn.autocommit(True)
cursor = conn.cursor()
url = "http://localhost:5000/users/1"

payload = json.dumps({
  "user_id": 1,
  "user_name": "john"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

get = requests.get('http://127.0.0.1:5000/data/1')
if get.ok:
    print(res.json())


def get_value_be():
    user_id = "1"
    cursor.execute("SELECT * FROM tZsOURTiTL.users WHERE (user_id) = " + user_id + ";")
    user_name = ""
    for row in cursor:
        print(row)
        user_name = row[1]
    cursor.close()
    conn.close()
    return user_name

get_value_be()