from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target,"html.parser")

for location in soup.select("location"):
    print("City:", location.select_one("city").string)
    print("Weather:",location.select_one("wf").string)
    print("MinTemp:",location.select_one("tmn").string)
    print("MaxTemp:",location.select_one("tmx").string)
    print("RainProbability:",location.select_one("rnSt").string)

# fom flask import Flask #함수를 실행해 웹에 띄움. 웹 서버 만들 때 사용
# 실행시 터미널에
# $env:FLASK_APP="파일 이름"
# flask run
# 입력해줘야함
# __name__=="__main__" => 현재 이 파일이 모듈로서 실행되는지 엔트리포인트로서 실행되는지 체크하기 위함
target=request.urlopen("https://tmssl.akamaized.net//images/wappen/head/1005.png?lm=1689169528")
output=target.read()
file = open("output.png","wb")
file.write(output)
file.close()

#이미지 저장하는 방법 (바이너리 데이터니까)