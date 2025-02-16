# -*- coding: utf-8 -*-
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import sys

# Стили для приложения
APP_STYLES = """
QMainWindow {
    background-color: #2D2D2D;
    color: #FFFFFF;
    font-family: 'Segoe UI';
}

QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #4CAF50, stop:1 #45a049);
    color: white;
    border-radius: 8px;
    padding: 15px 30px;
    font-size: 16px;
    border: none;
    min-width: 200px;
    margin: 10px;
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #45a049, stop:1 #4CAF50);
}

QPushButton:pressed {
    background: #357a38;
}

QLabel {
    color: #FFFFFF;
    font-size: 20px;
    font-weight: bold;
    margin: 20px;
}

QProgressBar {
    background: #404040;
    border-radius: 5px;
    height: 20px;
    margin: 20px;
}

QProgressBar::chunk {
    background: #4CAF50;
    border-radius: 5px;
    width: 10px;
}
"""

class Logger:
    def __init__(self):
        self.current_date = datetime.datetime.now().strftime("%d_%m_%Y")
        self.current_time = datetime.datetime.now().strftime("%H-%M")
        
    def create_new_log_file(self):
        self.log_file_name = f"{self.current_date}_{self.current_time}.txt" 
        with open(self.log_file_name, 'w'):
            pass
            
    def write(self, text):
        with open(self.log_file_name, "a", encoding="utf-8") as log_file:
            log_file.write(text + "\n")

class CommandRun(QtCore.QThread):
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

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setStyleSheet(APP_STYLES)
        
    def setup_ui(self):
        self.setWindowTitle("Windows Activator")
        self.setMinimumSize(600, 400)
        
        # Центральный виджет и layout
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Элементы интерфейса
        self.label = QtWidgets.QLabel("Вас приветствует Windows Activator!")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.pushButton = QtWidgets.QPushButton("Активировать Windows")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setValue(0)
        
        # Добавление элементов в layout
        main_layout.addStretch()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.pushButton, 0, QtCore.Qt.AlignCenter)
        main_layout.addStretch()
        main_layout.addWidget(self.progressBar)
        
        # Подключение сигналов
        self.pushButton.clicked.connect(self.start_commands)
        
        # Эффект тени для кнопки
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(3, 3)
        self.pushButton.setGraphicsEffect(shadow)

    def start_commands(self):
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Была нажата кнопка Активировать Windows")
        self.progressBar.setValue(10)
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Было установлено значение прогресс бара на 10%")
        command_sfc = CommandRun("sfc /scannow")
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Был создан класс command_sfc")
        command_sfc.finished_signal.connect(lambda: self.check_exit_code(command_sfc))
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная привязка функции исполнения команды")
        command_sfc.start()
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешный старт команды sfc /scannow")

    def check_exit_code(self, command_sfc):
        if command_sfc.get_result_code() == 0:
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная обработка команды sfc /scannow")
            self.progressBar.setValue(25)
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная установка значения прогресс бара на 25%")
            command_slmgr_ipk = CommandRun("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешное создание класса command_slmgr_ipk")
            command_slmgr_ipk.finished_signal.connect(lambda: self.check_exit_code_ipk(command_slmgr_ipk))
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная привязка функции исполнения команды")
            command_slmgr_ipk.start()
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешный старт команды slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        else:
            str_get_result_code = str(command_sfc.get_result_code())
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [ERROR] Команда sfc /scannow завершилась с кодом: {str_get_result_code}")

    def check_exit_code_ipk(self, ssilka):
        if ssilka.get_result_code() == 0:
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная обработка команды slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
            self.progressBar.setValue(50)
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная установка значения прогресс бара на 50%")
            command_slmgr_skms = CommandRun("slmgr /skms kms.digiboy.ir")
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешное создание класса command_slmgr_skms")
            command_slmgr_skms.finished_signal.connect(lambda: self.check_exit_code_skms(command_slmgr_skms))
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная привязка функции исполнения команды")
            command_slmgr_skms.start()
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешный старт команды slmgr /skms kms.digiboy.ir")
        else:
            str_get_result_code = str(ssilka.get_result_code())
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [ERROR] Команда slmgr /ipk завершилась с кодом: {str_get_result_code}")

    def check_exit_code_skms(self, ssilka):
        if ssilka.get_result_code() == 0:
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная обработка команды slmgr /skms kms.digiboy.ir")
            self.progressBar.setValue(75)
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная установка значения прогресс бара на 75%")
            command_slmgr_ato = CommandRun("slmgr /ato")
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешное создание класса command_slmgr_ato")
            command_slmgr_ato.finished_signal.connect(lambda: self.check_exit_code_ato(command_slmgr_ato))
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная привязка функции исполнения команды")
            command_slmgr_ato.start()
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешный старт команды slmgr /ato")
        else:
            str_get_result_code = str(ssilka.get_result_code())
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [ERROR] Команда slmgr /skms завершилась с кодом: {str_get_result_code}")

    def check_exit_code_ato(self, ssilka):
        if ssilka.get_result_code() == 0:
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная обработка команды slmgr /ato")
            self.progressBar.setValue(100)
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная установка значения прогресс бара на 100%")
        else:
            str_get_result_code = str(ssilka.get_result_code())
            log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [ERROR] Команда slmgr /ato завершилась с кодом: {str_get_result_code}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    log_file.create_new_log_file()
    log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешный запуск Windows Activator")
    sys.exit(app.exec_())