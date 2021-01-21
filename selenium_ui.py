from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url = 'http://127.0.0.1:6035/main_page'
driver = webdriver.Firefox()
driver.get(url)

element_name ='cep'

# search_box = driver.find_element_by_name(element_name)
#
# search_box.clear()
# search_box.send_keys('13504056')
# search_box.send_keys(Keys.ENTER)
#
def search_for(driver, search_string, element_name):
    search_box = driver.find_element_by_name(element_name)
    search_box.clear()
    search_box.send_keys('13504056')
    search_box.send_keys(Keys.ENTER)
search_for(driver, '13504056', element_name)

#
#
# time.sleep(15)
# driver.close()

try:
    # driver.find_element_by_xpath("//input[@type='submit']")
    # driver.find_element_by_id('cep')
    # driver.find_element_by_name('cep')
    driver.find_element_by_css_selector("input[id='cep'][type='text']")
    print('Test Pass: Link text by XPath found')

except Exception as e:
    print('Exception found' ,format(e))
