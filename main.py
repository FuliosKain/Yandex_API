import sys
import find
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPixmap


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        # Загружаем интерфейс из design.ui
        uic.loadUi('maps.ui', self)

        # Получаем доступ к элементам интерфейса
        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'coord')  # Имя вашего QLineEdit
        self.button = self.findChild(QtWidgets.QPushButton, 'search')  # Имя вашего QPushButton
        self.label = self.findChild(QtWidgets.QLabel, 'map')  # Имя вашего QLabel

        # Подключаем кнопку к методу
        self.button.clicked.connect(self.load_image)

    def load_image(self):
        #coords = self.lineEdit.text()
        coords = 0

        # Загружаем изображение в QLabel
        pixmap = QPixmap(find.find_the_place(coords))
        if not pixmap.isNull():
            self.label.setPixmap(pixmap.scaled(self.label.size()))
        else:
            self.label.setText("Image not found!")  # Сообщение об ошибке, если изображение не найдено


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
