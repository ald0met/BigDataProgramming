import sys

def is_leap(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

def get_day_name(year,month,day):
    day_name=["일요일","월요일","화요일","수요일","목요일","금요일","토요일"]
    month_date={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if is_leap(year)==True:
        month_date[2]=29
    else:
        if (month,day)==(2,29):
            return False
    count=365*(year-1)+sum(1 for i in range(1,year) if is_leap(i)==True)
    count+=sum(month_date[i] for i in range(1,month))
    count+=day
    return day_name[count%7]
if __name__=="__main__":
    year=int(sys.argv[1])
    month=int(sys.argv[2])
    day=int(sys.argv[3])
    day_name=get_day_name(year,month,day)
    if day_name==False:
        print("입력하신 날짜는 존재하지 않습니다.")
    else:
        print(day_name)
