APP_STYLES = """
QMainWindow {
    background-color: #2D2D2D;
    color: #FFFFFF;
    font-family: 'Segoe UI';
}

/* Стили для чекбоксов */
QCheckBox {
    color: #FFFFFF;
    font-size: 16px;
    spacing: 10px;
    margin: 15px;
}

QCheckBox::indicator {
    width: 20px;
    height: 20px;
    border: 2px solid #4CAF50;
    border-radius: 4px;
    background-color: transparent;
}

QCheckBox::indicator:checked {
    background-color: #4CAF50;
    image: url(:/icons/checked.png);
}

QCheckBox::indicator:hover {
    border: 2px solid #45a049;
}

QCheckBox#checkbox_windows {
    color: #FFD700;
}

QCheckBox#checkbox_office {
    color: #00BFFF;
}

/* Стили для кнопки */
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

/* Стили для метки */
QLabel {
    color: #FFFFFF;
    font-size: 20px;
    font-weight: bold;
    margin: 20px;
}

/* Стили для прогресс-бара */
QProgressBar {
    background: #404040;
    border-radius: 5px;
    height: 30px;
    margin: 20px;
    text-align: center;
    font-size: 16px;
    color: white;
}

QProgressBar::chunk {
    background: #4CAF50;
    border-radius: 5px;
    width: 10px;
}

/* Групповая рамка */
QGroupBox {
    border: 2px solid #4CAF50;
    border-radius: 10px;
    margin-top: 10px;
    padding: 15px;
}

QGroupBox::title {
    color: #4CAF50;
    subcontrol-origin: margin;
    left: 10px;
}
QLabel#label_wait {
    padding-left: 40px;
    text-align: center;
}
"""