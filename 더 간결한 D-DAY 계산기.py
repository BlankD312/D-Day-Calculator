print('오늘로부터의 D-DAY','',sep='\n')

print('오늘 날짜','',sep='\n')

today_year = int(input('년도: '))
today_month = int(input('월: '))
today_date = int(input('일: '))

print('','그날 날짜','',sep='\n')

the_year = int(input('년도: '))
the_month = int(input('월: '))
the_date = int(input('일: '))

year_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year4_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
today4 = year4_month[:today_month-1]
the_day4 = year4_month[:the_month-1]
what_day = ['월','화','수','목','금','토','일']


def yun(y):
    return y//4-y//100+y//400 #윤년의 정의를 이용한 해당 해까지의 윤년개수 찾는 함수

def today(y,m,d): #그 해의 몇 번째 날인지 찾는 함수(y는 year, m은 month, d는 day를 나타냄)
    if y%4==0:
        return sum(year4_month[:m-1])+d 
    else:
        return sum(year_month[:m-1])+d
        

def order(y,m,d):
    return (y-1)*365+yun(y)+today(m,y,d) #서기 1년 부터 봤을 때 몇번째 날인지 찾는 함수

        
    
print('D-',order(the_month,the_year,the_date)-order(today_month,today_year,today_date),sep='')

print(what_day[order(the_month,the_year,the_date)%7-1],'요일',sep='')


user_input = input('시스템을 종료하려면 Enter키를 누르세요')

#if문을 많이 사용할수록 코드는 길어진다.
#함수를 많이 사용할수록 코드는 간결해진다.
