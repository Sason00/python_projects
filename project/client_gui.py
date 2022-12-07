import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QLineEdit

# C:\Python310\Lib\site-packages\PySide6\uic.exe

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
dialog = loader.load("untitled.ui", None)

btn = dialog.create_new_room_button
print(f"{btn=}")

btn.clicked.connect(lambda: print())

dialog.show()
app.exec()
