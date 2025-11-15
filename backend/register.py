import bcrypt
from backend.koneksi import get_connection
from mysql.connector import Error

def register_user(username, email, password, alamat, tipe_user):
    if tipe_user not in ['Pembeli', 'Penjual']:
        print("Error: Tipe user tidak valid.")
        return False

    conn = get_connection()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)

        query = """
        INSERT INTO users (username, email, PASSWORD, alamat, tipe_user)
        VALUES (%s, %s, %s, %s, %s)
        """
        
        data = (username, email, hashed_password.decode('utf-8'), alamat, tipe_user)

        cursor.execute(query, data)
        conn.commit()

        print(f"User '{username}' berhasil terdaftar.")
        return True

    except Error as e:
        if e.errno == 1062:
            print(f"Error: Username '{username}' atau Email '{email}' sudah digunakan.")
        else:
            print(f"Error saat registrasi: {e}")
        
        conn.rollback()
        return False
        
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()