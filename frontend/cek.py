import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from backend.login import login_user
from backend.register import register_user


# -----------------------
#  WINDOW LOGIN
# -----------------------
def open_login_window():
    login_win = tk.Toplevel()
    login_win.title("Login User")
    login_win.geometry("300x250")

    tk.Label(login_win, text="Login", font=("Arial", 14)).pack(pady=10)

    tk.Label(login_win, text="Username / Email").pack()
    entry_user = tk.Entry(login_win, width=30)
    entry_user.pack()

    tk.Label(login_win, text="Password").pack()
    entry_pass = tk.Entry(login_win, width=30, show="*")
    entry_pass.pack()

    def handle_login():
        user_input = entry_user.get()
        pass_input = entry_pass.get()

        result = login_user(user_input, pass_input)

        if result:
            messagebox.showinfo("Sukses", f"Login berhasil!\nSelamat datang {result['username']}")
        else:
            messagebox.showerror("Gagal", "Username/Email atau Password salah.")

    tk.Button(login_win, text="Login", width=20, command=handle_login).pack(pady=10)


# -----------------------
#  WINDOW REGISTER
# -----------------------
def open_register_window():
    reg_win = tk.Toplevel()
    reg_win.title("Register User")
    reg_win.geometry("350x400")

    tk.Label(reg_win, text="Register", font=("Arial", 14)).pack(pady=10)

    tk.Label(reg_win, text="Username").pack()
    entry_username = tk.Entry(reg_win, width=30)
    entry_username.pack()

    tk.Label(reg_win, text="Email").pack()
    entry_email = tk.Entry(reg_win, width=30)
    entry_email.pack()

    tk.Label(reg_win, text="Password").pack()
    entry_password = tk.Entry(reg_win, width=30, show="*")
    entry_password.pack()

    tk.Label(reg_win, text="Alamat").pack()
    entry_alamat = tk.Entry(reg_win, width=30)
    entry_alamat.pack()

    tk.Label(reg_win, text="Tipe User (pembeli/penjual)").pack()
    entry_tipe = tk.Entry(reg_win, width=30)
    entry_tipe.pack()

    def handle_register():
        username = entry_username.get()
        email = entry_email.get()
        password = entry_password.get()
        alamat = entry_alamat.get()
        tipe_user = entry_tipe.get()

        result = register_user(username, email, password, alamat, tipe_user)

        if result:
            messagebox.showinfo("Sukses", "Pendaftaran berhasil.")
        else:
            messagebox.showerror("Gagal", "Pendaftaran gagal. Cek terminal untuk info detail.")

    tk.Button(reg_win, text="Register", width=20, command=handle_register).pack(pady=15)


# -----------------------
#  MAIN WINDOW
# -----------------------
root = tk.Tk()
root.title("LensArt Shop - Test Backend")
root.geometry("300x200")

tk.Label(root, text="Test Login & Register", font=("Arial", 14)).pack(pady=20)

tk.Button(root, text="Login", width=20, command=open_login_window).pack(pady=5)
tk.Button(root, text="Register", width=20, command=open_register_window).pack(pady=5)

root.mainloop()
