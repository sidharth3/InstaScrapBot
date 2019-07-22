import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InstaBot():
    def __init__(self, username, password):
        self.password = password
        self.username = username
        self.browser = webdriver.Chrome()

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        uName = self.browser.find_element_by_name("username")
        passW = self.browser.find_element_by_name("password")
        uName.send_keys(self.username)
        passW.send_keys(self.password)
        passW.send_keys(Keys.ENTER)
        time.sleep(2)

    
bot = InstaBot('', '') #Enter your username and password here
bot.signIn()


