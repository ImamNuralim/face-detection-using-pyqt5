# from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit

# class RegisterWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Register")
#         self.setGeometry(0, 0, 800, 600)  # Mengatur ukuran jendela

#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)

#         self.layout = QVBoxLayout(self.central_widget)

#         self.label = QLabel("Halaman Register", self)
#         self.layout.addWidget(self.label)

#         self.email_label = QLabel("Email:", self)
#         self.layout.addWidget(self.email_label)

#         self.email_input = QLineEdit(self)
#         self.layout.addWidget(self.email_input)

#         self.password_label = QLabel("Password:", self)
#         self.layout.addWidget(self.password_label)

#         self.password_input = QLineEdit(self)
#         self.layout.addWidget(self.password_input)
#         self.password_input.setEchoMode(QLineEdit.Password)  # Mengatur mode input menjadi password

#         self.button = QPushButton("Register", self)
#         self.layout.addWidget(self.button)

#         self.button.clicked.connect(self.register_button_clicked)  # Menghubungkan klik tombol dengan fungsi register_button_clicked

#     def register_button_clicked(self):
#         email = self.email_input.text()
#         password = self.password_input.text()

#         # Lakukan proses pendaftaran pengguna baru
#         # Contoh: Menyimpan data pendaftaran ke database atau file
#         # ...

#         print("Pendaftaran pengguna baru:")
#         print("Email:", email)
#         print("Password:", password)
