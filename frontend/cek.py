import sys, os
from PyQt5 import QtWidgets, QtGui

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.resize(800, 600)

label = QtWidgets.QLabel(window)
label.setGeometry(0, 0, 800, 600)

print("Current path:", os.getcwd())
print("File exists:", os.path.exists("Background2.png"))

pixmap = QtGui.QPixmap("Background2.png")
print("Gambar valid:", not pixmap.isNull())

label.setPixmap(pixmap)
label.setScaledContents(True)

window.show()
sys.exit(app.exec_())
