from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QHBoxLayout
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import *


class ZTermTitleBar(MSFluentTitleBar):
    """Title bar with icon and title"""

    def __init__(self, parent):
        super().__init__(parent)

        # add buttons
        self.toolButtonLayout = QHBoxLayout()
        color = QColor(206, 206, 206) if isDarkTheme() else QColor(96, 96, 96)
        self.searchButton = TransparentToolButton(
            FIF.SEARCH_MIRROR.icon(color=color), self
        )
        self.settingsButton = TransparentToolButton(
            FIF.SETTING.icon(color=color), self
        )

        self.toolButtonLayout.setContentsMargins(20, 0, 20, 0)
        self.toolButtonLayout.setSpacing(10)
        self.toolButtonLayout.addWidget(self.searchButton)
        self.toolButtonLayout.addWidget(self.settingsButton)
        self.hBoxLayout.insertLayout(4, self.toolButtonLayout)

        # add tab bar
        self.tabBar = TabBar(self)

        self.tabBar.setMovable(True)
        self.tabBar.setTabMaximumWidth(220)
        self.tabBar.setTabShadowEnabled(False)
        self.tabBar.setTabSelectedBackgroundColor(
            QColor(255, 255, 255, 125), QColor(255, 255, 255, 50)
        )
        # self.tabBar.setScrollable(True)
        self.tabBar.setCloseButtonDisplayMode(TabCloseButtonDisplayMode.ON_HOVER)

        # self.tabBar.tabCloseRequested.connect(self.tabBar.removeTab)
        # self.tabBar.currentChanged.connect(lambda i: print(self.tabBar.tabText(i)))

        self.hBoxLayout.insertWidget(5, self.tabBar, 1)
        self.hBoxLayout.setStretch(6, 0)

    def canDrag(self, pos: QPoint):
        if not super().canDrag(pos):
            return False

        pos.setX(pos.x() - self.tabBar.x())
        return not self.tabBar.tabRegion().contains(pos)
