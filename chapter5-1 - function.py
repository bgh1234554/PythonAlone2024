#가변 매개변수 * 기호 사용해서 만들 수 있음. -> 여러 개의 변수를 원하는 만큼 받기 가능, 뒤에 일반 변수 올 수 없음.

# values = ["즐거운","파이썬","프로그래밍"]
# def printNTimes(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# i = int(input("몇번 반복하고 싶나요?"))
# printNTimes(i,*values)

#가변 매개변수와 기본 매개변수 (함수 뒤에 옵션으로 A=b 이런식으로 있는 것)을 동시에 사용할땐,
#기본 매개변수 사용 시 A=n 이런 방식으로 직접 지정해야함.

# def printNTimes (*values, n=2):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# printNTimes("지금부터는","제가","정리한 글을",n=3)

# def test(a,b=100,c=20):
#     print(a+b+c)

# test(10,b=50,c=22)
# test(1)

#함수 외부에 있는 변수를 함수 내부에서 참조하고 싶을 때 global 키워드 사용

#메모이제이션 (완전 중요!!)
fibodic = [0,1,1]
#array에 미리 저장
def fibonacci(n):
    if n < len(fibodic): #이미 있는 경우 고대로 리턴
        # print(n,"번째 피보나치 수 찾음.")
        return fibodic[n]
    else: #없으면 계산해서
        ans = fibonacci(n-2)+fibonacci(n-1)
        fibodic.append(ans) #메모리에 저장
        return ans

print(fibonacci(1))
print(fibonacci(20))
print(fibonacci(50))
print(fibonacci(100))

#리스트 중첩화 푸는 재귀함수 만들어보기
def flatten(data):
    output=[]
    for i in data:
        if type(i)==list:
            output += flatten(i) #리스트를 리스트에 추가할때는 + 기호 또는 extend 메소드 사용
        else:
            output.append(i)
    return output

print(flatten([[1,2],3,[[4,5],6],[7,[8,9,[10,[11,12,[13,14],15],16],17],18],19]))

#모든 사람이 테이블에 나눠 앉는 경우의 수 구하는 재귀함수 문제
MIN_PERSON = 2
MAX_PERSON = 10
TOTAL = 100
memo = {

}

def way(PeopleLeft,PeopleSit):
    key = str([PeopleLeft,PeopleSit])
    if key in memo:
        return memo[key]
    if PeopleLeft<0:
        return 0 #무효니까 0 리턴
    if PeopleLeft==0:
        return 1 #유효하기 때문에 경우의 수로 추가 #다 앉아서 남은 사람 없다는 뜻.
    count = 0
    for i in range(PeopleSit,MAX_PERSON+1): #테이블 하나에 이미 2명이 최소 앉아야 하니까, 일단 2명 앉히고 계산해보는거지.
        count += way(PeopleLeft-i,i) #그 다음 테이블에는 2~10명 앉힐 수 있으니까 앉혀보고 재귀
    memo[key] = count
    return count

print(way(TOTAL,MIN_PERSON))

#튜플 하나짜리로 만들때는 (value, )와 같은 방식으로 만들어야함.
#함수가 여러개의 값을 리턴하고 싶게 만들 때 튜플 사용.
#lambda x: x*x (lambda 매개변수: 리턴값)
#map(함수, 리스트) 리스트를 함수에 넣고 리턴값으로 다시 리스트를 뽑아내줌
#filter(함수, 리스트) 리스트를 함수에 넣고 True 값을 반환하는 것만 리스트에 넣어서 반환해줌
