import paramiko
import random


print("выбрать файл с ip:\n")


while 1:
    file1 = input("1)sup1_shared_hosting.txt\n2)sup2_ipSSH.txt\n")
    if file1 == "1":
        file1 = "sup1_shared_hosting.txt"
        break
    if file1 == "2": 
        file1 = "sup2_ipSSH.txt"
        break


file = open(file1)
onstring = file.read().split("\n")[:-1]
print(onstring)
host = onstring


for hostn in host:
    
    secret = input('\nConnecting to: {0}.......\
            \nВведите пароль:\n'.format(hostn))
    
    port = input('Введите порт(def 2222):')
    if port is "":
        port = '2222'
    
    user = input('Введие имя юзера(def root):')
    if user is "":
        user = 'root'
    
    
    password = ''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@!#(){}[]')) for x in range(15)])
    command = "echo -e '{0}\n{0}\n'| passwd".format(password)
    
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    
    try:
    
        client.connect(hostname=hostn, username=user, password=secret, port=port)
    
    except paramiko.ssh_exception.AuthenticationException:
        print("неправельный пароль(пропускаем ip)")
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
        continue
    
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("неправельный порт(пропускаем ip)")
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
        continue
    
    
    stdin, stdout, stderr = client.exec_command(command)
    for line in stdout:
            print('... ' + line.strip('\n'))
    print("new password is: {0} /  {1}".format(hostn,password))
    print("\n=========================================================\n")

    
client.close()
