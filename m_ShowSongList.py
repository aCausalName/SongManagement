from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        QWidget.__init__(self, None )

    # 创建窗口
    def setupUI(self):

        self.setFixedSize(650, 350)
        self.move(300, 310)
        self.setWindowTitle("查看歌单")
        self.setFixedSize(650, 350)

    def ShowSong(self):
        self.table = QTableWidget(5, 5)
        self.table.setHorizontalHeaderLabels(['1', '2', '3', '4', '5'])
        self.table.setVerticalHeaderLabels(['1', '2', '3', '4', '5'])
        self.table.horizontalHeader().setDisabled(True)
        self.table.verticalHeader().setDisabled(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectItems)



def main():
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.setupUI()
    mainWindow.ShowSong()
    mainWindow.show()

    app.exec_()
    app.closingDown()


if __name__ == '__main__':
    main()
