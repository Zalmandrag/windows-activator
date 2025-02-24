import datetime

class Logger:
    def __init__(self):
        self.current_date = datetime.datetime.now().strftime("%d_%m_%Y")
        self.current_time = datetime.datetime.now().strftime("%H-%M")
        self.create_new_log_file()
        
    def create_new_log_file(self):
        self.log_file_name = f"{self.current_date}_{self.current_time}.txt" 
        with open(self.log_file_name, 'w'):
            pass
            
    def write(self, text):
        with open(self.log_file_name, "a", encoding="utf-8") as log_file:
            log_file.write(text + "\n")