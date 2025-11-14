import tkinter as tk

# Membuat window utama
root = tk.Tk()
root.title("Selamat Datang")
root.geometry("400x200")  # ukuran window: lebar x tinggi

# Membuat label teks
label = tk.Label(root, text="Selamat Datang di Aplikasi!", 
                 font=("Arial", 16, "bold"), 
                 fg="white", 
                 bg="#23589C", 
                 padx=20, pady=20)
label.pack(expand=True)

# Tombol keluar
button = tk.Button(root, text="Keluar", 
                   font=("Arial", 12), 
                   bg="#3498db", fg="white", 
                   command=root.destroy)
button.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
