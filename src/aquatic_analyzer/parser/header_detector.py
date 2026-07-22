HEADER_HINTS={"จังหวัด","ภาค","จำนวนฟาร์มที่เฝ้าระวัง","EHP","VpAHPND","WSSV"}

def detect_header(ws, max_scan=10):
    best_row=1
    best_score=-1
    for r in range(1,min(max_scan,ws.max_row)+1):
        score=0
        for c in ws[r]:
            if c.value and str(c.value).strip() in HEADER_HINTS:
                score+=1
        if score>best_score:
            best_score=score
            best_row=r
    return best_row,best_score
