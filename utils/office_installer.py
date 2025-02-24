import datetime,subprocess
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import command_run
wo = False
progress = None
label = None
class office_installer:
 def __init__(self, log_file,progress,label, wo=False):
    self.wo = wo
    self.log_file = log_file
    self.progress = progress
    self.label = label
 def check_exit_code_office(self, command):
       if (wo):
            if (command.get_result_code == 0):
             self.log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная обработка команды reg add")
             process = subprocess.Popen(r".\setup.exe /configure .\configuration-Office2021Enterprise.xml", shell=True)
             self.progress.setValue(65)
             self.check_exit_code_setup()
       else:
             self.log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная обработка команды reg add")
             process = subprocess.Popen(r".\setup.exe /configure .\configuration-Office2021Enterprise.xml", shell=True)
             self.progress.setValue(15)
             self.check_exit_code_setup()

 def check_exit_code_setup(self):
            self.log_file.write(f"{datetime.datetime.now().strftime('%d_%m_%Y')}_{datetime.datetime.now().strftime('%H-%M')} [INFO] Успешная активация office")
            self.label.setText("Активация выполнена успешно!")
            self.progress.setValue(100)