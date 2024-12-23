# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLayout,
                               QPushButton, QSizePolicy, QSpacerItem, QWidget)


class Ui_signup(object):
    def setupUi(self, signup):
        if not signup.objectName():
            signup.setObjectName(u"signup")
        signup.resize(1000, 720)
        self.horizontalLayoutWidget = QWidget(signup)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1001, 83))
        self.headerHorizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.headerHorizontalLayout.setObjectName(u"headerHorizontalLayout")
        self.headerHorizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.headerHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerGraphicsView = QGraphicsView(self.horizontalLayoutWidget)
        self.headerGraphicsView.setObjectName(u"headerGraphicsView")

        self.headerHorizontalLayout.addWidget(self.headerGraphicsView, 0, Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerHorizontalLayout.addItem(self.horizontalSpacer)

        self.ciftliklerButton = QPushButton(self.horizontalLayoutWidget)
        self.ciftliklerButton.setObjectName(u"ciftliklerButton")
        self.ciftliklerButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))

        self.headerHorizontalLayout.addWidget(self.ciftliklerButton)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.headerHorizontalLayout.addItem(self.horizontalSpacer_4)

        self.urunlerButton = QPushButton(self.horizontalLayoutWidget)
        self.urunlerButton.setObjectName(u"urunlerButton")
        self.urunlerButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))

        self.headerHorizontalLayout.addWidget(self.urunlerButton)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.headerHorizontalLayout.addItem(self.horizontalSpacer_2)

        self.accountButton = QPushButton(self.horizontalLayoutWidget)
        self.accountButton.setObjectName(u"accountButton")
        self.accountButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))

        self.headerHorizontalLayout.addWidget(self.accountButton, 0, Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.headerHorizontalLayout.addItem(self.horizontalSpacer_3)

        self.retranslateUi(signup)

        QMetaObject.connectSlotsByName(signup)

    # setupUi

    def retranslateUi(self, signup):
        signup.setWindowTitle(QCoreApplication.translate("signup", u"signup", None))
        self.ciftliklerButton.setText(QCoreApplication.translate("signup", u"\u00c7iftlikler", None))
        self.urunlerButton.setText(QCoreApplication.translate("signup", u"\u00dcr\u00fcnler", None))
        self.accountButton.setText(QCoreApplication.translate("signup", u"Hesap", None))
    # retranslateUi
