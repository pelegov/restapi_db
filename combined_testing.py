import json
import pymysql
import requests
from selenium import webdriver
from db_connector import post_value, get_value, delete_value, put_value

url = "http://localhost:5000/users/12"
conn = pymysql.connect(host='remotemysql.com', port=3306, user='tZsOURTiTL', passwd='kjgwPi1fPd', db='tZsOURTiTL')
conn.autocommit(True)
cursor = conn.cursor()
driver = webdriver.Firefox(executable_path="/Users/nave-peleg/Downloads/geckodriver")

payload = json.dumps({
  "user_id": 12,
  "user_name": "navetime",
  "creation_date": "17022022"
})
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

get = requests.get('http://127.0.0.1:5000/users/12')
if get.ok:
    print(res.json())

get_value("12")

driver.get('http://127.0.0.1:5000/users/12')
