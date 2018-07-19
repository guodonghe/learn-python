import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.18.70',port=22,username='guosai',password='guosai')
stdin,stdout,stderr = ssh.exec_command("ifconfig")
a = stdout.read().decode()
print (a)
ssh.close()
        
