# ------------------------
# Collection
# 리스트(List)
# ------------------------
# li1=[100,200,3.14,'hello',True]
# print(li1)
# print(li1[0])
# print(li1[-5])
# print(li1[-1])
# print(li1[1])
# print(li1[2])
# print(li1[3])
# print(li1[4])
# print(li1[5])

# li2=[1]*5
# print(li2)

# li3=[100,200,300]
# print(f"메모리위치 : {id(li3)}")
# li3=li3+[400,500]
# print(f"메모리위치 : {id(li3)}")
# li3.append(600)
# li3.append(700)
# print(f"메모리위치 : {id(li3)}")
# li3.insert(1,150)
# print(f"메모리위치 : {id(li3)}")
# print(li3)
# print(len(li3))
# print(f" pop 삭제한 값 확인 : {li3.pop()}")
# print(f"삭제이후 확인 :{li3}")
# print(f"remove 삭제한 값 확인 : {li3.remove(300)}")
# print(f"삭제이후 확인 :{li3}")

# ------------------------
# Collection
# 2차원 리스트(중첩 리스트)
# li1[행번호][열번호]
# li1[행번호]
# ------------------------
li1=[
    [100,200,300,350],
    [400,500,600],
    [700,800,900,1000,1100]
]
print(li1[0][0])
print(li1[2][1])
print(li1[2][2])
print(li1[0])
print(li1[1])
print(li1[2])
print(len(li1)) # 행개수
print(len(li1[0])) # 0번째 1차원리스트의 요소개수
print(len(li1[1])) # 1번째 1차원리스트의 요소개수
print(len(li1[2])) # 2번째 1차원리스트의 요소개수