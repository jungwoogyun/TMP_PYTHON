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
# a, b = 150, 240
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(2 * 10)
# print(2 ** 10)
# print(7 // 2)
# print(7 % 2)    # 1.짝홀수 , 2.배수 , 3.범위제한 , 4.끝자리n자리

# n = int(input("n 입력 : "))
# print(f"n : {n}")
# # 홀짝수
# if n%2 == 0 :
#     print(f"{n}은 짝수 입니다")
# else :
#     print(f"{n}은 홀수 입니다")
# print("------")
#
# # 배수 구분
# if n%3 == 0 :
#     print(f"{n}은 3의 배수 입니다.")
#
# # 자리수 확인(n에 1234 입력)
# print("오른쪽 1자리 : ",n%10)
# print("오른쪽 2자리 : ",n%100)
# print("오른쪽 3자리 : ",n%1000)

# # 수의 범위 제한
# import random
# import time
#
# while True:
#     num=random.randint(1,100)
#     print(f"랜덤값 : {num} 제한 0~5 :{num%6}" )
#     time.sleep(0.5)

#-----------------------
# 4. 연산자(Operator)
# 4-3. 대입(복합 대입) 연산자
#-----------------------
# a = 10
# a += 2
# a -= 2
# a *= 2
# a **= 2
# a /= 2
# a //= 3
# a %= 7

#-----------------------
# 4. 연산자(Operator)
# 4-4. 관계(비교) 연산자
#-----------------------
# n=int(input("n입력 : "))
# print(n>10)
# print(n>=10)
# print(n<10)
# print(n<=10)
# print(n==10)
# print(n!=10)

#-----------------------
# 4. 연산자(Operator)
# 4-5. 논리 연산자
#-----------------------
# print(True and False)
# print(True or False)
# print(not True)
# print(5 > 3 and 2 < 1)


# n=int(input("n입력 : "))
# if n%2==0:
#     print(f"{n}은 짝수")
#     if n%3==0:
#         print(f"{n}은 3의배수")

# if n%2==0 and n%3==0:
#     print(f"{n}은 짝수 이면서 3의 배수")
#
# if n%2==0 or n%3==0:
#     print(f"{n}은 짝수 이거나 3의 배수")

#-----------------------
# 5. 비트 연산자(Bitwise)
#-----------------------
# a=15    # 00001111
# b=11    # 00001011
# print(a&b) #00001011
# print(a|b) #00001111
# print(a^b) #00000000
# print(a << 2)
# print(a >> 2)

#-----------------------
# 6. 시퀀스 연산자 (+ , *)
#-----------------------
# arr1=[1,3,5]
# arr2=[2,4,6]
# arr3=arr1+arr2
# print(arr3)
# arr4=arr1*3
# print(arr4)
#
# print(type(arr3),type(arr4))


#-----------------------
# 8. 형변환(Type Casting)
#-----------------------
# print(int("10")+5)
# print(float("3.14")+1.1)
# print(str(100)+"점")
# print(int(3.9))
# print(bool(0),bool(1))


