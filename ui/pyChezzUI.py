# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\pyChezzMinUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(309, 397)
        Form.setStyleSheet(_fromUtf8(".blackBG{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(122, 97, 74, 255), stop:1 rgba(153, 125, 94, 255));border-radius: 5px;}\n"
".whiteBG{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 196), stop:1 rgb(255, 253, 225));border-radius: 5px;}\n"
"\n"
".darkBG{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(20, 20, 20), stop:1 rgb(70, 70, 70));border-radius: 7px;}\n"
".lightBG{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(200, 200, 200), stop:1 rgb(255, 255, 225));border-radius: 7px;}\n"
"\n"
".permissionYES{background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(100, 164, 100, 255), stop:1 rgba(171, 232, 171, 255));border-radius: 7px;}\n"
".permissionNO{background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(168, 80, 80, 255), stop:1 rgba(236, 148, 148, 255));border-radius: 7px;}\n"
"\n"
".parking{background-color: rgb(100,100, 100);border-radius: 7px; border: 1px solid gray;}\n"
"\n"
"/* dark orange stylesheet */\n"
"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"/*  END */\n"
"\n"
""))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.layMain = QtGui.QHBoxLayout()
        self.layMain.setObjectName(_fromUtf8("layMain"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnOpen = QtGui.QPushButton(Form)
        self.btnOpen.setObjectName(_fromUtf8("btnOpen"))
        self.horizontalLayout.addWidget(self.btnOpen)
        self.btnSave = QtGui.QPushButton(Form)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.horizontalLayout.addWidget(self.btnSave)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.frmOpponentPark = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmOpponentPark.sizePolicy().hasHeightForWidth())
        self.frmOpponentPark.setSizePolicy(sizePolicy)
        self.frmOpponentPark.setMinimumSize(QtCore.QSize(0, 32))
        self.frmOpponentPark.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmOpponentPark.setFrameShadow(QtGui.QFrame.Raised)
        self.frmOpponentPark.setObjectName(_fromUtf8("frmOpponentPark"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frmOpponentPark)
        self.horizontalLayout_2.setContentsMargins(1, 0, 1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pebleOppDark = QtGui.QFrame(self.frmOpponentPark)
        self.pebleOppDark.setMinimumSize(QtCore.QSize(15, 0))
        self.pebleOppDark.setMaximumSize(QtCore.QSize(15, 16777215))
        self.pebleOppDark.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pebleOppDark.setFrameShadow(QtGui.QFrame.Raised)
        self.pebleOppDark.setObjectName(_fromUtf8("pebleOppDark"))
        self.horizontalLayout_2.addWidget(self.pebleOppDark)
        self.pebleOppLight = QtGui.QFrame(self.frmOpponentPark)
        self.pebleOppLight.setMinimumSize(QtCore.QSize(15, 0))
        self.pebleOppLight.setMaximumSize(QtCore.QSize(15, 16777215))
        self.pebleOppLight.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pebleOppLight.setFrameShadow(QtGui.QFrame.Raised)
        self.pebleOppLight.setObjectName(_fromUtf8("pebleOppLight"))
        self.horizontalLayout_2.addWidget(self.pebleOppLight)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.frmOpponentPark)
        self.grdFields = QtGui.QFrame(Form)
        self.grdFields.setObjectName(_fromUtf8("grdFields"))
        self.grdFieldsLayout = QtGui.QGridLayout(self.grdFields)
        self.grdFieldsLayout.setMargin(10)
        self.grdFieldsLayout.setSpacing(0)
        self.grdFieldsLayout.setObjectName(_fromUtf8("grdFieldsLayout"))
        self.fieldG1 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldG1.sizePolicy().hasHeightForWidth())
        self.fieldG1.setSizePolicy(sizePolicy)
        self.fieldG1.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldG1.setObjectName(_fromUtf8("fieldG1"))
        self.grdFieldsLayout.addWidget(self.fieldG1, 7, 6, 1, 1)
        self.fieldF1 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldF1.sizePolicy().hasHeightForWidth())
        self.fieldF1.setSizePolicy(sizePolicy)
        self.fieldF1.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldF1.setObjectName(_fromUtf8("fieldF1"))
        self.grdFieldsLayout.addWidget(self.fieldF1, 7, 5, 1, 1)
        self.fieldH1 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldH1.sizePolicy().hasHeightForWidth())
        self.fieldH1.setSizePolicy(sizePolicy)
        self.fieldH1.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldH1.setObjectName(_fromUtf8("fieldH1"))
        self.grdFieldsLayout.addWidget(self.fieldH1, 7, 7, 1, 1)
        self.fieldD5 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldD5.sizePolicy().hasHeightForWidth())
        self.fieldD5.setSizePolicy(sizePolicy)
        self.fieldD5.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldD5.setObjectName(_fromUtf8("fieldD5"))
        self.grdFieldsLayout.addWidget(self.fieldD5, 3, 3, 1, 1)
        self.fieldF5 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldF5.sizePolicy().hasHeightForWidth())
        self.fieldF5.setSizePolicy(sizePolicy)
        self.fieldF5.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldF5.setObjectName(_fromUtf8("fieldF5"))
        self.grdFieldsLayout.addWidget(self.fieldF5, 3, 5, 1, 1)
        self.fieldA6 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldA6.sizePolicy().hasHeightForWidth())
        self.fieldA6.setSizePolicy(sizePolicy)
        self.fieldA6.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldA6.setObjectName(_fromUtf8("fieldA6"))
        self.grdFieldsLayout.addWidget(self.fieldA6, 2, 0, 1, 1)
        self.fieldA5 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldA5.sizePolicy().hasHeightForWidth())
        self.fieldA5.setSizePolicy(sizePolicy)
        self.fieldA5.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldA5.setObjectName(_fromUtf8("fieldA5"))
        self.grdFieldsLayout.addWidget(self.fieldA5, 3, 0, 1, 1)
        self.fieldB5 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldB5.sizePolicy().hasHeightForWidth())
        self.fieldB5.setSizePolicy(sizePolicy)
        self.fieldB5.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldB5.setObjectName(_fromUtf8("fieldB5"))
        self.grdFieldsLayout.addWidget(self.fieldB5, 3, 1, 1, 1)
        self.fieldH7 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldH7.sizePolicy().hasHeightForWidth())
        self.fieldH7.setSizePolicy(sizePolicy)
        self.fieldH7.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldH7.setObjectName(_fromUtf8("fieldH7"))
        self.grdFieldsLayout.addWidget(self.fieldH7, 1, 7, 1, 1)
        self.fieldC6 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldC6.sizePolicy().hasHeightForWidth())
        self.fieldC6.setSizePolicy(sizePolicy)
        self.fieldC6.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldC6.setObjectName(_fromUtf8("fieldC6"))
        self.grdFieldsLayout.addWidget(self.fieldC6, 2, 2, 1, 1)
        self.fieldE6 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldE6.sizePolicy().hasHeightForWidth())
        self.fieldE6.setSizePolicy(sizePolicy)
        self.fieldE6.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldE6.setObjectName(_fromUtf8("fieldE6"))
        self.grdFieldsLayout.addWidget(self.fieldE6, 2, 4, 1, 1)
        self.fieldG6 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldG6.sizePolicy().hasHeightForWidth())
        self.fieldG6.setSizePolicy(sizePolicy)
        self.fieldG6.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldG6.setObjectName(_fromUtf8("fieldG6"))
        self.grdFieldsLayout.addWidget(self.fieldG6, 2, 6, 1, 1)
        self.fieldB6 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldB6.sizePolicy().hasHeightForWidth())
        self.fieldB6.setSizePolicy(sizePolicy)
        self.fieldB6.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldB6.setObjectName(_fromUtf8("fieldB6"))
        self.grdFieldsLayout.addWidget(self.fieldB6, 2, 1, 1, 1)
        self.fieldC5 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldC5.sizePolicy().hasHeightForWidth())
        self.fieldC5.setSizePolicy(sizePolicy)
        self.fieldC5.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldC5.setObjectName(_fromUtf8("fieldC5"))
        self.grdFieldsLayout.addWidget(self.fieldC5, 3, 2, 1, 1)
        self.fieldD6 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldD6.sizePolicy().hasHeightForWidth())
        self.fieldD6.setSizePolicy(sizePolicy)
        self.fieldD6.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldD6.setObjectName(_fromUtf8("fieldD6"))
        self.grdFieldsLayout.addWidget(self.fieldD6, 2, 3, 1, 1)
        self.fieldF6 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldF6.sizePolicy().hasHeightForWidth())
        self.fieldF6.setSizePolicy(sizePolicy)
        self.fieldF6.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldF6.setObjectName(_fromUtf8("fieldF6"))
        self.grdFieldsLayout.addWidget(self.fieldF6, 2, 5, 1, 1)
        self.fieldG7 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldG7.sizePolicy().hasHeightForWidth())
        self.fieldG7.setSizePolicy(sizePolicy)
        self.fieldG7.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldG7.setObjectName(_fromUtf8("fieldG7"))
        self.grdFieldsLayout.addWidget(self.fieldG7, 1, 6, 1, 1)
        self.fieldE5 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldE5.sizePolicy().hasHeightForWidth())
        self.fieldE5.setSizePolicy(sizePolicy)
        self.fieldE5.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldE5.setObjectName(_fromUtf8("fieldE5"))
        self.grdFieldsLayout.addWidget(self.fieldE5, 3, 4, 1, 1)
        self.fieldH6 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldH6.sizePolicy().hasHeightForWidth())
        self.fieldH6.setSizePolicy(sizePolicy)
        self.fieldH6.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldH6.setObjectName(_fromUtf8("fieldH6"))
        self.grdFieldsLayout.addWidget(self.fieldH6, 2, 7, 1, 1)
        self.fieldD4 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldD4.sizePolicy().hasHeightForWidth())
        self.fieldD4.setSizePolicy(sizePolicy)
        self.fieldD4.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldD4.setObjectName(_fromUtf8("fieldD4"))
        self.grdFieldsLayout.addWidget(self.fieldD4, 4, 3, 1, 1)
        self.fieldC4 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldC4.sizePolicy().hasHeightForWidth())
        self.fieldC4.setSizePolicy(sizePolicy)
        self.fieldC4.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldC4.setObjectName(_fromUtf8("fieldC4"))
        self.grdFieldsLayout.addWidget(self.fieldC4, 4, 2, 1, 1)
        self.fieldB4 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldB4.sizePolicy().hasHeightForWidth())
        self.fieldB4.setSizePolicy(sizePolicy)
        self.fieldB4.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldB4.setObjectName(_fromUtf8("fieldB4"))
        self.grdFieldsLayout.addWidget(self.fieldB4, 4, 1, 1, 1)
        self.fieldA4 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldA4.sizePolicy().hasHeightForWidth())
        self.fieldA4.setSizePolicy(sizePolicy)
        self.fieldA4.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldA4.setObjectName(_fromUtf8("fieldA4"))
        self.grdFieldsLayout.addWidget(self.fieldA4, 4, 0, 1, 1)
        self.fieldH5 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldH5.sizePolicy().hasHeightForWidth())
        self.fieldH5.setSizePolicy(sizePolicy)
        self.fieldH5.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldH5.setObjectName(_fromUtf8("fieldH5"))
        self.grdFieldsLayout.addWidget(self.fieldH5, 3, 7, 1, 1)
        self.fieldG5 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldG5.sizePolicy().hasHeightForWidth())
        self.fieldG5.setSizePolicy(sizePolicy)
        self.fieldG5.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldG5.setObjectName(_fromUtf8("fieldG5"))
        self.grdFieldsLayout.addWidget(self.fieldG5, 3, 6, 1, 1)
        self.fieldB2 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldB2.sizePolicy().hasHeightForWidth())
        self.fieldB2.setSizePolicy(sizePolicy)
        self.fieldB2.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldB2.setObjectName(_fromUtf8("fieldB2"))
        self.grdFieldsLayout.addWidget(self.fieldB2, 6, 1, 1, 1)
        self.fieldH3 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldH3.sizePolicy().hasHeightForWidth())
        self.fieldH3.setSizePolicy(sizePolicy)
        self.fieldH3.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldH3.setObjectName(_fromUtf8("fieldH3"))
        self.grdFieldsLayout.addWidget(self.fieldH3, 5, 7, 1, 1)
        self.fieldA2 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldA2.sizePolicy().hasHeightForWidth())
        self.fieldA2.setSizePolicy(sizePolicy)
        self.fieldA2.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldA2.setObjectName(_fromUtf8("fieldA2"))
        self.grdFieldsLayout.addWidget(self.fieldA2, 6, 0, 1, 1)
        self.fieldE3 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldE3.sizePolicy().hasHeightForWidth())
        self.fieldE3.setSizePolicy(sizePolicy)
        self.fieldE3.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldE3.setObjectName(_fromUtf8("fieldE3"))
        self.grdFieldsLayout.addWidget(self.fieldE3, 5, 4, 1, 1)
        self.fieldF3 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldF3.sizePolicy().hasHeightForWidth())
        self.fieldF3.setSizePolicy(sizePolicy)
        self.fieldF3.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldF3.setObjectName(_fromUtf8("fieldF3"))
        self.grdFieldsLayout.addWidget(self.fieldF3, 5, 5, 1, 1)
        self.fieldG3 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldG3.sizePolicy().hasHeightForWidth())
        self.fieldG3.setSizePolicy(sizePolicy)
        self.fieldG3.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldG3.setObjectName(_fromUtf8("fieldG3"))
        self.grdFieldsLayout.addWidget(self.fieldG3, 5, 6, 1, 1)
        self.fieldD3 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldD3.sizePolicy().hasHeightForWidth())
        self.fieldD3.setSizePolicy(sizePolicy)
        self.fieldD3.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldD3.setObjectName(_fromUtf8("fieldD3"))
        self.grdFieldsLayout.addWidget(self.fieldD3, 5, 3, 1, 1)
        self.fieldH4 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldH4.sizePolicy().hasHeightForWidth())
        self.fieldH4.setSizePolicy(sizePolicy)
        self.fieldH4.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldH4.setObjectName(_fromUtf8("fieldH4"))
        self.grdFieldsLayout.addWidget(self.fieldH4, 4, 7, 1, 1)
        self.fieldE4 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldE4.sizePolicy().hasHeightForWidth())
        self.fieldE4.setSizePolicy(sizePolicy)
        self.fieldE4.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldE4.setObjectName(_fromUtf8("fieldE4"))
        self.grdFieldsLayout.addWidget(self.fieldE4, 4, 4, 1, 1)
        self.fieldC3 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldC3.sizePolicy().hasHeightForWidth())
        self.fieldC3.setSizePolicy(sizePolicy)
        self.fieldC3.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldC3.setObjectName(_fromUtf8("fieldC3"))
        self.grdFieldsLayout.addWidget(self.fieldC3, 5, 2, 1, 1)
        self.fieldF4 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldF4.sizePolicy().hasHeightForWidth())
        self.fieldF4.setSizePolicy(sizePolicy)
        self.fieldF4.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldF4.setObjectName(_fromUtf8("fieldF4"))
        self.grdFieldsLayout.addWidget(self.fieldF4, 4, 5, 1, 1)
        self.fieldB3 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldB3.sizePolicy().hasHeightForWidth())
        self.fieldB3.setSizePolicy(sizePolicy)
        self.fieldB3.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldB3.setObjectName(_fromUtf8("fieldB3"))
        self.grdFieldsLayout.addWidget(self.fieldB3, 5, 1, 1, 1)
        self.fieldG4 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldG4.sizePolicy().hasHeightForWidth())
        self.fieldG4.setSizePolicy(sizePolicy)
        self.fieldG4.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldG4.setObjectName(_fromUtf8("fieldG4"))
        self.grdFieldsLayout.addWidget(self.fieldG4, 4, 6, 1, 1)
        self.fieldA3 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldA3.sizePolicy().hasHeightForWidth())
        self.fieldA3.setSizePolicy(sizePolicy)
        self.fieldA3.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldA3.setObjectName(_fromUtf8("fieldA3"))
        self.grdFieldsLayout.addWidget(self.fieldA3, 5, 0, 1, 1)
        self.fieldF7 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldF7.sizePolicy().hasHeightForWidth())
        self.fieldF7.setSizePolicy(sizePolicy)
        self.fieldF7.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldF7.setObjectName(_fromUtf8("fieldF7"))
        self.grdFieldsLayout.addWidget(self.fieldF7, 1, 5, 1, 1)
        self.fieldB8 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldB8.sizePolicy().hasHeightForWidth())
        self.fieldB8.setSizePolicy(sizePolicy)
        self.fieldB8.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldB8.setObjectName(_fromUtf8("fieldB8"))
        self.grdFieldsLayout.addWidget(self.fieldB8, 0, 1, 1, 1)
        self.fieldF8 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldF8.sizePolicy().hasHeightForWidth())
        self.fieldF8.setSizePolicy(sizePolicy)
        self.fieldF8.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldF8.setObjectName(_fromUtf8("fieldF8"))
        self.grdFieldsLayout.addWidget(self.fieldF8, 0, 5, 1, 1)
        self.fieldA8 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldA8.sizePolicy().hasHeightForWidth())
        self.fieldA8.setSizePolicy(sizePolicy)
        self.fieldA8.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldA8.setObjectName(_fromUtf8("fieldA8"))
        self.grdFieldsLayout.addWidget(self.fieldA8, 0, 0, 1, 1)
        self.fieldE7 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldE7.sizePolicy().hasHeightForWidth())
        self.fieldE7.setSizePolicy(sizePolicy)
        self.fieldE7.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldE7.setObjectName(_fromUtf8("fieldE7"))
        self.grdFieldsLayout.addWidget(self.fieldE7, 1, 4, 1, 1)
        self.fieldC7 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldC7.sizePolicy().hasHeightForWidth())
        self.fieldC7.setSizePolicy(sizePolicy)
        self.fieldC7.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldC7.setObjectName(_fromUtf8("fieldC7"))
        self.grdFieldsLayout.addWidget(self.fieldC7, 1, 2, 1, 1)
        self.fieldC8 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldC8.sizePolicy().hasHeightForWidth())
        self.fieldC8.setSizePolicy(sizePolicy)
        self.fieldC8.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldC8.setObjectName(_fromUtf8("fieldC8"))
        self.grdFieldsLayout.addWidget(self.fieldC8, 0, 2, 1, 1)
        self.fieldA7 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldA7.sizePolicy().hasHeightForWidth())
        self.fieldA7.setSizePolicy(sizePolicy)
        self.fieldA7.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldA7.setObjectName(_fromUtf8("fieldA7"))
        self.grdFieldsLayout.addWidget(self.fieldA7, 1, 0, 1, 1)
        self.fieldD7 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldD7.sizePolicy().hasHeightForWidth())
        self.fieldD7.setSizePolicy(sizePolicy)
        self.fieldD7.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldD7.setObjectName(_fromUtf8("fieldD7"))
        self.grdFieldsLayout.addWidget(self.fieldD7, 1, 3, 1, 1)
        self.fieldB7 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldB7.sizePolicy().hasHeightForWidth())
        self.fieldB7.setSizePolicy(sizePolicy)
        self.fieldB7.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldB7.setObjectName(_fromUtf8("fieldB7"))
        self.grdFieldsLayout.addWidget(self.fieldB7, 1, 1, 1, 1)
        self.fieldH8 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldH8.sizePolicy().hasHeightForWidth())
        self.fieldH8.setSizePolicy(sizePolicy)
        self.fieldH8.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldH8.setObjectName(_fromUtf8("fieldH8"))
        self.grdFieldsLayout.addWidget(self.fieldH8, 0, 7, 1, 1)
        self.fieldG8 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldG8.sizePolicy().hasHeightForWidth())
        self.fieldG8.setSizePolicy(sizePolicy)
        self.fieldG8.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldG8.setObjectName(_fromUtf8("fieldG8"))
        self.grdFieldsLayout.addWidget(self.fieldG8, 0, 6, 1, 1)
        self.fieldE8 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldE8.sizePolicy().hasHeightForWidth())
        self.fieldE8.setSizePolicy(sizePolicy)
        self.fieldE8.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldE8.setObjectName(_fromUtf8("fieldE8"))
        self.grdFieldsLayout.addWidget(self.fieldE8, 0, 4, 1, 1)
        self.fieldD8 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldD8.sizePolicy().hasHeightForWidth())
        self.fieldD8.setSizePolicy(sizePolicy)
        self.fieldD8.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldD8.setObjectName(_fromUtf8("fieldD8"))
        self.grdFieldsLayout.addWidget(self.fieldD8, 0, 3, 1, 1)
        self.fieldF2 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldF2.sizePolicy().hasHeightForWidth())
        self.fieldF2.setSizePolicy(sizePolicy)
        self.fieldF2.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldF2.setObjectName(_fromUtf8("fieldF2"))
        self.grdFieldsLayout.addWidget(self.fieldF2, 6, 5, 1, 1)
        self.fieldE2 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldE2.sizePolicy().hasHeightForWidth())
        self.fieldE2.setSizePolicy(sizePolicy)
        self.fieldE2.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldE2.setObjectName(_fromUtf8("fieldE2"))
        self.grdFieldsLayout.addWidget(self.fieldE2, 6, 4, 1, 1)
        self.fieldD1 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldD1.sizePolicy().hasHeightForWidth())
        self.fieldD1.setSizePolicy(sizePolicy)
        self.fieldD1.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldD1.setObjectName(_fromUtf8("fieldD1"))
        self.grdFieldsLayout.addWidget(self.fieldD1, 7, 3, 1, 1)
        self.fieldH2 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldH2.sizePolicy().hasHeightForWidth())
        self.fieldH2.setSizePolicy(sizePolicy)
        self.fieldH2.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldH2.setObjectName(_fromUtf8("fieldH2"))
        self.grdFieldsLayout.addWidget(self.fieldH2, 6, 7, 1, 1)
        self.fieldB1 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldB1.sizePolicy().hasHeightForWidth())
        self.fieldB1.setSizePolicy(sizePolicy)
        self.fieldB1.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldB1.setObjectName(_fromUtf8("fieldB1"))
        self.grdFieldsLayout.addWidget(self.fieldB1, 7, 1, 1, 1)
        self.fieldG2 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldG2.sizePolicy().hasHeightForWidth())
        self.fieldG2.setSizePolicy(sizePolicy)
        self.fieldG2.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldG2.setObjectName(_fromUtf8("fieldG2"))
        self.grdFieldsLayout.addWidget(self.fieldG2, 6, 6, 1, 1)
        self.fieldD2 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldD2.sizePolicy().hasHeightForWidth())
        self.fieldD2.setSizePolicy(sizePolicy)
        self.fieldD2.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldD2.setObjectName(_fromUtf8("fieldD2"))
        self.grdFieldsLayout.addWidget(self.fieldD2, 6, 3, 1, 1)
        self.fieldE1 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldE1.sizePolicy().hasHeightForWidth())
        self.fieldE1.setSizePolicy(sizePolicy)
        self.fieldE1.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldE1.setObjectName(_fromUtf8("fieldE1"))
        self.grdFieldsLayout.addWidget(self.fieldE1, 7, 4, 1, 1)
        self.fieldC1 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldC1.sizePolicy().hasHeightForWidth())
        self.fieldC1.setSizePolicy(sizePolicy)
        self.fieldC1.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldC1.setObjectName(_fromUtf8("fieldC1"))
        self.grdFieldsLayout.addWidget(self.fieldC1, 7, 2, 1, 1)
        self.fieldC2 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldC2.sizePolicy().hasHeightForWidth())
        self.fieldC2.setSizePolicy(sizePolicy)
        self.fieldC2.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldC2.setObjectName(_fromUtf8("fieldC2"))
        self.grdFieldsLayout.addWidget(self.fieldC2, 6, 2, 1, 1)
        self.fieldA1 = QtGui.QWidget(self.grdFields)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldA1.sizePolicy().hasHeightForWidth())
        self.fieldA1.setSizePolicy(sizePolicy)
        self.fieldA1.setMinimumSize(QtCore.QSize(30, 30))
        self.fieldA1.setObjectName(_fromUtf8("fieldA1"))
        self.grdFieldsLayout.addWidget(self.fieldA1, 7, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.grdFields)
        self.frmMyPark = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmMyPark.sizePolicy().hasHeightForWidth())
        self.frmMyPark.setSizePolicy(sizePolicy)
        self.frmMyPark.setMinimumSize(QtCore.QSize(0, 32))
        self.frmMyPark.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmMyPark.setFrameShadow(QtGui.QFrame.Raised)
        self.frmMyPark.setObjectName(_fromUtf8("frmMyPark"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frmMyPark)
        self.horizontalLayout_3.setContentsMargins(1, 0, 1, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pebleMyDark = QtGui.QFrame(self.frmMyPark)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pebleMyDark.sizePolicy().hasHeightForWidth())
        self.pebleMyDark.setSizePolicy(sizePolicy)
        self.pebleMyDark.setMinimumSize(QtCore.QSize(15, 0))
        self.pebleMyDark.setMaximumSize(QtCore.QSize(15, 16777215))
        self.pebleMyDark.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pebleMyDark.setFrameShadow(QtGui.QFrame.Raised)
        self.pebleMyDark.setObjectName(_fromUtf8("pebleMyDark"))
        self.horizontalLayout_3.addWidget(self.pebleMyDark)
        self.pebleMyLight = QtGui.QFrame(self.frmMyPark)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pebleMyLight.sizePolicy().hasHeightForWidth())
        self.pebleMyLight.setSizePolicy(sizePolicy)
        self.pebleMyLight.setMinimumSize(QtCore.QSize(15, 0))
        self.pebleMyLight.setMaximumSize(QtCore.QSize(15, 16777215))
        self.pebleMyLight.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pebleMyLight.setFrameShadow(QtGui.QFrame.Raised)
        self.pebleMyLight.setObjectName(_fromUtf8("pebleMyLight"))
        self.horizontalLayout_3.addWidget(self.pebleMyLight)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.frmMyPark)
        self.layMain.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frmIndicatorYOU = QtGui.QFrame(Form)
        self.frmIndicatorYOU.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmIndicatorYOU.setFrameShadow(QtGui.QFrame.Raised)
        self.frmIndicatorYOU.setObjectName(_fromUtf8("frmIndicatorYOU"))
        self.verticalLayout_2.addWidget(self.frmIndicatorYOU)
        self.frmIndicatorME = QtGui.QFrame(Form)
        self.frmIndicatorME.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmIndicatorME.setFrameShadow(QtGui.QFrame.Raised)
        self.frmIndicatorME.setObjectName(_fromUtf8("frmIndicatorME"))
        self.verticalLayout_2.addWidget(self.frmIndicatorME)
        self.verticalSlider = QtGui.QSlider(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy)
        self.verticalSlider.setMaximum(1)
        self.verticalSlider.setPageStep(1)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.verticalLayout_2.addWidget(self.verticalSlider)
        self.layMain.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.layMain)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "pyChezzMin", None))
        self.btnOpen.setText(_translate("Form", "Load", None))
        self.btnSave.setText(_translate("Form", "Save", None))
        self.frmOpponentPark.setProperty("class", _translate("Form", "parking", None))
        self.pebleOppDark.setProperty("class", _translate("Form", "darkBG", None))
        self.pebleOppLight.setProperty("class", _translate("Form", "lightBG", None))
        self.fieldG1.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldF1.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldH1.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldD5.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldF5.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldA6.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldA5.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldB5.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldH7.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldC6.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldE6.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldG6.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldB6.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldC5.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldD6.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldF6.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldG7.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldE5.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldH6.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldD4.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldC4.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldB4.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldA4.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldH5.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldG5.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldB2.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldH3.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldA2.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldE3.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldF3.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldG3.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldD3.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldH4.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldE4.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldC3.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldF4.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldB3.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldG4.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldA3.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldF7.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldB8.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldF8.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldA8.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldE7.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldC7.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldC8.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldA7.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldD7.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldB7.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldH8.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldG8.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldE8.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldD8.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldF2.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldE2.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldD1.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldH2.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldB1.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldG2.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldD2.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldE1.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldC1.setProperty("class", _translate("Form", "blackBG", None))
        self.fieldC2.setProperty("class", _translate("Form", "whiteBG", None))
        self.fieldA1.setProperty("class", _translate("Form", "blackBG", None))
        self.frmMyPark.setProperty("class", _translate("Form", "parking", None))
        self.pebleMyDark.setProperty("class", _translate("Form", "darkBG", None))
        self.pebleMyLight.setProperty("class", _translate("Form", "lightBG", None))
        self.frmIndicatorYOU.setProperty("class", _translate("Form", "permissionNO", None))
        self.frmIndicatorME.setProperty("class", _translate("Form", "permissionYES", None))

