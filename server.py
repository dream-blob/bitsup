import socket
from tkinter import *
host , port = ("", 2007)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))

print("le serveur est démarré...")

while True:
    socket.listen()
    conn, address = socket.accept()
    print("en écoute...")

    data = conn.recv(2048)
    data = data.decode("utf8")
    # tkinter init
    window = Tk()

    window.title("Server msg")
    window.geometry("400x220")
    window.config(background="#4AAF7F")
    text = Label(window, text=data,font=("Courrier", 10), bg="#4AAF7F", fg="white")
    text.pack(expand=YES)
    window.mainloop()

conn.close()