# 기본으로 존재하는 모듈 소개
import math, random, sys, os, datetime, time
# from math import 원하는 함수 
# import random as r (alias 지정 가능)
random.choice([1,2,3,4,5])
random.sample([1,2,3,4,5],2)
random.uniform(123.4,3443.2) #float 형식 리턴
random.random() #0~1사이의 숫자 리턴
random.randrange(213,423) #정수만 리턴
random.shuffle([1,2,3,4,5]) #섞을때 사용

print(sys.argv) #파이썬 cmd에서 명령 매개변수를 불러올 때 사용.

os.system("dir /w") #괄호 안에 명령어를 넣어 고대로 실행할때 사용.
print(os.name)
print(os.getcwd())
print(os.listdir())
os.mkdir("hello")
os.rmdir("hello")
# with open("original.txt","w+") as file:
#     file.write("hello!")
# os.rename("original.txt","new.txt")

#os.remove("new.txt")

now = datetime.datetime.now()
year, month, day, hour, minute, second = now.year, now.month, now.day, now.hour, now.minute, now.second
now.replace(year=now.year+1) #특정 시간 요소 교체하기 
after = now + datetime.timedelta(weeks=1,hours=1,minutes=1,seconds=10,days=23) #특정 시간 이전 이후 구하는 함수. 년도는 안되니까 replace 함수로 아예 새로운 날짜 설정함.
print(after.strftime("%Y{}, %m{}, %d{}, %H{}, %M{}, %S{}").format(*"년월일시분초")) #strftime() 시간을 형식에 맞춰 출력 

# time.sleep(5) # 5초간 정지함

# from urllib import request

# target = request.urlopen("https://google.com")
# output=target.read()

# print(output) #웹페이지에 있는 내용을 읽어서 출력

# #itemgetter: 특정 요소를 추출하는 함수를 만드는 함수. lambda보다 이해하기 쉬워서 많이 사용함.
# books = [{"제목":"혼공파","가격":18000,"리뷰":5}]
# from operator import itemgetter
# print(min(books,key=itemgetter("가격")))

#폴더라면 모두 탐색하기
def read_folder(path):
    output=os.listdir(path) #listdir - 현재 폴더에 있는 내용을 리턴함
    for item in output:
        if os.path.isdir(item):
            read_folder(path+"/"+item)
        else:
            print("파일:", item)

read_folder(".")

#외부모듈 까는 법
#cmd에 pip install 모듈이름