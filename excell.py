import xlrd
from openpyxl import Workbook, load_workbook
import os

Excel_file = 'C:\\Users\\AndersonGuilherme\\Desktop\\sheets\\testepy.xlsx'
Excel_worksheet = 'Sheet1'

def read_spreadsheet(Excel_file, Excel_worksheet):
    workbook = xlrd.open_workbook(Excel_file)
    sheet = workbook.sheet_by_name(Excel_worksheet)

    row_count = sheet.nrows
    col_count = sheet.ncols

    result_data = []

    for curr_row in range (1, row_count, 1):
        row_data = []

        for curr_row in range (1, col_count, 1):

            for curr_col in range(1, col_count, 1):
                data = sheet.cell_value(curr_row, curr_col)
                row_data.append(data)

            result_data.append(row_data)

        return result_data
