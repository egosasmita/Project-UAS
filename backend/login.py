import bcrypt
from backend.koneksi import get_connection
from mysql.connector import Error

def login_user(username_or_email, password):
    conn = get_connection()
    if conn is None:
        return None

    try:
        cursor = conn.cursor(dictionary=True) 
        
        query = """
        SELECT * FROM users 
        WHERE username = %s OR email = %s
        """
        
        cursor.execute(query, (username_or_email, username_or_email))
        user = cursor.fetchone()

        if user:
            stored_password_hash = user['PASSWORD'].encode('utf-8')
            input_password = password.encode('utf-8')

            if bcrypt.checkpw(input_password, stored_password_hash):
                print(f"Login berhasil untuk user: {user['username']}")
                
                user.pop('PASSWORD', None) 
                
                return user
            else:
                print("Login gagal: Password salah.")
                return None
        else:
            print("Login gagal: User tidak ditemukan.")
            return None

    except Error as e:
        print(f"Error saat proses login: {e}")
        return None
        
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()