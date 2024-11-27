from datetime import datetime

def isEOL(date):
    if date in [True, False]:
        return date
    else:
        return datetime.strptime(date, "%Y-%m-%d") < datetime.now()