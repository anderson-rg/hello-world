import xlrd
import openpyxl
from openpyxl import Workbook, load_workbook



def read_spreadsheet(spreadsheet_file, sheet_name):
    workbook = xlrd.open_workbook(spreadsheet_file)
    sheet = workbook.sheet_by_name(sheet_name)

    row_count = sheet.nrows
    col_count = sheet.ncols

    result_data = []

    for curr_row in range(1, row_count, 1):
        row_data = []

        for curr_col in range(1, col_count, 1):
            data = sheet.cell_value(curr_row, curr_col)
            row_data.append(data)

        result_data.append(row_data)

    return result_data

spreadsheet_file = 'data.xls'
sheet_name = 'Sheet1'
float_precision= 'round_trip'
