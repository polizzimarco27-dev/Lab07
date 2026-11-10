from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")

            query = "SELECT DISTINCT genere FROM libro ORDER BY genere"
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []

            for row in cursor:  # ogni riga ha una sola colonna, quindi prendo row[0]
                result.append(row[0])

            cursor.close()
            cnx.close()
            print("Generi read from database")
            return result

    # leggo i libri filtrati
    def get_libri_filtrati(self, biblioteca, genere):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")

            # JOIN con biblioteca per poter filtrare sul nome
            # COALESCE: se il parametro è None confronta la colonna con se stessa (sempre vero)
            query = """SELECT l.id, l.titolo, l.autore, l.genere, l.anno_pubblicazione, l.id_biblioteca
                       FROM libro l, biblioteca b
                       WHERE l.id_biblioteca = b.id
                       AND b.nome = COALESCE(%s, b.nome)
                       AND l.genere = COALESCE(%s, l.genere)
                       ORDER BY l.titolo"""
            cursor = cnx.cursor()
            cursor.execute(query, (biblioteca, genere))
            result = []

            for row in cursor:  # creo un oggetto Libro per ogni riga
                libro = Libro(*row)
                result.append(libro)

            cursor.close()
            cnx.close()
            print("Libri (filtrati) read from database")
            return result
