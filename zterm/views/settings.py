from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from qfluentwidgets import *


class Settings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(30, 30, 30, 30)
        self.vBoxLayout.setSpacing(20)

        self.title_text = TitleLabel("Z-Term Settings")


        # Shell Combo
        self.hBoxLayout1 = QHBoxLayout()
        self.hBoxLayout1.setContentsMargins(30, 30, 30, 30)
        self.hBoxLayout1.setSpacing(20)
        self.hBoxWidget1 = QWidget(self)
        self.hBoxWidget1.setLayout(self.hBoxLayout1)

        self.shell_select_label = BodyLabel("Shell", self)

        self.shell_select = ComboBox(self)
        self.shell_select.addItems(['bash', 'fish', 'powershell', 'cmd.exe'])

        self.hBoxLayout1.addWidget(self.shell_select_label)
        self.hBoxLayout1.addWidget(self.shell_select)

        # Font
        self.hBoxLayout2 = QHBoxLayout()
        self.hBoxLayout2.setContentsMargins(30, 30, 30, 30)
        self.hBoxLayout2.setSpacing(20)
        self.hBoxWidget2 = QWidget(self)
        self.hBoxWidget2.setLayout(self.hBoxLayout2)

        self.font_label = BodyLabel("Font", self)

        self._font = ComboBox(self)
        self._font.addItems(['Monaspace Krypton', 'Cascadia Mono', 'Consolas', 'monospace'])

        self.hBoxLayout2.addWidget(self.font_label)
        self.hBoxLayout2.addWidget(self._font)

        # Font Size
        self.hBoxLayout3 = QHBoxLayout()
        self.hBoxLayout3.setContentsMargins(30, 30, 30, 30)
        self.hBoxLayout3.setSpacing(20)
        self.hBoxWidget3 = QWidget(self)
        self.hBoxWidget3.setLayout(self.hBoxLayout3)

        self.font_size_label = BodyLabel("Font Size", self)

        self.font_size = ComboBox(self)
        self.font_size.addItems(map(str, [i for i in range(8, 65)]))

        self.hBoxLayout3.addWidget(self.font_size_label)
        self.hBoxLayout3.addWidget(self.font_size)

        # Add them all
        self.vBoxLayout.addWidget(self.title_text)
        self.vBoxLayout.addWidget(self.hBoxWidget1)
        self.vBoxLayout.addWidget(self.hBoxWidget2)
        self.vBoxLayout.addWidget(self.hBoxWidget3)

        self.setObjectName("Settings")
