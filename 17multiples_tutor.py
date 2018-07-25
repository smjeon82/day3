# 1~1000 사이의 17의 배수 구하기
count=0;total=0;nlist=[]
for number in range(1,1001) :
    if number%71==0 :
        count=count+1
        total+=number
        nlist.append(number)
print('17의 배수는: '+str(nlist))
print('17의 배수 갯수: '+str(count))
print('17의 배수의 합: '+str(total))

