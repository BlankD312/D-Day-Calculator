user_input = int(input( '아무 수나 입력 하세요: '))
print (user_input//10*10,'이상',user_input//10*10+10,'미만인 수 입니다.',sep='')

#디데이 계산기

print('오늘로부터의 D-DAY')
print('오늘 날짜')
today_year = int(input('년도:'))
today_month = int(input('월:'))
today_date = int(input('일:'))
print('그날 날짜')
the_year = int(input('년도:'))
the_month = int(input('월:'))
the_date = int(input('일:'))

year_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year4_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
today4 = year4_month[:today_month-1]
the_day4 = year4_month[:the_month-1]
today = year_month[:today_month-1]
the_day = year_month[:the_month-1]

if today_year == the_year :
   
    d_day = sum(the_day)+the_date -(sum(today)+today_date)
    print('D-',d_day,sep='')

elif today_year%4==0 and the_year-today_year<4: 
     d_day = 366-(sum(today4)+today_date)+(the_year-today_year-1)*365+sum(the_day)+the_date
     print('D-',d_day,sep='')

elif the_year%4==0 and the_year-today_year<4: 
     d_day = 365-(sum(today)+today_date)+(the_year-today_year-1)*365+sum(the_day4)+the_date
     print('D-',d_day,sep='')
     
elif the_year-today_year<4:
     d_day = 366-(sum(today)+today_date)+(the_year-today_year-1)*365+sum(the_day)+the_date
     print('D-',d_day,sep='')
    
else :
    
    d_day2 = 365-(sum(today)+today_date)+(the_year-today_year-1)*365+sum(the_day)+the_date
    print('D-',d_day2,sep='')
