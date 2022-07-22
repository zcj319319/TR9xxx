# -*- coding: utf-8 -*-


import re
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import xlwt
from ctypes import *
import ControlSPI
import time
import threading

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(334, 145)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setGeometry(QRect(30, 30, 280, 25))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QRect(110, 90, 120, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        
class MainDialog(QDialog):
    Signal_parp = pyqtSignal(str)
    def __init__(self, sheet_lst):
        super(MainDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.sheet_lst = sheet_lst
        self.ui.comboBox.addItem('select one sheet')
        for x in sheet_lst:
            self.ui.comboBox.addItem(x)
        self.ui.comboBox.currentIndexChanged.connect(self.select_sheet)
        self.ui.pushButton.clicked.connect(self.ok_and_quit)
    def select_sheet(self):
        self.select_sheet = self.ui.comboBox.currentText()
        self.Signal_parp.emit(self.select_sheet)
    def ok_and_quit(self):
        self.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEditbit7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit7.setGeometry(QtCore.QRect(230, 200, 30, 30))
        self.textEditbit7.setObjectName("textEditbit7")
        self.textEditbit6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit6.setGeometry(QtCore.QRect(280, 200, 30, 30))
        self.textEditbit6.setObjectName("textEditbit6")
        self.textEditbit5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit5.setGeometry(QtCore.QRect(330, 200, 30, 30))
        self.textEditbit5.setObjectName("textEditbit5")
        self.textEditbit4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit4.setGeometry(QtCore.QRect(380, 200, 30, 30))
        self.textEditbit4.setObjectName("textEditbit4")
        self.textEditbit3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit3.setGeometry(QtCore.QRect(430, 200, 30, 30))
        self.textEditbit3.setObjectName("textEditbit3")
        self.textEditbit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit2.setGeometry(QtCore.QRect(480, 200, 30, 30))
        self.textEditbit2.setObjectName("textEditbit2")
        self.textEditbit1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit1.setGeometry(QtCore.QRect(530, 200, 30, 30))
        self.textEditbit1.setObjectName("textEditbit1")
        self.textEditbit0 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit0.setGeometry(QtCore.QRect(580, 200, 30, 30))
        self.textEditbit0.setObjectName("textEditbit0")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 200, 120, 30))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 205, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 150, 120, 30))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(380, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(530, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(480, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(430, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 250, 661, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 90, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(300, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(420, 90, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(300, 90, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 140, 41, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(640, 165, 41, 20))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(640, 190, 41, 21))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(640, 215, 41, 21))
        self.pushButton_11.setObjectName("pushButton_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 23))
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
        self.label.setText(_translate("MainWindow", "data"))
        self.label_2.setText(_translate("MainWindow", "addr"))
        self.label_3.setText(_translate("MainWindow", "bit7"))
        self.label_4.setText(_translate("MainWindow", "bit6"))
        self.label_5.setText(_translate("MainWindow", "bit5"))
        self.label_6.setText(_translate("MainWindow", "bit4"))
        self.label_7.setText(_translate("MainWindow", "bit0"))
        self.label_8.setText(_translate("MainWindow", "bit1"))
        self.label_9.setText(_translate("MainWindow", "bit2"))
        self.label_10.setText(_translate("MainWindow", "bit3"))
        self.pushButton.setText(_translate("MainWindow", "READ"))
        self.pushButton_2.setText(_translate("MainWindow", "WRITE"))
        self.pushButton_4.setText(_translate("MainWindow", "MEM_RD"))
        self.pushButton_5.setText(_translate("MainWindow", "FFT"))
        self.toolButton.setText(_translate("MainWindow", "seq_test"))
        self.pushButton_6.setText(_translate("MainWindow", "WEIGHT_RD"))
        self.pushButton_7.setText(_translate("MainWindow", "204_config"))
        self.pushButton_8.setText(_translate("MainWindow", "cali_config"))
        self.pushButton_3.setText(_translate("MainWindow", "NYQ0"))
        self.pushButton_9.setText(_translate("MainWindow", "NYQ1"))
        self.pushButton_10.setText(_translate("MainWindow", "NYQ2"))
        self.pushButton_11.setText(_translate("MainWindow", "NYQ3"))
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.read_addr)
        self.ui.pushButton_2.clicked.connect(self.write_addr)
        self.ui.toolButton.clicked.connect(self.load_test_seq)
        self.ui.pushButton_4.clicked.connect(self.mem_read)
        self.ui.pushButton_5.clicked.connect(self.fft_gen)
        self.ui.pushButton_6.clicked.connect(self.weight_rd)
        self.ui.pushButton_8.clicked.connect(self.cali_cfg)
        self.ui.pushButton_7.clicked.connect(self.j204_cfg)
        self.ui.pushButton_3.clicked.connect(self.nyq0)
        self.ui.pushButton_9.clicked.connect(self.nyq1)
        self.ui.pushButton_10.clicked.connect(self.nyq2)
        self.ui.pushButton_11.clicked.connect(self.nyq3)
    def write_atom(self,addr,data):
        # self.ui.textBrowser.insertPlainText('write:addr='+hex(addr)+' data='+hex(data)+'\n')
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
        # self.ui.textBrowser.insertPlainText('read:addr='+hex(addr)+' data='+hex(int(str(read_buffer[0])))+'\n')
        return read_buffer
    def read_addr(self):
        now_addr = self.ui.textEdit_2.toPlainText()
        if re.match('^0x', now_addr):
            addr_read = int(now_addr,16)
        else:
            addr_read = int(now_addr)
        read_value = self.read_atom(addr_read)
        self.ui.textEdit.setText(hex(read_value[0]))
        read_value_bin = '{:0>8b}'.format(read_value[0])
        self.ui.textEditbit0.setText(read_value_bin[7])
        self.ui.textEditbit1.setText(read_value_bin[6])
        self.ui.textEditbit2.setText(read_value_bin[5])
        self.ui.textEditbit3.setText(read_value_bin[4])
        self.ui.textEditbit4.setText(read_value_bin[3])
        self.ui.textEditbit5.setText(read_value_bin[2])
        self.ui.textEditbit6.setText(read_value_bin[1])
        self.ui.textEditbit7.setText(read_value_bin[0])
        self.ui.textBrowser.insertPlainText('read:addr=' + hex(addr_read) + ' data=' + hex(read_value[0]) + '\n')
    def write_addr(self):
        now_addr = self.ui.textEdit_2.toPlainText()
        if re.match('^0x', now_addr):
            addr_write = int(now_addr,16)
        else:
            addr_write = int(now_addr)
        now_value = self.ui.textEdit.toPlainText()
        if re.match('^0x',now_value):
            write_value = int(now_value,16)
        else:
            write_value = int(now_value)
        write_value_bin = '{:0>8b}'.format(write_value)
        self.ui.textEditbit0.setText(write_value_bin[7])
        self.ui.textEditbit1.setText(write_value_bin[6])
        self.ui.textEditbit2.setText(write_value_bin[5])
        self.ui.textEditbit3.setText(write_value_bin[4])
        self.ui.textEditbit4.setText(write_value_bin[3])
        self.ui.textEditbit5.setText(write_value_bin[2])
        self.ui.textEditbit6.setText(write_value_bin[1])
        self.ui.textEditbit7.setText(write_value_bin[0])
        self.ui.textBrowser.insertPlainText('write:addr=' + hex(addr_write) + ' data=' + hex(write_value) + '\n')
        self.write_atom(addr_write, write_value)
    def load_test_seq(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            self.test_seq_file = dialog.selectedFiles()
            self.ui.textBrowser.insertPlainText('test seq file is '+str(self.test_seq_file[0])+'\n...\n...\n')
        # self.ui.textBrowser.insertPlainText('starting reading '+str(self.test_seq_file[0])+'\n')
        self.parser_seq_file(self.test_seq_file[0])
    def parser_seq_file(self, fn):
        data = xlrd.open_workbook(fn)
        sheetsall = data.sheet_names()
        dialog = MainDialog(sheetsall)
        dialog.Signal_parp.connect(self.deal_emit_sheet)
        dialog.show()
        dialog.exec_()
        sheet_idx = sheetsall.index(self.sheet_sel_lst)
        self.ui.textBrowser.insertPlainText(time.ctime()+': seq '+sheetsall[sheet_idx]+' config begin!\n')
        sheet_data = data.sheets()[sheet_idx]
        rows_num = sheet_data.nrows
        for x in range(0,rows_num):
            if sheet_data.cell_value(x,0) == 'sleep':
                if sheet_data.cell_value(x,1) == '':
                    time.sleep(5)
                    self.ui.textBrowser.insertPlainText('sleep 5\n')
                else:
                    tmp_time = int(sheet_data.cell_value(x,1))
                    time.sleep(tmp_time)
                    self.ui.textBrowser.insertPlainText('sleep '+str(tmp_time)+'\n')
            elif sheet_data.cell_value(x,0) == 'wait':
                temp_addr = int(sheet_data.cell_value(x,1),16)
                temp_value = int(sheet_data.cell_value(x,2),16)
                for i in range(0,300):
                    time.sleep(1)
                    read_value = self.read_atom(temp_addr)
                    if read_value[0] == temp_value:
                        self.ui.textBrowser.insertPlainText('wait event done!\n')
                        break
                    if i == 299:
                        self.ui.textBrowser.insertPlainText('after 5min, wait event not done! force quit\n')
            elif sheet_data.cell_value(x,0) == '':
                pass
            else:
                temp_addr = int(sheet_data.cell_value(x, 0), 16)
                temp_data = int(sheet_data.cell_value(x, 1), 16)
                self.write_atom(temp_addr, temp_data)
        self.ui.textBrowser.insertPlainText(time.ctime()+': seq '+sheetsall[sheet_idx]+' config done!\n')
    def deal_emit_sheet(self, select_sheet):
        self.sheet_sel_lst = select_sheet
    def read_mem_reg(self, addr0, addr1):
        write_buffer = (c_ubyte * 2)()
        read_buffer = (c_ubyte * 4096)()
        write_buffer[0] = addr0
        write_buffer[1] = addr1
        nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 4096)
        return read_buffer
    def mem_read(self):
        smp_lst = ['smp ddc output', 'smp tiskew corr', 'initial mem to 0', 'initial mem to 1']
        dialog = MainDialog(smp_lst)
        dialog.Signal_parp.connect(self.deal_emit_sheet)
        dialog.show()
        dialog.exec_()
        sheet_idx = smp_lst.index(self.sheet_sel_lst)
        if sheet_idx == 0:
            self.ui.textBrowser.insertPlainText('start sample ddc output!\n')
            #ddc output
            self.write_atom(0xf18, 0x00)
            self.write_atom(0xf16, 0x00)
            self.write_atom(0xf1d, 0x1)
            self.write_atom(0xf1c, 0x1)
            self.write_atom(0xf16, 0x08)
            self.write_atom(0xf17, 0x40)
            self.write_atom(0xf19, 0x3c)
            self.write_atom(0xf1a, 0x00)
            self.write_atom(0xf1b, 0x10)
            self.write_atom(0xf1d, 0x0)
            self.write_atom(0xf1c, 0x0)
            self.write_atom(0xf18, 0x02)
        elif sheet_idx == 1:
            self.ui.textBrowser.insertPlainText('start sample tiskew_corr output!\n')
            pass
        elif sheet_idx == 2:
            self.ui.textBrowser.insertPlainText('start initial mem to 0!\n')
            self.write_atom(0xf10, 0x0)
            self.write_atom(0xf11, 0x0)
            for i in range(0, 131072):
                self.write_atom(0xf24, 0x0)
        elif sheet_idx == 3:
            self.ui.textBrowser.insertPlainText('start initial mem to 1!\n')
            self.write_atom(0xf10, 0x0)
            self.write_atom(0xf11, 0x0)
            for i in range(0, 131072):
                self.write_atom(0xf24, 0xff)
        ##transport output0
        # self.write_atom(0xf18, 0x00)
        # self.write_atom(0xf16, 0x00)
        # self.write_atom(0xf1d, 0x1)
        # self.write_atom(0xf1c, 0x1)
        # self.write_atom(0xf16, 0xb)
        # self.write_atom(0xf17, 0x64)
        # self.write_atom(0xf19, 0x3c)
        # self.write_atom(0xf1a, 0x00)
        # self.write_atom(0xf1b, 0x10)
        # self.write_atom(0xf1d, 0x0)
        # self.write_atom(0xf1c, 0x0)
        # self.write_atom(0x5f8, 0x10)
        # self.write_atom(0xf18, 0x0)
        # ##transport output1
        # self.write_atom(0xf18, 0x00)
        # self.write_atom(0xf16, 0x00)
        # self.write_atom(0xf1d, 0x1)
        # self.write_atom(0xf1c, 0x1)
        # self.write_atom(0xf16, 0xb)
        # self.write_atom(0xf17, 0x24)
        # self.write_atom(0xf19, 0x3c)
        # self.write_atom(0xf1a, 0x00)
        # self.write_atom(0xf1b, 0x10)
        # self.write_atom(0xf1d, 0x0)
        # self.write_atom(0xf1c, 0x0)
        # self.write_atom(0x5f8, 0x15)
        # self.write_atom(0xf18, 0x0)
        ##read mem
        self.write_atom(0xf16, 0x10)
        self.write_atom(0xf10, 0x01)
        self.write_atom(0xf10, 0x0)
        self.write_atom(0xf11, 0x0)
        time.sleep(5)
        offset = 0x00
        data_old = 0x55
        fp = open('memory_dump_data.txt', 'w')
        for i in range(0, 32):
            data_new = i * 4 + offset
            self.write_atom(0xf11, data_old)
            self.write_atom(0xf11, data_new)
            read_buffer = self.read_mem_reg(0x8f, 0x24)
            for k in range(0, len(read_buffer)):
                fp.write("%02x\n" % (read_buffer[k]))
        fp.close()
        fd = open(r'D:\projects\DIQUN\diqun_fpga\write\memory_dump_data.txt')
        all_data = [x.strip() for x in fd]
        fd.close()
        if sheet_idx == 1:
            fo = open('mem.dat', 'w')
            for i in range(0, 2):
                for j in range(0, 2048):
                    dout = ''
                    for k in range(0, 8):
                        for m in range(0, 4):
                            idx = i * 65536 + j * 4 + k * 8192 + m
                            dout = all_data[idx] + dout
                    fo.write(dout + '\n')
            fo.close()
        self.ui.textBrowser.insertPlainText(time.ctime()+': mem read done!\n')
    def fft_gen(self):
        self.ui.textBrowser.clear()
        # fd = open('memory_dump_data.txt', 'r')
        # data = [x.strip() for x in fd]
        # fd.close()
        # data_num = len(data)
        # ts = np.linspace(1,data_num,data_num)
        # fft_size = 8192
        # data_array = np.array(data)
        # freq = np.linspace(1,int(fft_size)/2,int(fft_size/2)+1)
        # dout_fft = np.fft.rfft(data_array[:fft_size])/fft_size
        # dout_db = 20*np.log10(np.abs(dout_fft))
        # plt.figure(1)
        # plt.plot(freq, dout_db)
        # plt.figure(2)
        # plt.plot(ts,data_array)
        # plt.legend()
        # plt.show()
    def weight_rd(self):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('adc_weight')
        ws.write(0,0,'ch_idx')
        ws.write(0,1,'ch0')
        ws.write(0,2,'ch1')
        ws.write(0,3,'ch2')
        ws.write(0,4,'ch3')
        ws.write(1,0,'mdac0_weight1')
        ws.write(2,0,'mdac1_weight1')
        ws.write(3,0,'mdac2_weight1')
        ws.write(4,0,'mdac3_weight1')
        ws.write(5,0,'mdac4_weight1')
        ws.write(6,0,'mdac5_weight1')
        ws.write(7,0,'mdac6_weight1')
        ws.write(8,0,'mdac7_weight1')
        ws.write(9,0,'mdac0_weight2')
        ws.write(10,0,'mdac1_weight2')
        ws.write(11,0,'mdac2_weight2')
        ws.write(12,0,'mdac3_weight2')
        ws.write(13,0,'mdac4_weight2')
        ws.write(14,0,'mdac5_weight2')
        ws.write(15,0,'mdac6_weight2')
        ws.write(16,0,'mdac7_weight2')
        ws.write(17,0,'bkadc0_weight1')
        ws.write(18,0,'bkadc1_weight1')
        ws.write(19,0,'bkadc2_weight1')
        ws.write(20,0,'bkadc3_weight1')
        ws.write(21,0,'bkadc4_weight1')
        ws.write(22,0,'bkadc5_weight1')
        ws.write(23,0,'bkadc6_weight1')
        ws.write(24,0,'bkadc7_weight1')
        ws.write(25,0,'bkadc0_weight2')
        ws.write(26,0,'bkadc1_weight2')
        ws.write(27,0,'bkadc2_weight2')
        ws.write(28,0,'bkadc3_weight2')
        ws.write(29,0,'bkadc4_weight2')
        ws.write(30,0,'bkadc5_weight2')
        ws.write(31,0,'bkadc6_weight2')
        ws.write(32,0,'bkadc7_weight2')
        ws.write(33,0,'bkadc0_weight3')
        ws.write(34,0,'bkadc1_weight3')
        ws.write(35,0,'bkadc2_weight3')
        ws.write(36,0,'bkadc3_weight3')
        ws.write(37,0,'bkadc4_weight3')
        ws.write(38,0,'bkadc5_weight3')
        ws.write(39,0,'bkadc6_weight3')
        ws.write(40,0,'bkadc7_weight3')
        ws.write(41,0,'mdac_os0_weight')
        ws.write(42,0,'mdac_os1_weight')
        ws.write(43,0,'mdac_gec_weight')
        ws.write(44,0,'mdac_dither_weight')
        ws.write(45,0,'gec_coeff')
        ws.write(46,0,'chopper_coeff')
        ws.write(47,0,'tios_coeff')
        ws.write(48,0,'tigain_coeff')
        ws.write(49, 0, 'tiskew_code')
        ws.write(50, 0, 'opgain_code')
        for ch_idx in range(0,4):
            for os_idx in range(0,2):
                read_data = self.read_atom(0x800+0x1d+ch_idx*4+os_idx*2)
                read_data1 = self.read_atom(0x800+0x1e+ch_idx*4+os_idx*2)
                weight = read_data1[0]*256+read_data[0]
                ws.write(41+os_idx,1+ch_idx,weight)
            read_data = self.read_atom(0x800+0x2d+ch_idx*2)
            read_data1 = self.read_atom(0x800+0x2e+ch_idx*2)
            weight = read_data1[0]*256+read_data[0]
            ws.write(43,1+ch_idx,weight)
            for mdac_idx in range(0,8):
                read_data = self.read_atom(0x800+0x3c+ch_idx*24+mdac_idx*3)
                read_data1 = self.read_atom(0x800+0x3d+ch_idx*24+mdac_idx*3)
                read_data2 = self.read_atom(0x800+0x3e+ch_idx*24+mdac_idx*3)
                weight = read_data2[0]*65536+read_data1[0]*256+read_data[0]
                ws.write(1+mdac_idx,1+ch_idx,weight)
                read_data = self.read_atom(0x800+0x9c+ch_idx*16+mdac_idx*2)
                read_data1 = self.read_atom(0x800+0x9d+ch_idx*16+mdac_idx*2)
                weight = read_data1[0]*256+read_data[0]
                ws.write(9+mdac_idx,1+ch_idx,weight)
                read_data = self.read_atom(0x800+0xdc+ch_idx*16+mdac_idx*2)
                read_data1 = self.read_atom(0x800+0xdd+ch_idx*16+mdac_idx*2)
                weight = read_data1[0]*256+read_data[0]
                ws.write(17+mdac_idx,1+ch_idx,weight)
                read_data = self.read_atom(0x800+0x11c+ch_idx*16+mdac_idx*2)
                read_data1 = self.read_atom(0x800+0x11d+ch_idx*16+mdac_idx*2)
                weight = read_data1[0]*256+read_data[0]
                ws.write(25+mdac_idx,1+ch_idx,weight)
                read_data = self.read_atom(0x800+0x15c+ch_idx*16+mdac_idx*2)
                read_data1 = self.read_atom(0x800+0x15d+ch_idx*16+mdac_idx*2)
                weight = read_data1[0]*256+read_data[0]
                ws.write(33+mdac_idx,1+ch_idx,weight)
            read_data = self.read_atom(0x800+0x19c+ch_idx*3)
            read_data1 = self.read_atom(0x800+0x19d+ch_idx*3)
            read_data2 = self.read_atom(0x800+0x19e+ch_idx*3)
            weight = read_data2[0]*65536+read_data1[0]*256+read_data[0]
            ws.write(44,1+ch_idx,weight)
            read_data = self.read_atom(0x800+0x365+ch_idx*2)
            read_data1 = self.read_atom(0x800+0x366+ch_idx*2)
            weight = read_data1[0]*256+read_data[0]
            ws.write(45,1+ch_idx,weight)
            read_data = self.read_atom(0x800+0x383+ch_idx*2)
            read_data1 = self.read_atom(0x800+0x384+ch_idx*2)
            weight = read_data1[0]*256+read_data[0]
            ws.write(46,1+ch_idx,weight)
            read_data = self.read_atom(0x800+0x3a6+ch_idx*2)
            read_data1 = self.read_atom(0x800+0x3a7+ch_idx*2)
            weight = read_data1[0]*256+read_data[0]
            ws.write(47,1+ch_idx,weight)
            read_data = self.read_atom(0x800+0x3c8+ch_idx*2)
            read_data1 = self.read_atom(0x800+0x3c9+ch_idx*2)
            weight = read_data1[0]*256+read_data[0]
            ws.write(48,1+ch_idx,weight)
            read_data = self.read_atom(0x800 + 0x3fa + ch_idx * 2)
            read_data1 = self.read_atom(0x800 + 0x3fb + ch_idx * 2)
            weight = read_data1[0] * 256 + read_data[0]
            ws.write(49, 1 + ch_idx, weight)
            read_data = self.read_atom(0x800 + 0x38 + ch_idx)
            weight = read_data[0]
            ws.write(50, 1 + ch_idx, weight)
        wb.save('ana_weight.xls')
        self.ui.textBrowser.insertPlainText(time.ctime() + ': weight read done!\n')
    def cali_cfg(self):
        self.ui.textBrowser.insertPlainText(time.ctime()+': cali cfg!\n')
        cali_thread = threading.Thread(target=self.cali_config)
        cali_thread.start()
    def cali_config(self):
        for x in range(50):
            self.ui.textBrowser.insertPlainText(time.ctime() + ': threading test'+str(x)+'!\n')
            time.sleep(5)
            self.fsm_oneround()
    def fsm_oneround(self):
        self.write_atom(0x810, 0x1)
        time.sleep(1)
        self.write_atom(0x810,0x0)
        time.sleep(1)
        self.write_atom(0xb60,0x1)
        time.sleep(1)
        self.write_atom(0xb60,0x0)
        time.sleep(1)
        self.write_atom(0xba0,0x1)
        time.sleep(1)
        self.write_atom(0xba0,0x0)
        time.sleep(1)
        self.write_atom(0xbd8, 0x1)
        self.write_atom(0xbd9, 0x1)
        self.write_atom(0xbda, 0x1)
        self.write_atom(0xbdb, 0x1)
        self.write_atom(0xbd8, 0x0)
        self.write_atom(0xbd9, 0x0)
        self.write_atom(0xbda, 0x0)
        self.write_atom(0xbdb, 0x0)
        self.write_atom(0xbc7, 0x0) ##can del
        self.write_atom(0xbc0, 0x1)
        time.sleep(1)
        self.write_atom(0xbc0, 0x0)
        self.write_atom(0xbf9, 0x0) ## can del
        self.write_atom(0xbf0, 0x1)
        for i in range(300):
            time.sleep(1)
            read_value = self.read_atom(0xbf1)
            if read_value[0] == 1:
                self.ui.textBrowser.insertPlainText('wait event done!\n')
                break
            if i == 299:
                self.ui.textBrowser.insertPlainText('after 5min, wait event not done! force quit\n')
        self.write_atom(0xbf0,0x1)

    def j204_cfg(self):
        self.ui.textBrowser.insertPlainText(time.ctime()+': j204 cfg!\n')
    def nyq0(self):
        self.ui.textBrowser.insertPlainText(time.ctime()+': nyq0 cfg!\n')
    def nyq1(self):
        self.ui.textBrowser.insertPlainText(time.ctime()+': nyq1 cfg!\n')
    def nyq2(self):
        self.ui.textBrowser.insertPlainText(time.ctime()+': nyq2 cfg!\n')
    def nyq3(self):
        self.ui.textBrowser.insertPlainText(time.ctime()+': nyq3 cfg!\n')
        
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
