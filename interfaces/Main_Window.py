from PyQt5 import QtWidgets, QtGui, QtCore
import sys, os
import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import styles
import Windows_Activator
from utils import office_installer, windows_installer

log_file = None
progress_bar = None
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, log_file):
        super().__init__()
        self.log_file = log_file
        self.setup_ui()
        self.setStyleSheet(styles.APP_STYLES)

    def setup_ui(self):
        self.setWindowTitle("Windows Activator")
        self.setMinimumSize(800, 600)  # Увеличиваем размер окна
        
        # Главный контейнер
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        
        # Основной layout
        self.main_layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(self.main_layout)
        
        # Группа для выбора действий
        group_box = QtWidgets.QGroupBox("Выберите действия:")
        group_layout = QtWidgets.QVBoxLayout()
        
        # Чекбоксы
        self.checkbox_windows = QtWidgets.QCheckBox("Активировать Windows")
        self.checkbox_office = QtWidgets.QCheckBox("Установить Office")
        self.checkbox_windows.setObjectName("checkbox_windows")
        self.checkbox_office.setObjectName("checkbox_office")
        
        group_layout.addWidget(self.checkbox_windows)
        group_layout.addWidget(self.checkbox_office)
        group_box.setLayout(group_layout)
        
        self.pushButton = QtWidgets.QPushButton("Выполнить")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setValue(0)
        self.progressBar.setFormat("%p%")
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        
        self.main_layout.addWidget(group_box)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.pushButton, 0, QtCore.Qt.AlignCenter)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.progressBar)
        
        self.message_widget = QtWidgets.QWidget()
        self.message_layout = QtWidgets.QVBoxLayout()
        self.message_widget.setLayout(self.message_layout)
        self.main_layout.addWidget(self.message_widget)
        
        self.pushButton.clicked.connect(lambda: Windows_Activator.start_commands(self))
        self.checkbox_windows.stateChanged.connect(Windows_Activator.active_checkbox_windows)
        self.checkbox_office.stateChanged.connect(Windows_Activator.active_checkbox_office)
        
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QtGui.QColor(0, 0, 0, 150))
        shadow.setOffset(5, 5)
        self.pushButton.setGraphicsEffect(shadow)

    def get_progress(self):
        return self.progressBar