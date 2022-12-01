import sys
import socket
import psutil
import os
import platform

host = ""
port = 7777

def Serveur():
    while True:
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(1)
        msg = ""
        reply = ""
        while msg != "kill" and msg != "reset":
            print("En attente du client")
            conn, address = server_socket.accept()
            print(f"Client connecté {address}")

            msg = ""
            while msg != "kill" and msg != "disconect" and msg != "reset":
                msg = conn.recv(1024).decode()
                print(msg)
                if msg == "ram":
                    reply = str(psutil.virtual_memory().percent)
                    conn.send(reply.encode())

                elif msg == "cpu":
                    reply = str(psutil.cpu_percent())
                    conn.send(reply.encode())

                if msg == "os":
                    reply = str(platform.system())
                    conn.send(reply.encode())


                else:
                    reply = msg
                    conn.send(reply.encode())






            conn.close()
            print("fermeture de la connexion")

        server_socket.close()
        print("fermeture du serveur")
        if msg == "kill":
            exit()

if __name__ == '__main__':
    sys.exit(Serveur())