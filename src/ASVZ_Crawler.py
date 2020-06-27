import datetime
import os
import time
import re
import KEYS

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options


def page_has_loaded_id(browser, old_page):
    try:
        new_page = browser.find_element_by_tag_name('html')
        return new_page.id != old_page.id
    except NoSuchElementException:
        return False

def init_page(webpage, register):
    # get paths of geckodriver and Firefox exe
    # gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    # binary = ChromeBinary(r'/home/pi/Desktop/ASVZ_Crawler/chromedriver')
    # Using Firefox to access web
    # driver = webdriver.Firefox()
    # Open the website
    # driver.get(webpage)
    
    # do some magic, otherwise it wont work
    # driver.switch_to.default_content()

    options = Options()
    options.log.level = "trace"
    options.add_argument("--headless")

    # browser = webdriver.Firefox(firefox_options=options)
    driver = webdriver.Firefox()
    driver.get(webpage)
    old_page = driver.find_element_by_tag_name('html')

    # while is escaped when moving to second page
    while not page_has_loaded_id(driver, old_page):
        # Find Login Button
        button_list = driver.find_elements_by_tag_name('button')
        login_button = button_list[0]
        for b in button_list:
            if 'Login' in b.get_attribute('title'):
                login_button = b
        # Click login
        login_button.click()

    old_page = driver.find_element_by_tag_name('html')
    # while is escaped when moving to second page
    while not page_has_loaded_id(driver, old_page):
        # Find Login SwitchAai Button
        switch_button = driver.find_element_by_name("provider")
        switch_button.click()

    old_page = driver.find_element_by_tag_name('html')
    while not page_has_loaded_id(driver, old_page):
        # click on ETH in Dropdown
        select_arrow = driver.find_element_by_id('userIdPSelection_iddtext')
        select_arrow.click()

        uni_box = driver.find_element_by_id('userIdPSelection_iddtext')
        uni_box.send_keys('ETH Zurich')

        select_key = driver.find_element_by_name('Select')
        select_key.click()

    # Fill out username and password field
    input_username = driver.find_element_by_id('username')
    input_username.send_keys(KEYS.USERNAME)
    input_password = driver.find_element_by_id('password')
    input_password.send_keys(KEYS.PASSWORD)

    # submit data
    final_login_button = driver.find_element_by_name('_eventId_proceed')
    final_login_button.click()

    # wait for reload to complete
    while not webpage in driver.current_url:
        time.sleep(10)

    # get Register-opens time
    driver.implicitly_wait(10)  # seconds
    description_text = driver.find_elements_by_class_name('ng-star-inserted')
    register_opens = datetime.datetime.now()
    for texts in description_text:
        if "Online-Einschreibungen" in texts.text:
            text = texts.text.split('Online-Einschreibungen koennen ab ')
            register_opens = datetime.datetime.strptime(text[0:16], "%d.%m.%Y %H:%M")
            return register_opens
            break
        break

    if register:
        # click on register button
        register_button = driver.find_element_by_id('btnRegister')
        register_button.click()
    driver.quit()


if __name__ == "__main__":


    options = Options()
    options.log.level = "trace"
    options.add_argument("--headless")

    # browser = webdriver.Firefox(firefox_options=options)
    browser = webdriver.Firefox()
    browser.get('https://schalter.asvz.ch/tn/lessons/116834')

    # driver = webdriver.Firefox()
    # driver.get('www.google.com')
    # init_page('https://schalter.asvz.ch/tn/lessons/116834', False)

