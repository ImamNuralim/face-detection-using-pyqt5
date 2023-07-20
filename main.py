from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from splashscreen import SplashScreen
from slideshow import SlideShowPage
from mainwindow import MainWindow

def main():
    app = QApplication([])

    splash = SplashScreen()
    splash.show()

    # Menjalankan tugas yang membutuhkan waktu

    main_window = QMainWindow()
    main_window.setWindowTitle("Main Window")
    main_window.setGeometry(0, 0, 1151, 687)  # Mengatur ukuran main window

    # Mengatur posisi jendela utama ke tengah layar
    screen_geometry = app.desktop().availableGeometry()
    main_window.move((screen_geometry.width() - main_window.width()) // 2, (screen_geometry.height() - main_window.height()) // 2)

    splash.finish(main_window)  # Menutup splash screen

    stacked_widget = QStackedWidget(main_window)
    main_window.setCentralWidget(stacked_widget)

    slideshow_page = SlideShowPage()
    stacked_widget.addWidget(slideshow_page)

    main_page = MainWindow()
    stacked_widget.addWidget(main_page)

    stacked_widget.setCurrentWidget(slideshow_page)  # Menampilkan halaman slide show pertama

    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()
