from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Buka Browser
driver=webdriver.Chrome()
driver.get("file:///D:/test/Mini_Project/Blackpink_Login/login.html")
time.sleep(1)

#Isi username dan password
driver.find_element(By.ID, "username").send_keys("ella123")
driver.find_element(By.ID, "password").send_keys("passwordku")
driver.find_element(By.ID, "login-button").click()

time.sleep(5)

welcome_text=driver.find_element(By.ID, "welcome-message").text

assert "Welcome, Ella" in welcome_text, "Login gagal atau text tidak sesuai"
time.sleep(10)
driver.quit()