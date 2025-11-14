import bcrypt
import mysql.connector

from . import koneksi

def check_password(stored_hashed_password, provided_password):
    if isinstance(stored_hashed_password, str):
        stored_hashed_password = stored_hashed_password.encode('utf-8')
        
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_hashed_password)

def login_user(email, password):

    if not (email and password):
        return "Email dan Password wajib diisi!"
        
    conn = None
    cursor = None
    try:
        conn = koneksi.get_db_connection()
        if conn is None:
            return "Gagal terhubung ke database."

        cursor = conn.cursor()
        query = "SELECT password FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        
        user_row = cursor.fetchone() 
        
        if user_row:
            stored_hashed_password = user_row[0] 
            
            # 2. Periksa password
            if check_password(stored_hashed_password, password):
                return "Login berhasil!"
            else:
                return "Email atau Password salah."
        else:
            return "Email atau Password salah."
            
    except mysql.connector.Error as err:
        return f"Terjadi error saat login: {err}"
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()