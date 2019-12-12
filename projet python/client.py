import socket                                         

def extraireinfo1(info):

    x  = info.split("'")

    return x[1]	
	
	
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = '127.0.0.1'#'10.1.0.104'                           
port = 2001                                          

client.connect((host, port))






while 1:

    print("Client démarré.")

    recu = client.recv(1024)

    print("Serveur a dit :  %s" % extraireinfo1(str(recu)))

    n = input("Veuillez entrer un nombre (FIN  pour quitter):")

    if n == "FIN":

        break

    client.send(n.encode())


    recu = client.recv(1024)

    print("Résultat :  %s" % extraireinfo1(str(recu)))




client.close()
print("Connexion fermée")

