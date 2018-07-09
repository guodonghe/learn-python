str=input()
fact = 1
sum = 0
if str.isdigit():
    if int(str) > 0:
        n = int(str)
        for i in range(1,n+1):
            fact = fact*i
            sum = sum + fact
        print (sum)
    else:
        print ("输入有误，请输入正整数")
else:
    print ("输入有误，请输入正整数")
