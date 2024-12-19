#원래는 open 하면 .close()로 닫아야 하지만 with 구문을 사용하면 굳이 close를 안써도 됨
#파일이 원하는 위치에 생성되는 것을 원하면 VSCode에서 열려있는 폴더를 잘 선택해야함. 안 그럴시 parent folder에 vscode가 txt 파일을 생성함.

file = open("test.txt","w+",encoding='utf-8')
file.write("Hello Python!")
file.close()

with open("test2.txt","w") as file:
    file.write("Hello World!")

#파일 읽을땐 read() 사용
# with open("test2.txt","r+") as file:
#     contents=file.read()

# print(contents)

# 샘플 파일 만들기
# import random
# hanguls = list("가나다라마바사아자차카타파하")
# with open("info.txt","w+",encoding='utf-8') as file:
#    for i in range(100):
#       name=random.choice(hanguls)+random.choice(hanguls)+random.choice(hanguls)
#       weight=random.randrange(50,120)
#       height=random.randrange(150,200)
#       file.write("{}, {}, {}\n".format(name,weight,height))
# # 한줄씩 읽을 때
# file = open("info.txt","r+",encoding='utf-8')
# resultfile = open("result.txt","w+",encoding='utf-8')
# for line in file:
#   (name, weight, height) = line.strip().split(", ") #strip: Return a copy of the string with leading and trailing whitespace removed.
#   if (not name) or (not weight) or (not height):
#     continue
#   bmi = int(weight) / ((int(height)/100)**2)
#   result = ""
#   if 25 <= bmi:
#     result = "과체중"
#   elif 18.5 <= bmi:
#     result = "정상 체중"
#   else:
#     result = "저체중"
#   print('\n'.join([
#     "이름: {}",
#     "몸무게: {}",
#     "키: {}",
#     "BMI: {}",
#     "결과: {}",
#   ]).format(name,weight,height,bmi,result))
#   resultfile.write("{}, {}, {}, {}, {}\n".format(name,weight,height,bmi,result))
#   print()
# file.close()

# .wrtielines() -> 리스트를 차례로 읽어 알아서 for문 없이 써주는 메소드
# .readline() -> 파일을 개행문자 기준으로 끊어 읽는 메소드
# .readlines() -> 파일을 통으로 읽어서 for문 없이 알아서 리스트로 리턴해주는 메소드
# 참조: https://rfriend.tistory.com/524

matrix_quotes = ["The Matrix is the world that has been pulled over your eyes to blind you from the truth.\n",
                 "You have to let it all go, Neo. Fear, doubt, and disblief. Free your mind.\n",
                "There is a difference between knowing the path and walking the path.\n",
                "Welcome to the desert of the real!\n"]

# with open("matrixquote.text","w") as file:
#    for line in matrix_quotes:
#       file.write(line)

# with open("matrixquote.text","w") as file:
#    file.writelines(matrix_quotes)

#둘이 같은 기능을 함

# with open("matrixquote.text","r") as file:
#     lines=[]
#     line=file.readline()
#     while line != "":
#         lines.append(line)
#         line=file.readline()
#     print(lines)

# with open("matrixquote.text","r") as file:
#     lines=file.readlines()
#     print(lines)

#위의 둘은 같은 기능을 함

# file.seek() -> 커서 움직이는 거랑 비슷한 기능임
# seek(기준점(바이트로), 거기서 얼마나 움직이는지)

# 제너레이터 -> 이터레이터를 직접 만들 때 사용. next()함수를 이용해 내부 코드를 실행함.
# 함수 내에 yield 키워드를 사용함으로써 만들 수 있음.

# 리스트 내에 dictionary가 들어가 있어 그것의 최대 최소를 비교할때는, 비교 기준을 세울 수 있는 key 함수를 만듬으로서 구현할 수 있음.
# print(min(books, key=price)) #books = [{"제목"="무엇","가격"="얼마"},...] def price(book): return book["가격"]
# print(min(books, key=lambda book: book["가격"]))
# sort 함수에서도 똑같은 방식을 사용할 수 있음.

#하노이탑 알고리즘
import time
count=0
def HanoiTower(n,start,end,suff):
    global count
    if n==1:
        count+=1
        print("{}->{}".format(start,end))
    if n>=2:
        HanoiTower(n-1,start,suff,end)
        count+=1
        print("{}->{}".format(start,end))
        HanoiTower(n-1,suff,end,start)

n = int(input("How many stacks do you have?"))
st = float(time.time())
HanoiTower(n,"Left","Middle","Right")
print(f"You moved it {count} times")
fin = float(time.time())
print("It took around","{:.4f}".format(fin-st),"seconds to calculate that")