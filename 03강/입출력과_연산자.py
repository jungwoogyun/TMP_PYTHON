#-----------------------
# 1.출력 1-1. 이스케이프 문자(Escape Sequence)
#-----------------------
# print("HELLO\nWORLD")
# print("이름:\t나이:")
# print("강사님이 \"집에 갈시간입니다\" 라고 말하셨다 ")
#
# print("하2",)

#-----------------------
# 1.출력 1-2. print() 옵션
#-----------------------
# # 1 기본
# print("A","B","C",end="\n")
# # 2. sep
# print("A","B","C",sep='-')
# # 3. end
# print("A","B","C", end='~')
# print("D")
# print("2025","01","01",sep="/",end="!\n")

#-----------------------
# 2. 문자열 서식화 (Formatting)
# 2-1. % 포맷 (옛 방식)
#-----------------------
# print("나의 이름은 %s 이고 나이는 %d 입니다" % ("홍길동",40.5) )
# print("점수 : %d점 , 평점 : %f" % (90,88.8))
#
# print("%d %o %x" % (255,255,255 ))

# name = "홍길동"
# score = 95
# average = 87.55555
# print(f"{name}님의 점수는 {score}점 입니다")
# print(f"평균 : {average:.2f}")

#-----------------------
# 입력 — input()
#-----------------------
# name = input("이름을 입력하세요 : ")
# age = input("나이를 입력하세요 : ")
# print(f"이름은 {name}, 나이는 {age} 입니다.")

# n1 = input("n1값 입력 : ")
# n2 = input("n2값 입력 : ")
# print(type(n1),type(n2))
# n1 =int(n1) # str->int(자료형변환)
# n2 =int(n2) # str->int(자료형변환)
# print(n1+n2)


#-----------------------
# 4. 연산자(Operator)
#-----------------------
a, b = 150, 240
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(2 * 10)
print(2 ** 10)
print(7 // 2)
print(7 % 2)    # 1.짝홀수 , 2.배수 , 3.범위제한 , 4.끝자리n자리

