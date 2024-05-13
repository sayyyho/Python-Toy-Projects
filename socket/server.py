from socket import *
import threading
import time

host = "127.0.0.1"
port = 9123

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind((host, port))

print("server에서 listen 중..")
server_socket.listen()

conn, addr = server_socket.accept()

print(f"연결 완료 !!!\nuser_info : {addr[0]} : {addr[1]}")
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
            print("\n[from client]")
            if not msg or msg == "quit": 
                print("socket is closed. please enter key <<< control + c or control + d >>>")        
                client_socket.close()
                break
            print(f">> {msg}\n(you) >> ", end="")
        except:
            pass
        
sending = threading.Thread(target=send, args=(conn,))
receiving = threading.Thread(target=receive, args=(conn,))
sending.daemon = True
receiving.daemon = True
sending.start()
receiving.start()

server_socket.close()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        conn.close()
        server_socket.close()
        break
print("\n프로그램 종료")