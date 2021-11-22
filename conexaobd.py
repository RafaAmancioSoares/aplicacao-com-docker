import mysql.connector
from credencial import usr, pswd

def insert_db(idCaptura, nome, idade, sexo, altura):
    try:  
        mydb = mysql.connector.connect(
            host = "18.212.61.221",
            user = usr,
            password = pswd,
            database = "ac3_rafaela"
        )

        if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Conectado ao MySQL Server versão ", db_Info)

            mycursor = mydb.cursor() # mandar query para o MySQL

            sql_query = "INSERT INTO dadosColetados() VALUES (%s, %s, %s, %s, %s)"
            val = [idCaptura, nome, idade, sexo, altura]
            mycursor.execute(sql_query, val)
            
            mydb.commit()

            print(mycursor.rowcount, "registro inserido")
    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL", e)
    finally:
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("Conexão com MySQL está fechada\n")

def selectbanco():
    cnx = mysql.connector.connect(user=usr, password=pswd, database='ac3_rafaela')
    cursor = cnx.cursor()

    query = ("SELECT * FROM dadosColetados")


    cursor.execute(query)
    records = cursor.fetchall()
    print(records)
    
    
    # for row in records:
    #     print("Id = ", row[0])

    cursor.close()
    cnx.close()
