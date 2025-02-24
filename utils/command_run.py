from PyQt5 import QtCore
import subprocess
path_to_dir = None
class CommandRun(QtCore.QThread):
    finished_signal = QtCore.pyqtSignal()

    def __init__(self, command, path_to_dir=None):
        super().__init__()
        self.path_to_dir = path_to_dir
        self.command = command
        self.result_code = 0

    def run(self):
        if (path_to_dir != None):
             process = subprocess.Popen(self.command, shell=True, cwd=path_to_dir)
             process.wait()
             self.result_code = process.returncode
             self.finished_signal.emit()
        else:
             process = subprocess.Popen(self.command, shell=True)
             process.wait()
             self.result_code = process.returncode
             self.finished_signal.emit()
    def get_result_code(self):
        return self.result_code
    