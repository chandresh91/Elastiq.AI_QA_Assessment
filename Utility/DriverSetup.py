from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver():
    #add your path
    driver_path = "C:/Users/admin/Downloads/chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver
