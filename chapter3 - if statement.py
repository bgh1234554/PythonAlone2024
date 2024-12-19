#날짜 시간 활용하기
import datetime
now = datetime.datetime.now()
print("현재 시간은 {}년 {}월 {}일 {}시 {}분 {}초입니다.".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

#pass 키워드 -> 미구현 부분 표현하기 위해 사용
#아니면 raise NotImplementedError