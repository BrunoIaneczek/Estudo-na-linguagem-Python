from PyQt5 import uic, QtWidgets

def funcao_principal():
    print('ola mundo')


app = QtWidgets.QApplication([])
formulario = uic.loadUi('teste.ui')
formulario.pushButton.clicked.connect(funcao_principal())

formulario.show()
app.exec()


