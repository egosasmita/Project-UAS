import bcrypt
import mysql.connector
from mysql.connector import errorcode

from . import koneksi

def hash_password(password):
    """Meng-hash password mentah menggunakan bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def register_user(username, email, password, alamat, tipe_user):
    """Logika untuk mendaftarkan pengguna baru ke MySQL."""
    
    if not (username and email and password and alamat and tipe_user):
        return "Semua field wajib diisi!"

    hashed_pw = hash_password(password)
    
    conn = None
    cursor = None
    try:
        conn = koneksi.get_db_connection()
        if conn is None:
            return "Gagal terhubung ke database."
            
        cursor = conn.cursor()
        
        query = (
            "INSERT INTO users (username, email, password, alamat, tipe_user) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        data = (username, email, hashed_pw, alamat, tipe_user)
        
        cursor.execute(query, data)
        conn.commit() 
        
        return "Registrasi berhasil!"
        
    except mysql.connector.IntegrityError:
        return "Username atau Email sudah terdaftar."
    except mysql.connector.Error as err:
        return f"Terjadi error saat registrasi: {err}"
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()