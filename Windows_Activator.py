# -*- coding: utf-8 -*-
import subprocess
from PyQt5 import QtGui, QtWidgets,QtCore
from PyQt5.QtWidgets import QLabel, QMessageBox
import datetime
import sys
from utils import logger, command_run, windows_installer, office_installer
from imgs import resources
from interfaces import Main_Window
# словарь с чекбоксами
active_checkboxes = {'windows_checkbox': False, 'office_checkbox': False}
 
log_file = logger.Logger()


def active_checkbox_windows(checked):
    active_checkboxes['windows_checkbox'] = checked

def active_checkbox_office(checked):
    active_checkboxes['office_checkbox'] = checked
   
def start_commands(self):
    if active_checkboxes['windows_checkbox'] and not active_checkboxes['office_checkbox']:
        self.label = QLabel("Пожалуйста ожидайте \n Процесс активации может занимать до 10 минут")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.move(60,20)
        self.layout().addWidget(self.label)
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Была нажата кнопка Выполнить")
        command_sfc = command_run.CommandRun("sfc /scannow")
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Был создан класс command_sfc")
        progress_bar = self.get_progress()  # Получаем progressBar из self
        win_inst = windows_installer.windows_installer(log_file, progress_bar, self.label)
        command_sfc.finished_signal.connect(lambda: win_inst.check_exit_code(command_sfc))
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная привязка функции исполнения команды")
        command_sfc.start()
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешный старт команды sfc /scannow")
    elif not active_checkboxes['windows_checkbox'] and active_checkboxes['office_checkbox']:
        # для случая когда пользователь выбрал только активацию office
        self.label = QLabel("Пожалуйста ожидайте \n Процесс активации может занимать до 10 минут")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.move(60,20)
        self.layout().addWidget(self.label)
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Была нажата кнопка Выполнить")
        command_reg__add = command_run.CommandRun(r'reg add "HKCU\Software\Microsoft\Office\16.0\Common\ExperimentConfigs\Ecs" /v "CountryCode" /t REG_SZ /d "std::wstring|US" /f')
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Был создан класс command_reg__add")
        progress_bar = self.get_progress()
        office_inst = office_installer.office_installer(log_file, progress_bar, self.label)
        command_reg__add.finished_signal.connect(lambda: office_inst.check_exit_code_office(command_reg__add))
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная привязка функции исполнения команды")
        command_reg__add.start()
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешный старт команды reg add")
    elif (active_checkboxes['office_checkbox'] and active_checkboxes['windows_checkbox']):
        # для случая когда пользователь выбрал и активацию windows и активацию office
        self.label = QLabel("Пожалуйста ожидайте \n Процесс активации и установки может занимать\n до 10 минут")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.move(60,20)
        self.layout().addWidget(self.label)
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Была нажата кнопка Выполнить")
        command_sfc = command_run.CommandRun("sfc /scannow")
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Был создан класс command_sfc")
        progress_bar = self.get_progress()
        win_inst = windows_installer.windows_installer(log_file, progress_bar, self.label, wo=True)
        command_sfc.finished_signal.connect(lambda: win_inst.check_exit_code(command_sfc))
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная привязка функции исполнения команды")
        command_sfc.start()
        log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешный старт команды sfc /scannow")
        
        office_inst = office_installer.office_installer(log_file, progress_bar, self.label,True)
        win_inst.activation_complete_signal.connect(lambda: start_office_activation(self))
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Ошибка")
        msg.setText("Для того чтобы запустить выполнение каких-либо действий выберите эти действия!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

def start_office_activation(self):
    self.label.setText("Начинается активация Office...")
    log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Начинается активация Office")
    command_reg__add = command_run.CommandRun(r'reg add "HKCU\Software\Microsoft\Office\16.0\Common\ExperimentConfigs\Ecs" /v "CountryCode" /t REG_SZ /d "std::wstring|US" /f')
    log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Был создан класс command_reg__add")
    progress_bar = self.get_progress()
    office_inst = office_installer.office_installer(log_file, progress_bar, self.label, wo=True)
    command_reg__add.finished_signal.connect(lambda: office_inst.check_exit_code_office(command_reg__add))
    log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная привязка функции исполнения команды")
    command_reg__add.start()
    log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешный старт команды reg add")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("imgs/logo.png"))
    
    log_file = logger.Logger()
    log_file.create_new_log_file()
    log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешный запуск Windows Activator")
    
    main_window = Main_Window.MainWindow(log_file)
    main_window.show()
    progress_bar = main_window.get_progress
    sys.exit(app.exec_())