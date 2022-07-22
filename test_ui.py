# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import xlrd
import re
from ctypes import *
from time import sleep
# Import module
import ControlSPI
import time
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(270, 80, 256, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(270, 140, 256, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(270, 200, 256, 41))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(270, 260, 256, 41))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(270, 320, 256, 41))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(270, 380, 256, 41))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(270, 440, 256, 41))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(270, 500, 256, 41))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 30, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 180, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 270, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 80, 161, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(600, 80, 121, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(600, 140, 121, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(600, 200, 121, 41))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(600, 260, 121, 41))
        self.textEdit_5.setObjectName("textEdit_5")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(10, 500, 141, 41))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(40, 370, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setObjectName("toolButton_2")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(600, 320, 121, 41))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(600, 380, 121, 41))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(600, 440, 121, 41))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(600, 500, 121, 41))
        self.textEdit_9.setObjectName("textEdit_9")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(770, 30, 256, 501))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 30, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1077, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "addr"))
        self.label_2.setText(_translate("MainWindow", "field-attr-value"))
        self.pushButton.setText(_translate("MainWindow", "READ"))
        self.pushButton_2.setText(_translate("MainWindow", "WRITE"))
        self.toolButton.setText(_translate("MainWindow", "reg_map read"))
        self.toolButton_2.setText(_translate("MainWindow", "TEST sequence"))
        self.label_3.setText(_translate("MainWindow", "write_value"))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.read_addr)
        self.ui.pushButton_2.clicked.connect(self.write_addr)
        self.ui.toolButton_2.clicked.connect(self.load_test_seq)
        self.ui.toolButton.clicked.connect(self.load_reg_map)
        self.single_reg = {}
    def read_addr(self):
        self.ui.textBrowser.clear()
        self.ui.textBrowser_2.clear()
        self.ui.textBrowser_3.clear()
        self.ui.textBrowser_4.clear()
        self.ui.textBrowser_5.clear()
        self.ui.textBrowser_6.clear()
        self.ui.textBrowser_7.clear()
        self.ui.textBrowser_8.clear()
        now_addr = self.ui.textEdit.toPlainText()
        read_value = self.read_atom(int(now_addr, 16))
        self.ui.textBrowser_9.insertPlainText('read addr '+now_addr+' value '+hex(int(str(read_value[0])))+'\n')
        if now_addr in self.single_reg.keys():
            for i in range(0,len(self.single_reg[now_addr])):
                if i == 0:
                    self.ui.textBrowser.insertPlainText(self.single_reg[now_addr][0])
                elif i == 1:
                    self.ui.textBrowser_2.insertPlainText(self.single_reg[now_addr][1])
                elif i == 2:
                    self.ui.textBrowser_3.insertPlainText(self.single_reg[now_addr][2])
                elif i == 3:
                    self.ui.textBrowser_4.insertPlainText(self.single_reg[now_addr][3])
                elif i == 4:
                    self.ui.textBrowser_5.insertPlainText(self.single_reg[now_addr][4])
                elif i == 5:
                    self.ui.textBrowser_6.insertPlainText(self.single_reg[now_addr][5])
                elif i == 6:
                    self.ui.textBrowser_7.insertPlainText(self.single_reg[now_addr][6])
                elif i == 7:
                    self.ui.textBrowser_8.insertPlainText(self.single_reg[now_addr][7])
        else:
            self.ui.textBrowser_9.insertPlainText('reg map has no addr '+now_addr+' please load reg map first or check input addr!!\n')
    def write_addr(self):
        now_addr = self.ui.textEdit.toPlainText()
        if now_addr in self.single_reg.keys():
            write_value = []
            write_bit = []
            for i in range(0,len(self.single_reg[now_addr])):
                temp_str = self.single_reg[now_addr][i].split(',')
                write_bit.append(temp_str[2][2])
                if i == 0:
                    write_value.append(self.ui.textEdit_2.toPlainText())
                elif i == 1:
                    write_value.append(self.ui.textEdit_3.toPlainText())
                elif i == 2:
                    write_value.append(self.ui.textEdit_4.toPlainText())
                elif i == 3:
                    write_value.append(self.ui.textEdit_5.toPlainText())
                elif i == 4:
                    write_value.append(self.ui.textEdit_6.toPlainText())
                elif i == 5:
                    write_value.append(self.ui.textEdit_7.toPlainText())
                elif i == 6:
                    write_value.append(self.ui.textEdit_8.toPlainText())
                elif i == 7:
                    write_value.append(self.ui.textEdit_9.toPlainText())
            value = 0
            for x in range(0,len(write_value)):
                if re.match('^0x(\w+)',write_value[x]):
                    value = value + int(write_value[x],16)*2**(int(write_bit[x]))
                else:
                    value = value + int(write_value[x])*2**(int(write_bit[x]))
            self.ui.textBrowser_9.insertPlainText('write addr '+now_addr+' '+hex(value)+'\n')
            self.write_atom(int(now_addr,16), value)
        else:
            self.ui.textBrowser_9.insertPlainText('reg map has no addr '+now_addr+' please load reg map first or check input addr!!\n')
    def load_test_seq(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            self.test_seq_file = dialog.selectedFiles()
            self.ui.textBrowser_9.insertPlainText('test seq file is '+str(self.test_seq_file[0])+'\n...\n...\n')
        self.ui.textBrowser_9.insertPlainText('starting reading '+str(self.test_seq_file[0])+'\n')
        print ('1111111111111111111')
        self.parser_seq_file(self.test_seq_file[0])
    def parser_seq_file(self, fn):
        data = xlrd.open_workbook(fn)
        sheet_data = data.sheets()[0]
        rows_num = sheet_data.nrows
        seq_addr = []
        seq_data = []
        for x in range(1,rows_num):
            seq_addr.append(sheet_data.cell_value(x,0))
            seq_data.append(sheet_data.cell_value(x,1))
        for i in range(0,len(seq_addr)):
            print (seq_addr[i])
            print (seq_data[i])
            self.write_atom(int(seq_addr[i],16), int(seq_data[i],16))
    def write_atom(self,addr,data):
        write_buffer = (c_ubyte * 3)()
        read_buffer = (c_ubyte * 1)()
        addr_str = '{:0>4x}'.format(addr)
        write_buffer[0] = int(addr_str[0:2],16)
        write_buffer[1] = int(addr_str[2:],16)
        write_buffer[2] = data
        nRet = ControlSPI.VSI_WriteBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 3)
    def read_atom(self,addr):
        write_buffer = (c_ubyte * 2)()
        read_buffer = (c_ubyte * 1)()
        addr_str = '{:0>4x}'.format(addr)
        write_buffer[0] = int(addr_str[0:2], 16)+128
        write_buffer[1] = int(addr_str[2:], 16)
        nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 1)
        return read_buffer
    def load_reg_map(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            self.reg_map = dialog.selectedFiles()
            self.ui.textBrowser_9.insertPlainText('reg map file is '+str(self.reg_map[0])+'\n...\n...\n')
        self.ui.textBrowser_9.insertPlainText('starting reading '+str(self.reg_map[0])+'\n')
        self.parser_reg_map(self.reg_map[0])
    def parser_reg_map(self, fn):
        data = xlrd.open_workbook(fn)
        sheet_data = data.sheets()[3]
        rows_num = sheet_data.nrows
        for x in range(1,rows_num):
            if sheet_data.cell_value(x,2) == '' and sheet_data.cell_value(x,6) != '':
                self.single_reg[addr_str].append(sheet_data.cell_value(x,6)+','+sheet_data.cell_value(x,8)+','+sheet_data.cell_value(x,7)+','+sheet_data.cell_value(x,9))
            elif sheet_data.cell_value(x,2) != '' and sheet_data.cell_value(x,0) != '':
                addr_str = sheet_data.cell_value(x,2)
                self.single_reg.setdefault(addr_str, []).append(sheet_data.cell_value(x,6)+','+sheet_data.cell_value(x,8)+','+sheet_data.cell_value(x,7)+','+sheet_data.cell_value(x,9))
    # def 
        
if __name__ == "__main__":
    # Scan device
    nRet = ControlSPI.VSI_ScanDevice(1)
    if (nRet <= 0):
        print("No device connect!")
    #  exit()
    else:
        print("Connected device number is:" + repr(nRet))

    # Open device
    nRet = ControlSPI.VSI_OpenDevice(ControlSPI.VSI_USBSPI, 0, 0)
    if (nRet != ControlSPI.ERR_SUCCESS):
        print("Open device error!")
        # exit()
    else:
        print("Open device success!")
    # Initialize device
    SPI_Init = ControlSPI.VSI_INIT_CONFIG()
    SPI_Init.ClockSpeed = 1125000;
    SPI_Init.ControlMode = 3;
    SPI_Init.CPHA = 0;
    SPI_Init.CPOL = 0;
    SPI_Init.LSBFirst = 0;
    SPI_Init.MasterMode = 1;
    SPI_Init.SelPolarity = 0;
    SPI_Init.TranBits = 8;

    nRet = ControlSPI.VSI_InitSPI(ControlSPI.VSI_USBSPI, 0, byref(SPI_Init))
    if (nRet != ControlSPI.ERR_SUCCESS):
        print("Initialization device error!")
    # exit()
    else:
        print("Initialization device success!")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
