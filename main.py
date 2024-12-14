# -*- coding: utf-8 -*-
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import sys

class Logger:
    def __init__(self):
        self.current_date = datetime.datetime.now().strftime("%d_%m_%Y")
        self.current_time = datetime.datetime.now().strftime("%H-%M")
    def create_new_log_file(self):
        self.log_file_name = f"{self.current_date}_{self.current_time}.txt" 
        self.log_file = open(self.log_file_name, 'w')
        self.log_file.close()
    def write(self, text):
        with open(self.log_file_name, "a", encoding="utf-8") as log_file:
            log_file.write(text + "\n")
class Command_run(QtCore.QThread):
    finished_signal = QtCore.pyqtSignal()

    def __init__(self, command):
        super().__init__()
        self.command = command
        self.result_code = 0

    def run(self):
        process = subprocess.Popen(self.command, shell=True)
        process.wait() 
        self.result_code = process.returncode 
        self.finished_signal.emit() 

    def get_result_code(self):
         return self.result_code
log_file = Logger()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 270, 188, 13))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 380, 151, 61))
        self.pushButton.setObjectName("pushButton")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 530, 781, 51))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect button click
        self.pushButton.clicked.connect(self.start_commands)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Windows Activator"))
        self.label.setText(_translate("MainWindow", "Вас приветствует Windows Activator!"))
        self.pushButton.setText(_translate("MainWindow", "Активировать Windows"))
        self.progressBar.setValue(0)

    def start_commands(self):
        log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Была нажата кнопка Активировать Windows")
        self.progressBar.setValue(10)
        log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Было установленно значение прогрес бара на 10%")
        command_sfc = Command_run("sfc /scannow")
        log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Был создан класс command_sfc")
        command_sfc.finished_signal.connect(lambda: self.check_exit_code(command_sfc))
        log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешная привязка функции исполнения комманды")
        command_sfc.start()
        log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешный старт коммадны sfc /scannow")

    def check_exit_code(self, command_sfc):
        if command_sfc.get_result_code() == 0:
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешная обработка комманды sfc /scannow")
            self.progressBar.setValue(25)
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешная установка значения прогрес бара на 25%")
            command_slmgr_ipk = Command_run("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешное содание класса command_slmgr_ipk")
            command_slmgr_ipk.finished_signal.connect(lambda: self.check_exit_code_ipk(command_slmgr_ipk))
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешная привязка функции исполнения комманды")
            command_slmgr_ipk.start()
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешный старт коммадны slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        else:
            str_get_result_code = str(command_sfc.get_result_code)
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [ERROR] Комманда sfc /scannow завершилась с кодом: {str_get_result_code}")
    def check_exit_code_ipk(self, ssilka):
        if ssilka.get_result_code() == 0:
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешная обработка комманды slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
            self.progressBar.setValue(50)
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешная установка значения прогрес бара на 50%")
            command_slmgr_skms = Command_run("slmgr /skms kms.digiboy.ir")
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешное содание класса command_slmgr_skms")
            command_slmgr_skms.finished_signal.connect(lambda: self.check_exit_code_skms(command_slmgr_skms))
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешная привязка функции исполнения комманды")
            command_slmgr_skms.start()
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешный старт коммадны slmgr /skms kms.digiboy.ir")
        else:
            str_get_result_code = str(command_slmgr_skms.get_result_code)
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [ERROR] Комманда sfc /scannow завершилась с кодом: {str_get_result_code}")
    def check_exit_code_skms(self, ssilka):
        if ssilka.get_result_code() == 0:
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешная обработка комманды slmgr /skms kms.digiboy.ir")
            self.progressBar.setValue(75)
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешная установка значения прогрес бара на 75%")
            command_slmgr_ato = Command_run("slmgr /ato")
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешное содание класса command_slmgr_ato")
            command_slmgr_ato.finished_signal.connect(lambda: self.check_exit_code_ato(command_slmgr_ato))
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешная привязка функции исполнения комманды")
            command_slmgr_ato.run()
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешный старт коммадны slmgr /ato")
        else:
            str_get_result_code = str(command_slmgr_ato.get_result_code)
            log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [ERROR] Комманда sfc /scannow завершилась с кодом: {str_get_result_code}")
    def check_exit_code_ato (self, ssilka):
        if ssilka.get_result_code() == 0: 
         log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешная обработка комманды slmgr /ato")
         self.progressBar.setValue(100)
         log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] Успешная установка значения прогрес бара на 100%")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    log_file.create_new_log_file()
    log_file.write(f"{datetime.datetime.now().strftime("%d_%m_%Y")}_{datetime.datetime.now().strftime("%H-%M")} [INFO] успшеный запуск Windows Activator")
    sys.exit(app.exec_())