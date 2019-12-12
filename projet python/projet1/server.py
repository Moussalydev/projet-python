from socket import *
from _thread import *
import threading


import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='reseau',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
ListeUtilisteurs=list()
ListeSockets={}
def extraireinfo1(info):
    x  = info.split("'")
    return x[1]
 
host = '127.0.0.1'
port = 2001
 
server = socket()
server.bind((host, port))
print("Serveur à l'écoute de requetes ...")

server.listen(500)




def getuser(client):
    user = client.recv(1024)
    user = extraireinfo1(str(user))
    user = user.split(" ")
    return user

def inscrire(user,password):


    cursor=connection.cursor()
    sql = """INSERT INTO client (login,
             motpasse)
             VALUES (%s, %s)"""
    try:
        # Execute the SQL command
        cursor.execute(sql,(user,password))
        # Commit your changes in the database
        connection.commit()
    except:
        # Rollback in case there is any error
        connection.rollback()


    # disconnect from server
    #connection.close()

    return True



def authentifier(user,password):
    try:
        with connection.cursor() as cursor:

            sql = "SELECT * FROM  client WHERE  login =%s and motpasse=%s"
            cursor.execute(sql, (user,password))
            result = cursor.fetchone()

    except:
         connection.close()

    if result == None:
        return False
    return True

def gestionclient(client):
    user = getuser(client)
    if user[2]=='1':
      inscrire(user[0],user[1])
    else:
      connected = authentifier(user[0],user[1])

    if not connected:
        client.send(("Acces refuse: tu es inconnu!").encode())
        return 0

    ListeUtilisteurs.append(user[0])
    ListeSockets[user[0]] =client
    #la diffusion du message a tout le monde

    print("Liste des clients est:" )
    print(ListeUtilisteurs)
    i= 0
    utile =" "
    while(i < len(ListeUtilisteurs)):
     utile +=ListeUtilisteurs[i] + "  "
     i+=1
    client.send(("LES PERSONNES EN LIGNE").encode())

    client.send((utile).encode())


    #envoie de la liste des utilisateur aux clients
    while True:
        message = "Ecrivez le nom du estinataire et ton message separes par espace: "
        client.send(message.encode())
        data = client.recv(1024)
        destinataire = extraireinfo1(str(data)).split(" ")
        message = destinataire[1]
        destinataire = destinataire[0]
        print("from server: votre message sera envoyé a "+destinataire)
        print("from server: ce qui sera envoye::: "+message)

        clientDestinataire = ListeSockets[destinataire]

        clientDestinataire.send(("message de "+user[0]+": "+ message).encode())
        #clientDestinataire.send(message.encode())


        #print(user[0] + "> " +extraireinfo1(str(data)))


 
while True:
    client, adresse = server.accept()
    print("Connexion avec  %s" % str(adresse))

    start_new_thread(gestionclient,(client,))


client.close()
server.close()
