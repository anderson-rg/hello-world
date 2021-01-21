from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
import eexcel as ee
from fpdf import FPDF



url = 'http://127.0.0.1:6035/main_page'


def search_for(input_string):
    search_box = driver.find_element_by_id('cep')
    search_box.clear()
    search_box.send_keys(input_string)
    search_box.send_keys(Keys.ENTER)
    if search_box:
        print('Search box found!')
    else:
        print('Search box not found')

def print_file(ts):
    get_image = driver.get_screenshot_as_file(ts)
    if get_image:
        print('Screenshot saved')
    else:
        print('Screenshot not saved')




def find_xpath():
    xpath_string = '/html/body/table/tbody/tr[2]/td[1]'
    element = WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, xpath_string)))
    if element:
        print('xpath found!')
    else:
        print('xpath not found!')


def my_pdf(file_list):
    pdf = FPDF()
    for file in file_list:
        pdf.set_font('Arial', '', 12)
        pdf.add_page()
        pdf.cell(2)
        pdf.cell(0, 0, 'filename: ' + file)
        pdf.image(file, 10, 20, 150, 0, 'png')

    pdf.output('results.pdf', 'F')
    print('pdf saved')


spreadsheet_file = 'data.xls'
sheet_name = 'Sheet1'
data_list = ee.read_spreadsheet(spreadsheet_file, sheet_name)
print(data_list)

file_list = []


for data in data_list:
    # now = datetime.now()
    #
    # timestamp = str(datetime.timestamp(now))
    print('Looking for', data)
    driver = webdriver.Firefox()
    driver.get(url)

    if '-' in str(data[0]):
        search_for(data[0])
    else:
        search_for(str(int(data[0])))
    file_name = str(data[0]) + '_1.png'
    print_file(file_name)
    file_list.append(file_name)
    find_xpath()
    file_name = str(data[0]) + '_2.png'
    print_file(file_name)
    file_list.append(file_name)
    print(file_list)
    driver.close()


my_pdf(file_list)












