from selenium import webdriver

###Establish Selenium driver to get the element from the specific route.
driver = webdriver.Firefox(executable_path="/Users/nave-peleg/Downloads/geckodriver")
driver.get("http://localhost:5001/users/get_user_data/1")
x = driver.find_element_by_id("user")
print(x.get_attribute("id"))