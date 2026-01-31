import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345


class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Client")
        self.root.geometry("500x450")

        self.chat = ScrolledText(root, state="disabled", font=("Segoe UI", 10))
        self.chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        bottom = tk.Frame(root)
        bottom.pack(fill=tk.X, padx=10, pady=5)

        self.entry = tk.Entry(bottom, font=("Segoe UI", 10))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry.bind("<Return>", self.send_message)

        self.send_btn = tk.Button(bottom, text="Send", command=self.send_message)
        self.send_btn.pack(side=tk.RIGHT)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))

        self.add("System", "Connected to server")

        threading.Thread(target=self.receive_messages, daemon=True).start()

    def add(self, sender, msg):
        self.chat.config(state="normal")
        self.chat.insert(tk.END, f"{sender}: {msg}\n")
        self.chat.config(state="disabled")
        self.chat.yview(tk.END)

    def send_message(self, event=None):
        msg = self.entry.get().strip()
        if not msg:
            return

        self.sock.sendall((msg + "\n").encode())
        self.add("You", msg)
        self.entry.delete(0, tk.END)

        if msg.lower() == "exit":
            self.sock.close()
            self.root.quit()

    def receive_messages(self):
        buffer = ""
        while True:
            try:
                data = self.sock.recv(1024)
                if not data:
                    break
                buffer += data.decode()
                while '\n' in buffer:
                    msg, buffer = buffer.split('\n', 1)
                    self.add("Server", msg)
            except:
                break


if __name__ == "__main__":
    root = tk.Tk()
    ChatClient(root)
    root.mainloop()
