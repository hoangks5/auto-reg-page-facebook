import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import rd;
import pyautogui as pg

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
for i in range(1):

    #brower = webdriver.Chrome('C:/Users/Hoang Nguyen/Desktop/auto/chromedriver.exe')
    brower = driver
    brower.maximize_window()
    brower.get('https://facebook.com/login')

    user = brower.find_element_by_id("email")
    user.send_keys("0358259xxx")
    passwd = brower.find_element_by_id("pass")
    passwd.send_keys("matkhau")
    passwd.send_keys(Keys.ENTER)
    time.sleep(2)
    brower.get('https://www.facebook.com/pages/creation?ref_type=launch_point')
    time.sleep(5)
    namepage = brower.find_element_by_id("jsc_c_q")
    namepage.send_keys(rd.name())
    namepage1 = brower.find_element_by_id("jsc_c_v")
    namepage1.send_keys("Bất động sản")
    time.sleep(1)
    namepage1.send_keys(Keys.DOWN)
    time.sleep(1)
    namepage1.send_keys(Keys.ENTER)
    done = brower.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div/div')
    done.click()
    time.sleep(10)
    done1 = brower.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div/div/div')
    done1.click()
    time.sleep(5)
    brower.get(brower.current_url+"/settings/?tab=admin_roles")
    time.sleep(4)
    pg.click(874,553)
    time.sleep(1)
    pg.hotkey('h')
    time.sleep(2)
    pg.hotkey('down')
    time.sleep(2)
    pg.hotkey('enter')
    pg.click(1377,550)
    time.sleep(1)
    pg.click(1377,527)
    time.sleep(1)
    pg.click(1485,592)
    time.sleep(1)
    pg.typewrite('matkhau',interval= 0.2)
    pg.hotkey('enter')

    chrome_options1 = webdriver.ChromeOptions()
    prefs1 = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options1.add_experimental_option("prefs",prefs1)
    driver1 = webdriver.Chrome(chrome_options=chrome_options1)
    brower1 = driver1
    brower1.get('https://facebook.com/login')
    user1 = brower1.find_element_by_id("email")
    user1.send_keys("0562978xxx")
    passwd1 = brower1.find_element_by_id("pass")
    passwd1.send_keys("matkhau")
    passwd1.send_keys(Keys.ENTER)
    time.sleep(2)
    brower1.get('https://www.facebook.com/pages/?category=invites&ref=notif&notif_id=1629423117903209&notif_t=page_admin_invite')
    time.sleep(3)
    pg.click(581,556)


    
