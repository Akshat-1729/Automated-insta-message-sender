from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
user=input("Enter username: ")
message=input("Enter message: ")
phno=input("Enter your registered phone number: ")
passwrd=input("Enter your insta password: ")
aa=webdriver.Chrome()
aa.maximize_window()
aa.get("https://www.instagram.com/accounts/login/")
time.sleep(1.6)
aa.find_element(By.NAME,"username").send_keys(phno)
time.sleep(1)
aa.find_element(By.NAME,"password").send_keys(passwrd)
time.sleep(1)
aa.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.RETURN)
time.sleep(6)
aa.find_element(By.XPATH,"//a[@href='/direct/inbox/?next=%2F']").click()
time.sleep(3)
aa.find_element(By.XPATH,"//button[@class='_a9-- _a9_1']").click()
time.sleep(3)
aa.find_element(By.XPATH,"//div[@class='_abm0']").click()
time.sleep(1)
aa.find_element(By.NAME,"queryBox").send_keys(user)
time.sleep(3)
aa.find_element(By.XPATH,"//button[@class='_abl-']").click()
time.sleep(3)
aa.find_element(By.XPATH,"//div[@class='_aagz']").click()
time.sleep(3)
aa.find_element(By.XPATH,"//textarea[@placeholder]").send_keys(message)
time.sleep(0.6)
aa.find_element(By.XPATH,"//textarea[@placeholder]").send_keys(Keys.RETURN)
time.sleep(3)

aa.close()
print("Message sent successfully")


