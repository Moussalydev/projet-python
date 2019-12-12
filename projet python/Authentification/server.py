import socket                                         

import sys

def extraireinfo1(info):
    x  = info.split("'")
    return x[1]	
	
def identification(info):

    fichier = open("auth.txt", "r")
    identifiant = info.split(" ")

    r = "0", "", ""

    i = 1

    while 1:
            q = fichier.readline()

            if q == "":
                return r
                break
            else:

                q = q.split("_")
                

                if ((q[1] == identifiant[0]) and (q[2] == identifiant[1])):

                    r = "1", q[1], q[3]
                    return r
                    break
            i = i+1                
    
    fichier.close()

    
	
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = '127.0.0.1'                           
port = 2001                                          

try:
    server.bind((host, port))
except socket.error:
    sys.exit()
	
	
print("Serveur à l'écoute de requetes ...")


server.listen(1)

while 1:  

	client,adresse = server.accept()      
	print("Connexion avec  %s" % str(adresse))

	message = "Bienvenue!"
	client.send(message.encode())

	recu = client.recv(1024)
	recu = recu.decode('utf-8')





	user = identification(recu)


	if user[0] == "0":

		print("Authentification échouée.")
		message = "Authentification échouée."
		client.send(message.encode())

	else:

		print(str(user[2]) + " est connecté.")
		message = "Authentification réussie."
		client.send(message.encode())


	
server.close()
print("Connexion fermée")

