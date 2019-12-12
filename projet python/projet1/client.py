
from socket import *
from _thread import *


def extraireinfo1(info):
    x  = info.split("'")
    return x[1]

def envoie(client):
    while True:
     message = input(":")
     client.send(message.encode())
    return 0

def inscrire(choix):
    longueur = 0
    indice = 0
    while indice == 0:
        log = input("INSCRIVEZ VOUS AVEC VOTRE PSEUDO \n".center(130))
        try:
            intlog = int(log)
            print("Le login ne doit pas etre que des chiffres\n")
        except ValueError:
            if (len(str(log)) > 2):
                indice += 1
            else:
                print("Le pseudo doit faire au moins 3 caracteres\n")

    while longueur < 7:
        mp = input("MOT DE PASSE SVP\n".center(130))
        chmp = str(mp)
        longueur = len(chmp)
        if longueur < 7:
            print("Attention: le mot de passe doit comporter 7 caracteres au moins")
            message =log + " " + mp



    return log + " " + mp + " " + choix


print("****************************************************  DIALOGUER DEVIENT FACIL****************************************************************\n")
def authent(choix):
 print("*****************************************************CONNECTION DANS L'APPLICATION************************************************************\n")
 i = 0
 longueur = 0
 indice = 0
 while indice==0:
  log =input("ENTREZ VOTRE PSEUDO \n".center(130))
  try:
   intlog = int(log)
   print("Le login ne doit pas etre que des chiffres\n")
  except ValueError:
   if(len(str(log))>2):
    indice+=1
   else:
    print("Le pseudo doit faire au moins 3 caracteres\n")

 while longueur < 7:
  mp = input("ENTREZ VOTRE MOT DE PASSE\n".center(130))
  chmp = str(mp)
  longueur = len(chmp)
  if longueur < 7:
   print("Attention: le mot de passe doit comporter 7 caracteres au moins")

 return log +" "+ mp + " " + choix



host = '127.0.0.1'
port = 2001
 
client = socket()

client.connect((host, port))

choix=input("Tapez 1 si tu veux tinscrire ou 0 te connecter\n")
if choix=='1':
   mes_inscr=inscrire(choix)
   print("Inscrit avec succes")
   client.send(mes_inscr.encode())
elif choix=='0':
   message = authent(choix)
   client.send(message.encode())





start_new_thread(envoie,(client,))

while True:

    data = client.recv(1024)
    print(extraireinfo1(str(data)))


client.close()
