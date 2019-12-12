import socket 

def binaire1(n):
    r = ""

    for i in range(8):
        r = str(n % 2) + r
        n = n // 2
		
    return r

def extraireinfo1(info):
    x  = info.split("'")

    return x[1]	
	
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = '127.0.0.1'#'10.1.0.104'                           
port = 2001                                          

server.bind((host, port))
print("Serveur à l'écoute de requetes ...")
server.listen(1)  

while 1:
    client,adresse = server.accept()      

    print("Connexion avec  %s" % str(adresse))

    message = "Liaison etablie avec succès."
    client.send(message.encode())

    recu = client.recv(1024)

    

    n = extraireinfo1(str(recu))

    if n =="":
        n=0

    resultat = binaire1(int(n))

    client.send(str(resultat).encode())

server.close()
print("Connexion fermée")

