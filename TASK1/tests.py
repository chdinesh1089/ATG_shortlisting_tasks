from selenium import webdriver
import requests
import time
import datetime
def responsetime(driver):
    navStart = driver.execute_script("return window.performance.timing.navigationStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")
    return domComplete-navStart
def consoleErrors(driver):
    try:
        browserlogs = driver.get_log('browser')
    except(ValueError,WebDriverException) as e:
        LOGGER.debug("could not get errors")
        return[]
    errors=[]
    for entry in browserlogs:
        if entry['level']=='SEVERE':
            errors.append(entry)
        return errors

def validations(driver,file):
    url = driver.current_url
    r=requests.get(url)
    stCode=r.status_code
    resTime=responsetime(driver)
    conserr=consoleErrors(driver)
    file.write("HTTP response Code: "+str(stCode)+"\nResponse time: "+str(resTime)+"ms\nconsole Errors:\n")
    if ((conserr)!=[]):
        file.write(str(conserr)+"\n")
    else:
        file.write('none\n')
    if(stCode!=200 or resTime>10000 or (conserr)!=[]):
        return False
    else:
        return True
    
def signIn(driver,email,password):  
    login= driver.find_element_by_link_text('Login')
    login.click()
    time.sleep(1)
    mail=driver.find_element_by_id('email')
    pswrd=driver.find_element_by_id('password')
    SIbtn=driver.find_element_by_css_selector('button.log-btn')
    mail.send_keys(email)
    pswrd.send_keys(password)
    SIbtn.click()

def test1():
    with open("testResults.txt","a") as f:
        f.write(str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))+" Test 1\n")
        driver=webdriver.Chrome()
        driver.get('https://atg.party')
        if(not validations(driver,f)):
            f.write("Failed\n")
            print('test1 Failed')
            return 
        signIn(driver,'hello@atg.world','Pass@123')
        f.write("Passed\n")
        print("test1 Passed")
        f.close()
def test2():
    with open("testResults.txt","a") as f:
        f.write("\n"+str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))+" Test 2\n")
        driver=webdriver.Chrome()
        driver.get('https://atg.party')
        if(not validations(driver,f)):
            f.write("Failed\n")
            print('test2 Failed')
            return 
        signIn(driver,'hello@atg.world','Pass@123')
        time.sleep(4)
        driver.get('https://www.atg.party/article')
        '''if(not validations(driver,f)):
            f.write("Failed")
            print('test2 Failed')
            return'''
        title = driver.find_element_by_id("title")
        title.send_keys("selinum Test")
        textarea = driver.find_element_by_class_name("fr-element")
        textarea.send_keys("It's a test!\nto post")
        postbtn = driver.find_element_by_id('featurebutton')
        postbtn.click()
        f.write("Passed\n")
        print("test2 Passed :)")
        f.close()
    
