import mysql.connector
from mysql.connector import errorcode

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'lensart_shop'
}

def get_db_connection():
    """Membuka koneksi baru ke database MySQL."""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Username atau password database salah")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"Database '{db_config['database']}' tidak ditemukan")
        else:
            print(f"Error koneksi DB: {err}")
        return None