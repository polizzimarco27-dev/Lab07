from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_all(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")

            query = "SELECT id, nome, indirizzo FROM biblioteca ORDER BY nome"
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                biblioteca = Biblioteca(*row)
                result.append(biblioteca)

            cursor.close()
            cnx.close()
            print("Biblioteche read from database")
            return result
