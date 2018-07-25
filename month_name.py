#월(숫자)을 입력하면 해당하는 월의 영문명을 출력하는 프로그램

month_name={1:'January',2:'February',3:'March', 4:'April', 5:'May', 6:'June'}
inpt=input('월을 입력하세요 ')
print(month_name[int(inpt)])
month_name[13]='Rest'
print(month_name)
del month_name[5]
print(month_name)
