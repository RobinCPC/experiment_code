#!/usr/bin/env python

"""
Embedded an IPythonConsole to interact with python-OCC
"""
from __future__ import print_function
from OCC.Display.backend import load_backend
load_backend('qt-pyside')
from OCC.Display.qtDisplay import qtViewer3d
from OCC import Quantity, Aspect

from inter_console import QIPythonWidget
try:
    from PySide import QtGui, QtCore
except ImportError:
    try:
        from PyQt5 import QtCore, QtWidgets, QtGui
    except ImportError:
        print("Need to install PySide or PyQt5!\n")


class InteractOCC(QtGui.QMainWindow):
    def __init__(self):
        super(InteractOCC, self).__init__()
        self.canvas = qtViewer3d()
        self.setCentralWidget(self.canvas)

        # add Ipython console as dockwidget
        consoleDock = QtGui.QDockWidget("console", self)
        consoleDock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea |
                                    QtCore.Qt.RightDockWidgetArea)
        self.console = QIPythonWidget(customBanner="Welcome to play python-occ!\n",)
        consoleDock.setWidget(self.console)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, consoleDock)

        # push occ display into variable of Ipython console
        self.console.pushVariables({"canvas": self.canvas})


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    interOCC = InteractOCC()
    interOCC.showMaximized()
    interOCC.canvas.InitDriver()
    interOCC.canvas._display.View.SetBgGradientColors(Quantity.Quantity_NOC_NAVYBLUE,
                                                    Quantity.Quantity_NOC_GRAY,
                                                    Aspect.Aspect_GFM_VER)
    interOCC.canvas._display.View_Iso()
    interOCC.console.pushVariables({"display":interOCC.canvas._display})
    app.exec_()
