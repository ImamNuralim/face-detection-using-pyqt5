import os

def is_first_time_user():
    # Lakukan logika untuk memeriksa apakah pengguna baru atau bukan
    settings_file = "settings.txt"
    return not os.path.isfile(settings_file)

def save_user_settings(username, password):
    # Simpan pengaturan pengguna ke dalam file
    settings_file = "settings.txt"
    with open(settings_file, "w") as file:
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
