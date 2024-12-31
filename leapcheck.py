def input_date():
    year=int(input("__년도를 입력하시오:"))
    month=int(input("__월을 입력하시오:"))
    day=int(input("__일을 입력하시오:"))
    return year,month,day

def is_leap(year):
    if (year%4==0) and (year%100!=0) or (year%400==0):
        return True
    else:
        return False
        
def get_day_name(year,month,day):
    week=["일요일","월요일","화요일","수요일","목요일","금요일","토요일"]
    month_day={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    total_days=365*(year-1)+sum([1 for i in range(1, year) if is_leap(i) ==True])
    
    if is_leap(year)==True:
        month_day[2]=29
    else:
        if (month,day)==(2,29): return False
    total_days+=sum([month_day[i] for i in range(1,month)])+sum([1 for i in range(day) if day<=month_day[month]])
    return week[total_days%7]
    
if __name__=="__main__":
    year,month,day=input_date()
    day_name=get_day_name(year,month,day)
    if day_name==False:
        print("입력하신 날짜는 존재하지 않습니다.")
    else:
        print(day_name)
        if is_leap(year)==True:
            print("입력하신 %s은 윤년입니다"%year)
