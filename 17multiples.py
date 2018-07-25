# 1~1000 사이의 17의 배수 구하기
mul17=[]
for num in range(1,1001) :
    if num%79==0 :
        mul17.append(num)
print(mul17)
len(mul17)
