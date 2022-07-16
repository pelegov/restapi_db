import json
import pymysql
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from db_connector import post_value, get_value, delete_value, put_value

url = "http://localhost:5000/users/12"
conn = pymysql.connect(host='sql11.freemysqlhosting.net', port=3306, user='sql11506470', passwd='QwjD6b64t9', db='sql11506470')
conn.autocommit(True)
cursor = conn.cursor()
driver = webdriver.Firefox(executable_path="/Users/nave-peleg/Downloads/geckodriver")

###POST call method
payload = json.dumps({
  "user_id": 2,
  "user_name": "navetime",
  "creation_date": "17022022"
})
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

###Get call method
get = requests.get('http://127.0.0.1:5000/users/1')
if get.ok:
    print(get.json())

###Function calling to check data
get_value("1")

###Selenium test.
driver.get('http://127.0.0.1:5000/users/1')


