#切片
#利用切片操作，实现一个trim()函数
#去除字符串首尾的空格，注意不要调用str的strip()方法:
#使用递归函数
def trim(str):
    if (str==''):
        return str
    elif (str[0]!=' ') and (str[-1]!=' '):
        return str
    elif str[0]==' ':
        return trim(str[1:])
    else:
        return trim(str[0:-1])

def main():
    if trim('hello ') != 'hello':
        print ('测试失败')
    elif trim(' hello') != 'hello':
        print ('测试失败')
    elif trim(' hello ') != 'hello':
        print ('测试失败')
    elif trim(' hello world ') != 'hello world':
        print ('测试失败')
    elif trim('  ') !='':
        print ('测试失败')
    else:
        print ('测试成功')

if __name__ == '__main__':
    main()
