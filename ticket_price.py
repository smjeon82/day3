# 입장료: ~7세 무료, 8~13세 500원, 14~19세 1000원,
# 20~64세 2000원, 65~ 무료
age=input('age ?')
age=int(age)
if age >=65:
    price=0
elif age >=20:
    price=2000
elif age >=14:
    price=1000
elif age >=8:
    price=500    
else:
    price=0
print("요금은 "+str(price)+"원")

