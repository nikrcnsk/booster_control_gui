from PyQt5.QtWidgets import QWidget, QLineEdit, QApplication, QPushButton, QGridLayout, QMessageBox, QFrame, QLabel

import sys
import json
import signal


# close programm by prss CTRL+C
signal.signal(signal.SIGINT, signal.SIG_DFL)


class windowButton(QPushButton):
    def __init__(self, text, custom_data):
        super().__init__(text)
        self.text = text
        self.custom_data = custom_data
        self.clicked.connect(self.on_click)


    def on_click(self):
        self.window = QWidget()
        self.window.setWindowTitle(f"{self.text}")
        self.window.setMinimumWidth(200)
        self.window.setMinimumHeight(200)

        self.grid = QGridLayout()

        n_max_in_row = 4
        i = 0

        for el in self.custom_data:
            self.frame = QFrame()
            self.frame.setFrameShape(QFrame.StyledPanel)
            self.label = QLabel(self.frame)
            # self.label.setAlignment(Qt.AlignCenter)
            self.label.setText(el["name"])
            self.grid.addWidget(self.frame, i // n_max_in_row, i % n_max_in_row)
            i += 1

        self.window.setLayout(self.grid)
        self.window.show()
        # self.window.hide()

    def closeEvent(self, ev):
        ev.accept()



class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()


        with open('booster.json', 'r') as file:
            config = json.load(file)

        booster_config = config["booster"]

        grid = QGridLayout()

        n_max_in_row = 4
        i = 0
        for ss, elems in booster_config.items():
            btn = windowButton(ss, config["booster"][ss])
            
            grid.addWidget(btn, i // n_max_in_row, i % n_max_in_row)
            i += 1
            
        self.setLayout(grid)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cw = CustomWidget()
    sys.exit(app.exec_())

