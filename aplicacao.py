# Criado por:
# ----------------------------------
# Rafaela Amancio - RA 02211055
# ----------------------------------

import random
import decimal
from  time import sleep 
from conexaobd import *

pessoas = ['Rafaela', 'Lucas', 'Flávia', 'Ana', 'Gabriel', 'Isabela', 'Julia', 'Carlos', 'Vinicius', 'Paula', 'Vitor']

i = 0
idCaptura = 0

while i == 0 :
    nome = random.choice(pessoas)
    idade = random.randrange(15, 65)
    altura = decimal.Decimal(random.randrange(150, 195))/100

    if (nome == "Lucas" or nome == "Gabriel" or nome == "Carlos" or nome == "Vinicius" or nome == "Vitor") :
        sexo = "M"
    else:
        sexo = "F"

    idCaptura += 1

    insert_db(idCaptura, nome, idade, sexo, altura)
    
    print("\n" * 100)

    print("-"*45, "//", "-"*45)
    print(' '*30, "CAPTURA DE DADOS DE USUÁRIOS")
    print("-"*45, "//", "-"*45)

    print("ID\t\tNOME\t\tIDADE\t\tSEXO\t\tALTURA")
    print(
        f"{idCaptura}\t\t{nome}\t\t{idade}\t\t{sexo}\t\t{altura}\n")
    
    sleep(3)