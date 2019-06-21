from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

#functions:

def signIn(driver,usr,pas):  
    login= driver.find_element_by_class_name('_0mzm-')
    username=driver.find_element_by_name('username')
    password=driver.find_element_by_name('password')
    username.send_keys(usr)
    password.send_keys(pas)
    login.click()

def navtoemmapage():
    driver.get("https://www.instagram.com/emmawatson/")

def openfollowers():
    followers = driver.find_elements_by_class_name("g47SY")
    followers[1].click()
    #driver.get("https://www.instagram.com/emmawatson/followers/")

def getnthfollower(n):
    scr1 = driver.find_element_by_class_name('isgrP')
    for i in range((n-24)//12 +1):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
        time.sleep(1)
    followers = driver.find_elements_by_class_name("d7ByH")
    print(len(followers))
    return followers[n-1]
def opennthfollowerspage(n):
    follower = getnthfollower(n)
    followerlink = "https://www.instagram.com/" + follower.text
    driver.get(followerlink)

def followuser():
    followbutton = driver.find_element_by_class_name("BY3EC")
    followbutton.click()
    
#code:
    
driver =webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(0.5)
signIn(driver,"emmafollowersfollower","itsforemma")
time.sleep(1)
navtoemmapage()
openfollowers()
time.sleep(1)
opennthfollowerspage(100)
time.sleep(1)
followuser()

