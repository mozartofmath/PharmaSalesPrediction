def weekends(x):
    if x >= 6:
        return 1
    return 0

def time_of_month(x):
    if x <= 10:
        return 0
    if x <= 20:
        return 1
    return 2

def label_holidays(x):
    if x in [0,'0','a','b','c']:
        return [0,'0','a','b','c'].index(x)
    return 5