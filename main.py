from PyQt6.QtWidgets import QApplication
from qfluentwidgets import FluentWindow


class Window(FluentWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.setObjectName("Window")
        self.resize(800, 600)
        self.setWindowTitle("Winsio")

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()