import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='lensart_shop',
            user='root',
            password=''
        )
        
        if connection.is_connected():
            return connection
            
    except Error as e:
        print(f"Error saat menghubungkan ke MySQL: {e}")
        return None

if __name__ == '__main__':
    conn = get_connection()
    if conn:
        print("Koneksi berhasil!")
        conn.close()