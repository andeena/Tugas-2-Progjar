from socket import *
import time

def main():
    server_name = 'localhost'  # Ganti dengan alamat IP server jika tidak menjalankan di mesin yang sama
    server_port = 45000
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))

    try:
        while True:
            message = input("Enter command (TIME/QUIT): ").strip().upper()
            if message == "TIME":
                client_socket.sendall("TIME\r\n".encode('utf-8'))
                response = client_socket.recv(32).decode('utf-8')
                print("From Server:", response)
            elif message == "QUIT":
                client_socket.sendall("QUIT\r\n".encode('utf-8'))
                break
            else:
                print("Invalid command. Please enter TIME or QUIT.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()