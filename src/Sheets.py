import gspread
# TODO figure out import from parent folder (config should not be in src)
import config

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key(config.googleSheets['url'])


def insertIntoWorksheet(worksheetName, firstRow, data):
    worksheet = sh.add_worksheet(worksheetName, 100, 100, 0)
    worksheet.insert_row(firstRow)
    worksheet.insert_rows(data, 2)