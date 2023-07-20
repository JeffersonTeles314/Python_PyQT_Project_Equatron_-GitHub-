from PyQt6 import QtCore, QtGui, QtWidgets
from random import *
from math import isclose

class Ui_Form(object):
    def setupUi(self, Form):
        
        #Criando a Janela
        Form.setObjectName("Form")
        Form.resize(480, 360)
        Form.setMinimumSize(QtCore.QSize(480, 360))
        Form.setMaximumSize(QtCore.QSize(480, 360))
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 10, 481, 81))

        #Criando as Fontes
            #Fonte fontFB_18_B
        fontFB_18_B = QtGui.QFont()
        fontFB_18_B.setFamily("Agency FB")
        fontFB_18_B.setPointSize(18)
        fontFB_18_B.setBold(True)
            #Fonte fontFB_12_B
        fontFB_12_B = QtGui.QFont()
        fontFB_12_B.setFamily("Agency FB")
        fontFB_12_B.setPointSize(12)
        fontFB_12_B.setBold(True)
            #Fonte fontFB_24
        fontFB_24 = QtGui.QFont()
        fontFB_24.setFamily("Agency FB")
        fontFB_24.setPointSize(24)
            #Fonte font_header
        font_header = QtGui.QFont()
        font_header.setFamily("Agency FB")
        font_header.setPointSize(48)
        font_header.setBold(True)
            #Fonte font_FB_14
        fontFB_14 = QtGui.QFont()
        fontFB_14.setFamily("Agency FB")
        fontFB_14.setPointSize(14)
            #Fonte fontFB_16
        fontFB_16 = QtGui.QFont()
        fontFB_16.setFamily("Agency FB")
        fontFB_16.setPointSize(16)

        self.label.setFont(font_header)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(310, 110, 161, 161))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.label_3.setFont(fontFB_18_B)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")


        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 141, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox, clicked = lambda:self.send_answer())
        self.pushButton.setGeometry(QtCore.QRect(10, 100, 141, 24))
        self.pushButton.setFont(fontFB_12_B)
        self.pushButton.setObjectName("pushButton")

        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 291, 161))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 281, 41))
        self.label_2.setFont(fontFB_24)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 281, 41))
        self.label_5.setFont(fontFB_24)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 281, 41))
        self.label_6.setFont(fontFB_24)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.groupBox_3 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 269, 461, 81))
        self.groupBox_3.setFont(fontFB_16)
        self.groupBox_3.setObjectName("groupBox_3")

        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 441, 51))
        self.label_7.setFont(fontFB_14)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        self.setequation()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Equatron V.1.2"))
        self.label_3.setText(_translate("Form", "Resultado:"))
        self.pushButton.setText(_translate("Form", "Enviar"))
        self.label_2.setText(_translate("Form", "X * A1 + B1"))
        self.label_5.setText(_translate("Form", "X * A2 + B2"))
        self.label_6.setText(_translate("Form", "= "))
        self.groupBox_3.setTitle(_translate("Form", "Como Usar?"))
        self.label_7.setText(_translate("Form", "Simples, basta resolver a equação na parte superior esquerda, e em seguida, colocar o resultado na parte direita e clicar \"Enviar\"."))

    def setequation(self):
        _translate = QtCore.QCoreApplication.translate
        vartest = True
        while vartest == True: 
            self.a1 = randint(-10,10)
            self.a2 = randint(-10,10)
            self.b1 = randint(-10,10)
            self.b2 = randint(-10,10)
            if self.a1 == self.a2:
                vartest = True
            else:
                vartest = False 
        self.resposta = (self.b2-self.b1)/(self.a1-self.a2)
        self.b1sig = ""
        self.b2sig = ""
        if self.b1 < 0:
            self.b1sig = ""
        else:
            self.b1sig = "+"

        if self.b2 < 0:
            self.b2sig = ""
        else:
            self.b2sig = "+"

        self.label_2.setText(_translate("Form", f"{self.a1}X {self.b1sig} {self.b1}"))
        self.label_5.setText(_translate("Form", f"{self.a2}X {self.b2sig} {self.b2}"))

    def send_answer(self):
        var1 = float(self.resposta)
        var0 = self.lineEdit.text()
        if not var0.isalpha():
            var2 = float(self.lineEdit.text())
        else:
            var2 = 0.0
        print(isclose(var1,var2, rel_tol=0.5, abs_tol=0.0))
        print(var1)
        print(var2)

        if isclose(var1,var2, rel_tol=0.5, abs_tol=0.0):
            self.lineEdit.setText("Resposta Certa!")
            self.setequation()
        else:
            self.lineEdit.setText("Resposta Errada!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
