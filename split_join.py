# -*- coding: utf-8 -*- 
# split&join的用法
'''
f = open('fname').read()
ls = f.split("$")
print (ls)
'''


ls = ['china','japan','england','american']
f = open('cname','a')
f.write(','.join(ls))
f.close()
