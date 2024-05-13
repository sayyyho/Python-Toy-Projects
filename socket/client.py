from socket import *
import threading
import time

SERVER_IP = '127.0.0.1'
SERVER_PORT = 9123

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

print(f"연결완료 !!\nip : {SERVER_IP}, port : {SERVER_PORT}")
print("if you want to close server, please enter <<< quit >>>")

def send(client_socket):
    while True:
        msg = input("(you) >> ")
        client_socket.sendall(msg.encode("utf-8"))
        if msg == "quit": 
            print("socket is closed. please enter key <<< control + c or control + d >>>")        
            client_socket.close()
            break
        
def receive(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode("utf-8")
            print("\n[from server]")
            if not msg or msg == "quit": 
                print("socket is closed. please enter key <<< control + c or control + d >>>")        
                client_socket.close()
                break
            print(f">> {msg}\n(you) >> ", end="")
        except:
            pass

sending = threading.Thread(target=send, args=(client_socket,))
receiving = threading.Thread(target=receive, args=(client_socket,))
sending.daemon = True
receiving.daemon = True
sending.start()
receiving.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        client_socket.close()
        break
print("\n프로그램 종료")