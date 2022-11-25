from PyQt5 import QtCore, QtGui, QtWidgets
from random import choice
from time import sleep

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 950)
        MainWindow.setMaximumSize(QtCore.QSize(1150, 950))
        MainWindow.setStyleSheet("#centralwidget{\n"
                                "background-color:rgb(177, 177, 177);\n"
                                "}\n"
                                "QPushButton\n"
                                "{\n"
                                "    color: silver;\n"
                                "    background-color: #302F2F;\n"
                                "    border-width: 2px;\n"
                                "    border-color: #4A4949;\n"
                                "    border-style: solid;\n"
                                "    padding-top: 2px;\n"
                                "    padding-bottom: 2px;\n"
                                "    padding-left: 10px;\n"
                                "    padding-right: 10px;\n"
                                "    border-radius: 4px;\n"
                                "}\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scissors_btn = QtWidgets.QPushButton(self.centralwidget)
        self.scissors_btn.setGeometry(QtCore.QRect(870, 500, 231, 311))
        self.scissors_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scissors_btn.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Scissors.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scissors_btn.setIcon(icon)
        self.scissors_btn.setIconSize(QtCore.QSize(231, 311))
        self.scissors_btn.setObjectName("scissors_btn")

        self.ai_card = QtWidgets.QLabel(self.centralwidget)
        self.ai_card.setGeometry(QtCore.QRect(470, 30, 231, 311))
        self.ai_card.setPixmap(QtGui.QPixmap("back.jpg"))
        self.ai_card.setScaledContents(True)
        self.ai_card.setObjectName("ai_card")

        self.rock_card = QtWidgets.QLabel(self.centralwidget)
        self.rock_card.setGeometry(QtCore.QRect(470, 30, 0, 311))
        self.rock_card.setPixmap(QtGui.QPixmap("Rock.png"))
        self.rock_card.setScaledContents(True)
        self.rock_card.setObjectName("rock_card")

        self.paper_card = QtWidgets.QLabel(self.centralwidget)
        self.paper_card.setGeometry(QtCore.QRect(470, 30, 0, 311))
        self.paper_card.setPixmap(QtGui.QPixmap("Paper.png"))
        self.paper_card.setScaledContents(True)
        self.paper_card.setObjectName("paper_card")

        self.scissors_card = QtWidgets.QLabel(self.centralwidget)
        self.scissors_card.setGeometry(QtCore.QRect(470, 30, 0, 311))
        self.scissors_card.setPixmap(QtGui.QPixmap("Scissors.png"))
        self.scissors_card.setScaledContents(True)
        self.scissors_card.setObjectName("scissors_card")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(245, 340, 696, 145))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")

        self.rock_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rock_btn.setGeometry(QtCore.QRect(70, 500, 231, 311))
        self.rock_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rock_btn.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Rock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rock_btn.setIcon(icon1)
        self.rock_btn.setIconSize(QtCore.QSize(231, 311))
        self.rock_btn.setObjectName("rock_btn")

        self.paper_btn = QtWidgets.QPushButton(self.centralwidget)
        self.paper_btn.setGeometry(QtCore.QRect(470, 500, 231, 311))
        self.paper_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.paper_btn.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Paper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paper_btn.setIcon(icon2)
        self.paper_btn.setIconSize(QtCore.QSize(231, 311))
        self.paper_btn.setObjectName("paper_btn")

        ########## This button is for testing purpose ##########
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(460, 850, 250, 70))
        self.reset.setAutoFillBackground(False)
        ont = QtGui.QFont()
        font.setPointSize(24)
        self.reset.setFont(font)
        self.reset.setText("Play again")
        self.reset.setObjectName("reset")
        self.reset.clicked.connect(self.reset_ui)
        self.reset.setEnabled(False)
        #######################################################

        MainWindow.setCentralWidget(self.centralwidget)
        self.random_card = self.rock_card
        self.rock_btn.clicked.connect(self.reverse_card)
        self.paper_btn.clicked.connect(self.reverse_card)
        self.scissors_btn.clicked.connect(self.reverse_card)

        self.rock_btn.clicked.connect(lambda x : self.evaluate_result(self.rock_card))
        self.paper_btn.clicked.connect(lambda x : self.evaluate_result(self.paper_card))
        self.scissors_btn.clicked.connect(lambda x : self.evaluate_result(self.scissors_card))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def reverse_card(self):
        self.random_card = choice([self.rock_card, self.scissors_card, self.paper_card])
        self.reverse_card = QtCore.QPropertyAnimation(self.ai_card, b"geometry")
        self.reverse_card.setDuration(200)
        self.reverse_card.setStartValue(QtCore.QRect(470, 30, 231, 311))
        self.reverse_card.setEndValue(QtCore.QRect(605, 30, 0, 311))

        self.show_random_card = QtCore.QPropertyAnimation(self.random_card, b"geometry")
        self.show_random_card.setDuration(200)
        self.show_random_card.setStartValue(QtCore.QRect(605, 30, 0, 311))
        self.show_random_card.setEndValue(QtCore.QRect(470, 30, 231, 311))

        self.text_change = QtCore.QPropertyAnimation(self.label, b"geometry")
        self.text_change.setDuration(1)
        self.text_change.setStartValue(QtCore.QRect(245, 340, 696, 145))
        self.text_change.setEndValue(QtCore.QRect(245, 340, 698, 145))

        self.animation_group = QtCore.QSequentialAnimationGroup()
        self.animation_group.addAnimation(self.reverse_card)
        self.animation_group.addAnimation(self.show_random_card)
        self.animation_group.addAnimation(self.text_change)
        self.animation_group.start()

    def compare(self, cards):
        if (self.rock_card in cards) and (self.paper_card in cards):
            return self.paper_card
        elif (self.rock_card in cards) and (self.scissors_card in cards):
            return self.rock_card
        elif (self.paper_card in cards) and (self.scissors_card in cards):
            return self.scissors_card
        else:
            return 0

    def evaluate_result(self, card):
        
        winner = self.compare([card, self.random_card])
        if card == winner:
            self.label.setText(" YOU WIN !!")
            self.label.setStyleSheet("color:rgb(48, 150, 54);\n")
        elif winner == 0:
            self.label.setText("       Draw")
            self.label.setStyleSheet("color:rgb(116, 116, 116);\n")
        elif self.random_card == winner:
            self.label.setText(" YOU LOSE !!")      
            self.label.setStyleSheet("color:rgb(230, 0, 0);\n")

        self.reset.setEnabled(True)
        self.rock_btn.setEnabled(False)
        self.paper_btn.setEnabled(False)
        self.scissors_btn.setEnabled(False)

    
    def reset_ui(self):
        self.ai_card.setGeometry(QtCore.QRect(470, 30, 231, 311))
        self.paper_card.setGeometry(QtCore.QRect(470, 30, 0, 311))
        self.rock_card.setGeometry(QtCore.QRect(470, 30, 0, 311))
        self.scissors_card.setGeometry(QtCore.QRect(470, 30, 0, 311))
        self.label.setText("Pick a card!")
        self.label.setStyleSheet("color:rgb(0, 0, 0);\n")
        self.reset.setEnabled(False)
        self.rock_btn.setEnabled(True)
        self.paper_btn.setEnabled(True)
        self.scissors_btn.setEnabled(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock Paper Scissors"))
        self.scissors_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>choose Scissors</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Pick a card!"))
        self.rock_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>choose ROCK !</p></body></html>"))
        self.paper_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>choose paper</p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
