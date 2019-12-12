import socket                                         

import sys
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = '127.0.0.1'                           
port = 2001                                      


def sortir(info):
        x = info.split(" ")

        if x[0] == "Total":
                client.close()
                print("Connexion fermée")
                
                
try:
        client.connect((host, port))
except socket.error:
        sys.exit()
        


print("Client démarré.")



recu = client.recv(1021)
recu = recu.decode('utf-8')

print(str(recu))


message = input("Entrer Login et mot de passe :")
client.send(message.encode())

recu = client.recv(1021)
recu = recu.decode('utf-8')

print(str(recu))

client.close()
print("Connexion fermée")

