from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
PATH = "chromedriver"
driver = webdriver.Chrome(PATH)
# takin username as input
login_id = input("Enter your kerberos id: ")
# taking password as input
password = getpass.getpass()
#opening moodle
driver.get("https://moodle.iitd.ac.in/login/index.php")
#sending username input
username = driver.find_element_by_id("username")
username.clear()
username.send_keys(login_id)
#sending password input
pa = driver.find_element_by_id("password")
pa.clear()
pa.send_keys(password)
#getting captcha text
text = driver.find_element_by_id("login").text
captcha = driver.find_element_by_id("valuepkg3")
#finding numbers in captcha text
no = [int(i) for i in text.split() if i.isdigit()]
#solving captcha
if (text.find('add') != -1):
    x = no[0]+no[1]
    captcha.send_keys(x)
elif (text.find('subtract') != -1):
    x = no[0] - no[1]
    captcha.send_keys(x)
elif (text.find('first') != -1):
    captcha.send_keys(no[0])
else:
    captcha.send_keys(no[1])


#logging in
login = driver.find_element_by_id("loginbtn")
login.click()
    
