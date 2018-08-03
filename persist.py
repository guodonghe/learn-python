try:
    while True:
        n = input("请输入一个小数: ")
        m = 1.0
        for i in range(365):
            if i % 7 in [5,6,0]:
                m = m
            else:
                m *= (1+eval(n))
        print ("一年累计努力值是原来的{:.3f}倍".format(m))
except:
    print ("输入有误,请输入一个小数")
