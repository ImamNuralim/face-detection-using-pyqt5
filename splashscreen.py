from PyQt5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__(QPixmap("resources/splash.png"))
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setEnabled(False)

        self.setGeometry(0, 0, 1151, 687)  # Mengatur ukuran splash screen

         # Mengatur posisi splash screen ke tengah layar
        screen_geometry = QApplication.desktop().screenGeometry()
        splash_geometry = self.geometry()
        x = (screen_geometry.width() - splash_geometry.width()) // 2
        y = (screen_geometry.height() - splash_geometry.height()) // 2
        self.move(x, y)

def main():
    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()

    app.processEvents()

    # Kode lainnya untuk halaman utama

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()