# Criado por:
# ----------------------------------
# Rafaela Amancio - RA 02211055
# ----------------------------------

import random
import decimal
from  time import sleep 
from conexaobd import *

listaNomeFem = ['Rafaela', 'Flavia', 'Ana', 'Isabella',  'Julia', 'Paula']
listaNomeMasc = ['Lucas', 'Gabriel', 'Carlos', 'Vinicius', 'Vitor', 'João']
listaSexo = ['F', 'M']

i = 0
idCaptura = 0

while i == 0 :
    sexo = random.choice(listaSexo)
    
    if (sexo == 'F'):
        nome = random.choice(listaNomeFem)
    else:
        nome = random.choice(listaNomeMasc)

    idade = random.randrange(15, 65)

    altura = decimal.Decimal(random.randrange(150, 195))/100

    idCaptura += 1

    insert_db(idCaptura, nome, idade, sexo, altura)
    
    print("\n" * 2)

    print("-"*45, "//", "-"*45)
    print(' '*30, "CAPTURA DE DADOS DE USUÁRIOS")
    print("-"*45, "//", "-"*45)

    print("ID\t\tNOME\t\tIDADE\t\tSEXO\t\tALTURA")
    print(
        f"{idCaptura}\t\t{nome}\t\t{idade}\t\t{sexo}\t\t{altura}\n")
    
    sleep(3)