import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InstaBot():
    def __init__(self, username, password):
        self.password = password
        self.username = username
        self.browser = webdriver.Chrome()

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/)
        uName = self.browser.find_element_by_name("username")
        