from openpyxl import load_workbook

def open_workbook(path):
    return load_workbook(path, data_only=True)
