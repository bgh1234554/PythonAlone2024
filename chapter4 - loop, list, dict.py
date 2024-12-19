#리스트
#뒤에 넣을때는 append(), 특정 위치에 넣을때는 insert(index,element)
# 한번에 여러 element 넣을 때는 .extend(LIST) 써야함. + 만 쓰면 실제로 합쳐지지 않음. .extend는 파괴적인 함수, +는 비파괴적임.
a = [1,2,3,4,5]
a.append(6)
a.insert(4,4.5)
print(a)
#내용 지울때는 .pop(index) 아니면 del LIST_NAME(index)
#슬라이싱 [시작:끝:단계] 단계에 -1넣으면 거꾸로 출력함
print(a[::-1])
#값을 입력해서 제거 .remove(val) 여러 개 있으면 제일 앞에 있는 거 하나만 제거함
#전부 지우고 싶으면 .clear(), 정렬시 .sort(reverse=True/False)
a = [1,2,3,4]
b = [*a, *a]
# *하면 a를 전개해서 입력한 것과 똑같은 의미임. 리스트에 요소를 추가할때 비파괴적으로 구현 가능
b = [*a, 5]
c = [*b, 6]
print(b)
print(c)
print(*a) #리스트가 아니라 안에 있는 element를 하나씩 출력함

#딕셔너리 dictionary = {"key":"element"}
dict_a = {"name":"어벤져스","type":"히어로 무비"}
print(dict_a["name"])
print(dict_a["type"])
dict_a["name"]="아쿠아맨"
print(dict_a["name"])

#dict에 새 값 추가 => 그냥 새로 입력하면 됨
dict_a["price"] = "54000"
print(dict_a)
#값 제거
del dict_a["price"]
print(dict_a)
#key가 있는지 in 으로 확인 가능 dictionary.get("Key")로 확인 가능
dict_a["price"] = "54000"
if "price" in dict_a:
    print(dict_a["price"])
print(dict_a.get("type"))

for key in dict_a:
    print(key,":",dict_a[key])

#유닉스 타임 #주석 단축키 ctrl+/
# import time
# number = 0
# target_tick = time.time()+5
# while time.time() < target_tick:
#     number+=1
# print("{}번 반복 성공".format(number))

#enumerate()함수 쓰면 리스트를 index와 element의 튜플로 저장함
example = ["A","B","C"]
for i, value in enumerate(example):
    print("{}번째 값은 {}".format(i,value))

#enumerate()의 딕셔너리 버전으로 items() 메소드가 있음
for key, value in dict_a.items():
    print("{}의 값은 {}".format(key,value))

#리스트 안에 for문 넣어서 삽입할 수도 있음
array = ["사과", "자두", "복숭아", "키위", "바나나", "초콜릿"]
output = [fruit for fruit in array if len(fruit)==2]
fruit = [fruit*2 for fruit in array if fruit!="초콜릿"]
print(output)
print(fruit)

#참고: 들여쓰기 되어있는 조건문에 여러줄 문자열을 만들면 출력시 들여쓰기가 반영되어 들어감.
#괄호 안에 여러줄로 문자열을 적으면 알아서 + 연산 처리된 것처럼 됨
text = (
    "이렇게 입력해도 "
    "한 줄 처리되어 출력됨"
)
print(text)
#join 함수 '구분자'.join(리스트)
print("::".join(["1","2","3","4"]))
print("".join(["1","3","5","7"]))

#next()함수를 적용할 수 있는 요소 interator for 반복자 in 반복할 수 있는 것
numbers = ["1","2","3","4","5"]
r_num = reversed(numbers)
for i in range(len(numbers)):
    print(next(r_num))

#2,8,16진수를 포맷 메서드로 바꿀 수 있음 {:b},{:o},{:x}