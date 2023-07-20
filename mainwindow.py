from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(0, 0, 800, 600)  # Mengatur ukuran jendela

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Halaman Utama", self)
        self.layout.addWidget(self.label)

        self.button = QPushButton("Tombol", self)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.button_clicked)  # Menghubungkan klik tombol dengan fungsi button_clicked

    def button_clicked(self):
        # Lakukan tindakan yang diinginkan saat tombol diklik
        print("Tombol diklik")
