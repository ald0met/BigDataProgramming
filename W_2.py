import sys
from datetime import datetime

if __name__=="__main__":
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])

    date = datetime(year, month, day)

    weekday_kr = {
        0: '월요일',
        1: '화요일',
        2: '수요일',
        3: '목요일',
        4: '금요일',
        5: '토요일',
        6: '일요일'
    }

print(weekday_kr[date.weekday()])
