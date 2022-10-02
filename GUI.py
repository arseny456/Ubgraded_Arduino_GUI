from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

app = QtWidgets.QApplication([])
ui = uic.loadUi("design.ui")
ui.setWindowTitle("SerialGUI")

serial = QSerialPort()
serial.setBaudRate(115200)
portlist = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    portlist.append(port.portName())
ui.comboBox.addItems(portlist)


def onOpen():
    serial.setPortName(ui.comboBox.currentText())
    serial.open(QIODevice.ReadWrite)
    print("sdfshf")


def onClose():
    serial.close()


def onRead():
    rx = serial.readLine()
    print(rx)


# def slider_r():
def R_btn_On():
    serial.write(b"ON\n")
    print('on')

def R_btn_off():
    serial.write(b"OFF\n")
    print('off')

ui.red_btn.clicked.connect(R_btn_On)
serial.readyRead.connect(onRead)
ui.Open_btn.clicked.connect(onOpen)
ui.Close_btn.clicked.connect(onClose)

ui.show()
app.exec()
