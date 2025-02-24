import sys, os
import datetime
from PyQt5 import QtCore
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import command_run
wo = False
progress = None
label = None
from PyQt5 import QtCore

class windows_installer(QtCore.QObject):
    activation_complete_signal = QtCore.pyqtSignal()

    def __init__(self, log_file, progress, label, wo=False):
        super().__init__()
        self.log_file = log_file
        self.wo = wo
        self.progress = progress
        self.label = label

    def check_exit_code(self, command_sfc):
        if command_sfc.get_result_code() == 0:
            self.log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешное выполнение комадны sfc /scannow")
            self.progress.setValue(15)
            command_slmgr_ipk = command_run.CommandRun("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
            command_slmgr_ipk.finished_signal.connect(lambda: self.check_exit_code_ipk(command_slmgr_ipk))
            command_slmgr_ipk.start()

    def check_exit_code_ipk(self, ssilka):
        if ssilka.get_result_code() == 0:
            self.log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Учпешное выполнение команды slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
            self.progress.setValue(30)
            command_slmgr_skms = command_run.CommandRun("slmgr /skms kms.digiboy.ir")
            command_slmgr_skms.finished_signal.connect(lambda: self.check_exit_code_skms(command_slmgr_skms))
            command_slmgr_skms.start()
        else:
            str_get_result_code = str(ssilka.get_result_code())

    def check_exit_code_skms(self, ssilka):
        if not self.wo:
            if ssilka.get_result_code() == 0:
                self.log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] slmgr /skms kms.digiboy.ir")
                self.progress.setValue(40)
                command_slmgr_ato = command_run.CommandRun("slmgr /ato")
                command_slmgr_ato.finished_signal.connect(lambda: self.check_exit_code_ato(command_slmgr_ato, self.label))
                command_slmgr_ato.start()
            else:
                str_get_result_code = str(ssilka.get_result_code())
        else:
            if ssilka.get_result_code() == 0:
                self.log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] slmgr /skms kms.digiboy.ir")
                self.progress.setValue(40)
                command_slmgr_ato = command_run.CommandRun("slmgr /ato")
                command_slmgr_ato.finished_signal.connect(lambda: self.check_exit_code_ato(command_slmgr_ato, self.label, 50))
                command_slmgr_ato.start()

    def check_exit_code_ato(self, ssilka, label, progress=100):
        if ssilka.get_result_code() == 0:
            self.log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная активация windows")
            self.label.setText("Активация выполнена успешно!")
            self.progress.setValue(progress)
            self.activation_complete_signal.emit()
        else:
            str_get_result_code = str(ssilka.get_result_code())