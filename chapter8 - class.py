class Student:
    def __init__(self, name, korean, math, english, science): #self가 자바의 this같은거. 무조건 처음에 넣어야함 파이썬에선.
        #__<이름>__ 형태의 특수한 형태가 많은데, 이는 보통 자동 호출되는 함수들이 많음
        #예를 들어, __str__을 따로 정의하면 str(Student)할 시 어떻게 출력될지 정할 수 있음.
        #자바랑 달리 클래스 생성자는 한개로만 할 수 있으며, 여러개를 원할 시 다른 클래스 함수로서 구현해야함.
        self.__name = name #파이썬에서는 private 변수 만들때 키워드 대신 __<변수이름>을 사용함.
        self.__korean = korean
        self.__math = math
        self.__english = english
        self.__science = science
    def __del__(self): #가비지 컬렉터로 인해 메모리에서 지워질때 실행됨.
        print("Data of {} has been deleted".format(self.__name))
    def get_sum(self):
        return self.__korean+self.__math+self.__english+self.__science
    def get_average(self):
        return self.get_sum(self)/4
    def __str__(self):
        return "{}\t{}\t,{}".format(self.__name,self.get_sum,self.get_average)
    def __eq__(self, value):
        if not isinstance(value,Student):
            raise TypeError("You can only compare between Student classes")
        return self.get_sum()==value.get_sum()
    # ne, gt, ge, lt, le도 있음 다 부등호 관련임.
    @classmethod #인스턴스 함수와 다르게 클래스 함수는 이렇게 데코레이터를 붙여서 활용함.
    def print(cls):
        print("List of Students")
        print("-----------------")
        print("Name\tSum\tAverage")
        for student in cls.students:
            print(str(student))
        print("-----------------")
    
student = Student("baek",75,100,97.5,100)
print(isinstance(student,Student)) #type하고 비슷하나 상속 시 return 값이 달라짐. isinstance는 상속까지 포함해서 계산함.

import math
class Circle:
    def __init__(self, radius):
        if radius<0:
            raise TypeError("You can only have positive number as a radius of a circle")
        self.__radius = radius
    def get_circumferenfe(self):
        return 2*math.pi*self.__radius
    def get_area(self):
        return math.pi*(self.__radius**2)
    # 파이썬은 게터랑 세터 쓸일 많기 때문에 데코레이터로 제공함. 변수이름과 같은 함수위에 게터 함수와 같은 기능을 지니도록 @property, 이후 세터함수에 @<변수이름>.setter라고 하면 됨.
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,value):
        if value<=0:
            raise TypeError("You can only have positive number as a radius of a circle")
        self.__radius=value
    #이렇게 하면 굳이 게터 세터함수 메서드로 안쓰고 그냥 cirle.radius=2 이런식으로 적어도 세터함수를 쓴 것과 같은 효과를 낼 수 있음.
    # def get_radius(self):
    #     return self.__radius
    # def set_radius(self,value):
    #     if not (isinstance(self,float) or isinstance(self.int)):
    #         raise TypeError("you should enter int or float")
    #     if value <=0:
    #         raise TypeError("You can only have positive number for radius")
    #     self.__radius=value

    #파이썬에서는 상속 구문이 굉장히 간단함.
class Parent:
    def __init__(self):
        self.value="test"
    def test(self):
        print("Parent class method")

class Child(Parent): #다른 부분
    def __init__(self):
        super().__init__() #부모님의 __init__()함수 호출
        print("Called __init__ method of Parent Class")
    #당연히 이 외에도 부모 클래스에 있는 메소드를 재정의 하거나, 부모 클래스에는 없는 새로운 메소드를 정의하는 것도 가능하다.\

class CustomException(Exception):
    def __init__(self,message,value):
        super().__init__()
        self.message=message
        self.value=value
        print("CustomException generated")
    def __str__(self):
        return "There's an Error - " + self.message
    def print(self):
        print("Error Info")
        print("Message:", self.message)
        print("Value:",self.value)
# raise CustomException
try:
    raise CustomException("No Reason", 273)
except CustomException as e:
    e.print()
    print(str(e))

#StudentList 클래스 구현해보기
class StudentTwo:
    def __init__(self,name,score):
        self.name=name
        self.score=score

class StudentList:
    def __init__(self):
        self.students=[]
    def append(self,student):
        self.students.append(student)
    def average(self):
        totalscore=0
        for student in self.students:
            totalscore+=student.score
        return totalscore/len(self.students)
    def get_first_by_score(self):
        return max(self.students,key=lambda x:x.score)
    def get_last_by_score(self):
        return min(self.students,key=lambda x:x.score)
students = StudentList()
students.append(StudentTwo("baek",100))
students.append(StudentTwo("Mike",34))
students.append(StudentTwo("Racoon",89))
students.append(StudentTwo("Shaun",15))

print("Students' average score is",students.average())
print("The best student is",students.get_first_by_score().name)
print("The worst student is",students.get_last_by_score().name)