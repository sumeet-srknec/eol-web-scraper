from datetime import datetime

def isEOL(date):
    return datetime.strptime(date, "%Y-%m-%d") < datetime.now()
    
    