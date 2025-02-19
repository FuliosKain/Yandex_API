import sys
from PIL import Image
import find
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPixmap


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('maps.ui', self)

        # Получаем доступ к элементам интерфейса
        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'coord')
        self.button = self.findChild(QtWidgets.QPushButton, 'search')
        self.label = self.findChild(QtWidgets.QLabel, 'map')

        # Подключаем кнопку к методу
        print('АБА')
        self.button.clicked.connect(self.load_image)
        print('БАБ')

    def load_image(self):
        #coords = self.lineEdit.text()
        coords = '39.605562 52.565400'

        # Загружаем изображение в QLabel
        print('Проверка Finde the place')
        image_bytes = (find.find_the_place(coords))
        image = Image.open(image_bytes)
        pixmap = QPixmap(image)
        print('Проверка1')
        if not pixmap.isNull():
            self.label.setPixmap(pixmap.scaled(self.label.size()))
        else:
            self.label.setText("Image not found!")
        print('Проверка 2')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
