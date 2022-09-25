import PyQt5.QtWidgets as PyQt
global res, nameEdit, singerEdit, ordererEdit, attachedCombo, sourceCombo


class MainWindow(PyQt.QWidget):

    def __init__(self):
        PyQt.QWidget.__init__(self, None)

    # 创建窗口
    def setupUI(self):
        global nameEdit, singerEdit, ordererEdit, attachedCombo, sourceCombo

        # 窗口初始化
        self.setFixedSize(650, 350)
        self.move(300, 310)
        self.setWindowTitle("添加歌曲")
        self.setFixedSize(650, 350)

        # 3个文本框（name, singer, orderer)
        nameEdit = PyQt.QTextEdit(self)
        nameEdit.resize(250, 50)
        nameEdit.move(30, 50)
        nameEdit.setPlaceholderText("请输入歌名(必填）")

        singerEdit = PyQt.QTextEdit(self)
        singerEdit.resize(250, 50)
        singerEdit.move(30, 150)
        singerEdit.setPlaceholderText("请输入歌手名（选填）")

        ordererEdit = PyQt.QTextEdit(self)
        ordererEdit.resize(250, 50)
        ordererEdit.move(30, 250)
        ordererEdit.setPlaceholderText("请输入你的名字（选填）")

        # 2个复选框（attached, source)
        attachedCombo = PyQt.QComboBox(self)
        attachedCombo.resize(150, 30)
        attachedCombo.move(400, 50)
        attachedCombo.addItems(['日常放歌', '社团活动', '自由活动'])

        sourceCombo = PyQt.QComboBox(self)
        sourceCombo.resize(150, 30)
        sourceCombo.move(400, 150)
        sourceCombo.addItems(['网易云音乐', 'QQ音乐', '酷狗音乐', 'Bilibili'])

        # 5个标签（name, singer, orderer, attached, source)
        self.nameText = PyQt.QLabel(self)
        self.nameText.move(30, 20)
        self.nameText.setText("歌名")

        self.singerText = PyQt.QLabel(self)
        self.singerText.move(30, 120)
        self.singerText.setText("歌手")

        self.ordererText = PyQt.QLabel(self)
        self.ordererText.resize(300, 30)
        self.ordererText.move(30, 220)
        self.ordererText.setText("点歌人（以保证你的歌曲出现问题时能及时与你联系）")

        self.attachedText = PyQt.QLabel(self)
        self.attachedText.move(400, 20)
        self.attachedText.setText("将歌曲保存在")

        self.sourceText = PyQt.QLabel(self)
        self.sourceText.move(400, 120)
        self.sourceText.setText("歌源")

        # 2个按钮
        self.okButton = PyQt.QPushButton(self)
        self.okButton.move(520, 300)
        self.okButton.setText("确定")
        self.okButton.clicked.connect(self.okPressed)

        self.cancelButton = PyQt.QPushButton(self)
        self.cancelButton.move(400, 300)
        self.cancelButton.setText("取消")
        self.cancelButton.clicked.connect(self.close)


    def okPressed(self):
        res.append(nameEdit.toPlainText())
        res.append(singerEdit.toPlainText())
        res.append(ordererEdit.toPlainText())
        res.append(attachedCombo.currentText())
        res.append(sourceCombo.currentText())
        self.close()


def main():
    global res
    res = []

    app = PyQt.QApplication([])
    mainWindow = MainWindow()
    mainWindow.setupUI()
    mainWindow.show()

    app.exec_()
    app.closingDown()

    return res

