from openpyxl.worksheet.worksheet import Worksheet

def get_merged_ranges(ws: Worksheet):
    return [str(r) for r in ws.merged_cells.ranges]
