import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345


def recv_messages(sock):
    buffer = ""
    while True:
        data = sock.recv(1024)
        if not data:
            break
        buffer += data.decode()
        while '\n' in buffer:
            msg, buffer = buffer.split('\n', 1)
            yield msg


def send_messages(client):
    while True:
        msg = input("Server: ")
        client.sendall((msg + "\n").encode())
        if msg.lower() == "exit":
            break


def handle_client(client, addr):
    print("Connected:", addr)

    threading.Thread(target=send_messages, args=(client,), daemon=True).start()

    for msg in recv_messages(client):
        print("Client:", msg)
        if msg.lower() == "exit":
            break

    client.close()
    print("Disconnected:", addr)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server running on {HOST}:{PORT}")

client, addr = server.accept()
handle_client(client, addr)
