import getpass

def check_user(user,password):
    if user == 'guo' and password == '123456':
        print('UserName: %s; Password: %s' % (user,password))
        return True
    else:
        return False
if __name__ == "__main__":
    usr = getpass.getuser()
    pwd = getpass.getpass('Input the passwd:')

    if check_user(usr,pwd):
        print ('OK!')
    else:
        print ('ERROR!')
