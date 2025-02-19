import sys
import requests
from PyQt6.QtWidgets import QLabel

from scale import scale
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

    def find_the_place(self, coords):
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {"apikey": "8013b162-6b42-4997-9691-77b7074026e0",
                           "geocode": coords,
                           "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        param = scale(toponym)
        toponym_longitude, toponym_lattitude = param[0].split()

        apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "spn": ",".join([str(param[1]), str(param[2])]),
            "apikey": apikey
        }

        map_api_server = "https://static-maps.yandex.ru/v1"
        response = requests.get(map_api_server, params=map_params)
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        return file

    def load_image(self):
        #coords = self.lineEdit.text()
        coords = '39.605562 52.565400'

        # Загружаем изображение в QLabel
        print('Проверка Finde the place')
        image = (self.find_the_place(coords))
        print(image)
        self.pixmap = QPixmap(self.map_file)
        print('Проверка1')
        if not self.pixmap.isNull():
            self.image = QLabel(self)
            self.image.move(0, 0)
            self.image.resize(600, 450)
            self.image.setPixmap(self.pixmap)
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
