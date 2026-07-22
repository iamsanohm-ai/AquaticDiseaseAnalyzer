def scan_workbook(workbook):
    results=[]
    for ws in workbook.worksheets:
        results.append({
            "sheet":ws.title,
            "rows":ws.max_row,
            "columns":ws.max_column,
            "merged_cells":len(ws.merged_cells.ranges)
        })
    return results
