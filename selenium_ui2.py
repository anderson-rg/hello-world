from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
import time

url = 'http://127.0.0.1:6035/main_page'
driver = webdriver.Firefox()
driver.get(url)


def search_for():
    search_box = driver.find_element_by_xpath("//input[@name='cep']")
    search_box.clear()
    search_box.send_keys('13504056')
    search_box.send_keys(Keys.ENTER)
    if search_box:
        print('Search box found!')
    else:
        print('Search box not found')

search_for()

def find_xpath():
    xpath_string = '/html/body/table/tbody/tr[2]/td[1]'
    element = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, xpath_string)))
    if element:
        print('xpath found!')
    else:
        print('xpath not found!')
find_xpath()


        # xpath_string = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/th[1]')
    # print(str(xpath_string))






# try:
#     # driver.find_elements_by_partial_link_text('')
#     driver.find_element_by_xpath("//input[@type='submit']")
#     # driver.find_element_by_id('cep')
#     # driver.find_element_by_name('cep')
#     # driver.find_element_by_css_selector("input[id='cep'][type='text']")
#     print('Test Pass: Link text by XPath found')
#
# except Exception as e:
#     print('Exception found',format(e))



