from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QTimer


class SlideShowPage(QWidget):
    def __init__(self):
        super().__init__()

        self.current_slide = 0
        self.slides = [
            "resources/slideshow.png",
            "resources/slideshow2.png",
            "resources/slideshow3.png"
        ]

        self.layout = QVBoxLayout(self)

        self.carousel_widget = QWidget(self)  # Widget untuk menampung carousel
        self.carousel_layout = QHBoxLayout(self.carousel_widget)  # Layout untuk carousel

        self.carousel_items = []  # Daftar widget untuk setiap slide

        # Membuat widget untuk setiap slide dan menambahkannya ke carousel
        for slide_path in self.slides:
            slide_widget = QLabel(self)
            slide_widget.setPixmap(QPixmap(slide_path).scaledToWidth(300))  # Menyesuaikan lebar gambar dengan lebar carousel
            self.carousel_layout.addWidget(slide_widget)
            self.carousel_items.append(slide_widget)

        self.layout.addWidget(self.carousel_widget, alignment=Qt.AlignCenter)  # Menampilkan carousel di tengah

        # Mengatur interval perpindahan slide secara otomatis
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_slide)
        self.timer.start(2000)  # Interval 2 detik

    def paintEvent(self, event):
        # Mengatur background color pada carousel
        painter = QPainter(self)
        painter.setBrush(Qt.white)
        painter.drawRect(self.rect())

    def next_slide(self):
        self.current_slide += 1
        if self.current_slide >= len(self.slides):
            self.current_slide = 0
        self.update_slide()

    def update_slide(self):
        for i, slide_widget in enumerate(self.carousel_items):
            if i == self.current_slide:
                slide_widget.show()
            else:
                slide_widget.hide()


def main():
    app = QApplication([])

    main_window = QMainWindow()
    main_window.setWindowTitle("Main Window")
    main_window.setGeometry(0, 0, 1151, 687)  # Mengatur ukuran jendela

    slideshow_page = SlideShowPage()
    main_window.setCentralWidget(slideshow_page)

    main_window.show()
    app.exec_()


if __name__ == "__main__":
    main()
