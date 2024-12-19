#format() 함수 연습
output_practice = "{}   {}".format(10, 40)
print(output_practice)
#공백으로 앞부분 채우기
output_a = "{:5d}".format(52)
output_b = "{:10d}".format(52)
print(output_a)
print(output_b)
#0으로 앞부분 채우기 (숫자는 총 칸수)
output_c = "{:05d}".format(52)
print(output_c)
#숫자 부호 넣기
output_d = "{:+d}".format(52)
#기호 부분 비워두면 입력했을 때만 알아서 입력됨
output_e = "{: d}".format(-52)
print(output_d)
print(output_e)
#기호와 공백 조합시에는 = 사용하여 기호가 앞일지 뒤일지 결정 가능.
output_f = "{:+5d}".format(52)
output_g = "{:=+5d}".format(-52)
print(output_f)
print(output_g)

#float 형태일땐 f 사용. <총 자릿수>.<소숫점 뒤 자리수> 형태로 표현 가능
output_a = "{:15.4f}".format(564.45876)
print(output_a)
#의미없는 0을 지울땐 g 사용.
output_b = "{:g}".format(52.0300)
print(output_b)
#.isOO 메소드로 여러가지 확인할 수 있음.
print("toandsf120".isalnum())

#f 함수 => format의 업그레이드 버전
print("3+4={}".format(3+4))
print(f"3+4={3+4}")
print(f"""3+4={3+4}\n1+6={1+6}\n2+5={2+5}""")

#문자열 자르기 -> split
a="10,20,30,40,50".split(",")
print(a) #리스트 출력