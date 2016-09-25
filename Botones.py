# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Botones.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(480, 319)
        self.Cancelar = QtGui.QPushButton(Dialog)
        self.Cancelar.setGeometry(QtCore.QRect(170, 250, 131, 51))
        self.Cancelar.setObjectName(_fromUtf8("Cancelar"))
        self.Capturar = QtGui.QPushButton(Dialog)
        self.Capturar.setGeometry(QtCore.QRect(30, 80, 201, 151))
        self.Capturar.setObjectName(_fromUtf8("Capturar"))
        self.Detener = QtGui.QPushButton(Dialog)
        self.Detener.setGeometry(QtCore.QRect(250, 80, 211, 151))
        self.Detener.setObjectName(_fromUtf8("Detener"))
        self.Configuraciones = QtGui.QPushButton(Dialog)
        self.Configuraciones.setGeometry(QtCore.QRect(0, 0, 121, 41))
        self.Configuraciones.setObjectName(_fromUtf8("Configuraciones"))
        self.Ayuda = QtGui.QPushButton(Dialog)
        self.Ayuda.setGeometry(QtCore.QRect(120, 0, 121, 41))
        self.Ayuda.setObjectName(_fromUtf8("Ayuda"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.Cancelar.setText(_translate("Dialog", "Cancelar", None))
        self.Capturar.setText(_translate("Dialog", "Capturar/Grabar", None))
        self.Detener.setText(_translate("Dialog", "Detener/Guardar", None))
        self.Configuraciones.setText(_translate("Dialog", "Configuraciones", None))
        self.Ayuda.setText(_translate("Dialog", "Ayuda", None))


###############Main Code################


class Mostrar(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = Mostrar()
	myapp.show()
	sys.exit(app.exec_())

def function():
    print hola