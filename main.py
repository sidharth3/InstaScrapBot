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
        time.sleep(5)
    
    def getFollowers(self, maxi):
        self.browser.get('https://www.instagram.com/' + self.username)
        followerButton = self.browser.find_element_by_css_selector('ul li a')
        followerButton.click()
        time.sleep(3) #delay time to make sure followers load
        followList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followList.find_elements_by_css_selector('li'))
    
        followList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < maxi):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
        
        followers = []
        for user in followList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == max):
                break
        return followers

        def getFollowing(self, maxi):


    def closeBrowser(self):
        self.browser.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()
        



    
bot = InstaBot('', '') #Enter your username and password here
bot.signIn()
bot.getUnfollowers(7)



