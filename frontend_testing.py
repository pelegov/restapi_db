from selenium import webdriver
from selenium.webdriver.common.by import By


###Establish Selenium driver to get the element from the specific route.
driver = webdriver.Firefox(executable_path="/Users/nave-peleg/Downloads/geckodriver")
driver.get("http://localhost:5001/users/get_user_data/1")
#x = driver.find_element_by_id("user")
x = driver.find_element(By.ID, 'user')
print(x.get_attribute("id"))

