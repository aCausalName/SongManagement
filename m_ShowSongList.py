from PyQt5.QtWidgets import *
global daily, AA, FA


class MainWindow(QTabWidget):

    def __init__(self):
        QWidget.__init__(self, None)
        super(MainWindow, self).__init__()

        # 窗口
        self.setFixedSize(650, 350)
        self.move(300, 310)
        self.setWindowTitle("查看歌单")
        self.setFixedSize(650, 350)
        # tab控件
        self.tab_daily = QWidget()
        self.tab_AA = QWidget()
        self.tab_FA = QWidget()
        self.addTab(self.tab_daily, "日常歌曲")
        self.addTab(self.tab_AA, "社团歌曲")
        self.addTab(self.tab_FA, "自由活动歌曲")
        self.tab_dailySetUp()
        self.tab_AASetUp()
        self.tab_FASetUp()
        # 布局
        self.MyLayout1 = QHBoxLayout()
        self.MyLayout2 = QHBoxLayout()
        self.MyLayout3 = QHBoxLayout()
        self.MyLayout1.addWidget(self.tabledaily)
        self.MyLayout2.addWidget(self.tableAA)
        self.MyLayout3.addWidget(self.tableFA)
        self.tab_daily.setLayout(self.MyLayout1)
        self.tab_AA.setLayout(self.MyLayout2)
        self.tab_FA.setLayout(self.MyLayout3)
    def TableInit(self, table):
        # 表格初始化（公共部分）
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(['歌名', '歌手', '点歌人', '播放源', '状态'])
        table.horizontalHeader().setDisabled(True)
        table.verticalHeader().setDisabled(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectItems)

    def tab_dailySetUp(self):
        self.tabledaily = QTableWidget()
        self.TableInit(self.tabledaily)
        self.tabledaily.setRowCount(len(daily))
        self.ShowSong(self.tabledaily, daily)
    def tab_AASetUp(self):
        self.tableAA = QTableWidget()
        self.TableInit(self.tableAA)
        self.tableAA.setRowCount(len(AA))
        self.ShowSong(self.tableAA, AA)
    def tab_FASetUp(self):
        self.tableFA = QTableWidget()
        self.TableInit(self.tableFA)
        self.tableFA.setRowCount(len(FA))
        self.ShowSong(self.tableFA, FA)

    def ShowSong(self, table, songList):
        for i in range(len(songList)):
            table.setItem(i, 0, QTableWidgetItem(songList[i]['name']))
            table.setItem(i, 1, QTableWidgetItem(songList[i]['singer']))
            table.setItem(i, 2, QTableWidgetItem(songList[i]['orderer']))
            table.setItem(i, 3, QTableWidgetItem(songList[i]['source']))
            if songList[i]['status'] == 0:
                table.setItem(i, 4, QTableWidgetItem('未播放'))
            else:
                table.setItem(i, 4, QTableWidgetItem('已播放'))

def main(dailySongList, AASongList, FASongList):
    global daily, AA, FA
    daily, AA, FA = dailySongList, AASongList, FASongList

    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()
    app.closingDown()
