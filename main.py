import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import rd;

for i in range(1):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)

    #brower = webdriver.Chrome('C:/Users/Hoang Nguyen/Desktop/auto/chromedriver.exe')
    brower = driver
    brower.get('https://facebook.com/login')

    user = brower.find_element_by_id("email")
    user.send_keys("0358259167")
    passwd = brower.find_element_by_id("pass")
    passwd.send_keys("matkhau")
    passwd.send_keys(Keys.ENTER)
    time.sleep(2)
    brower.get('https://www.facebook.com/pages/creation?ref_type=launch_point')
    time.sleep(5)
    namepage = brower.find_element_by_id("jsc_c_p")
    namepage.send_keys(rd.name())
    namepage1 = brower.find_element_by_id("jsc_c_t")
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
    time.sleep(3)
    cl1 = brower.find_elements_by_id('js_6')
    cl1.send_keys("h")
    time.sleep(2)
    cl1.send_keys(Keys.DOWN)
    time.sleep(1)
    cl1.send_keys(Keys.ENTER)
    cl2 = brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div[4]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/a')
    cl2.click()
    time.sleep(1)
    cl2.send_keys(Keys.DOWN)
    time.sleep(1)
    cl2.send_keys(Keys.ENTER)
    cl3 = brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div[4]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/button')
    cl3.click()