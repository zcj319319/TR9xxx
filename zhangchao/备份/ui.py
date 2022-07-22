# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from ui_base import test_ui
from ui_base import test_dialog 
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import threading
import time
import ctypes
import inspect
from ctypes import *
import ControlSPI
import re
import xlrd
import xlwt

class MainDialog(QDialog):
    Signal_parp = pyqtSignal(list)
    def __init__(self):
        super(MainDialog, self).__init__()
        self.ui = test_dialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.para_updata)
        self.select_sheet = []
    def para_updata(self):
        self.select_sheet.append(self.ui.lineEdit.text())
        self.select_sheet.append(self.ui.lineEdit_2.text())
        self.select_sheet.append(self.ui.lineEdit_3.text())
        self.select_sheet.append(self.ui.lineEdit_4.text())
        self.Signal_parp.emit(self.select_sheet)
        self.ok_and_quit()
    def ok_and_quit(self):
        self.close()
        
class MainDialog1(QDialog):
    Signal_parp = pyqtSignal(str)
    def __init__(self, sheet_lst):
        super(MainDialog1, self).__init__()
        self.ui = test_dialog.Ui_Dialog1()
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

class MyFigure(FigureCanvas):
    def __init__(self,width=5,height=4,dpi=100):
        self.fig = Figure(figsize=(width,height),dpi=dpi)
        super(MyFigure,self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)
    def plotsin(self):
        self.axes0 = self.fig.add_subplot(111)
        ts = np.linspace(1,4096,4096)
        ts_data = np.sin(2*np.pi*ts/399)
        self.axes0.plot(ts,ts_data)
    def plotfft(self):
        ts = np.linspace(1,4096,4096)
        ts_data = np.sin(2*np.pi*ts*111/4096)
        self.axes0 = self.fig.add_subplot(111)
        fft_size = 4096
        freq = np.linspace(1,int(fft_size/2),int(fft_size/2)+1)
        data_fft = np.fft.rfft(ts_data)/fft_size
        self.axes0.plot(freq,data_fft)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = test_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.F = MyFigure(width=3,height=2,dpi=100)
        self.F0 = MyFigure(width=3,height=2,dpi=100)
        self.push_button_cnt = 'start'
        self.ui.pushButton.clicked.connect(self.background_test)
        self.ui.toolButton.clicked.connect(self.para_read)
        self.ui.pushButton_2.clicked.connect(self.read_addr)
        self.ui.pushButton_3.clicked.connect(self.write_addr)
        self.ui.toolButton_2.clicked.connect(self.load_test_seq)
        self.ui.pushButton_4.clicked.connect(self.mem_read)
        self.ui.pushButton_5.clicked.connect(self.gen_waveform)
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
        dialog = MainDialog1(sheetsall)
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
    def read_mem_reg(self, addr0, addr1):
        write_buffer = (c_ubyte * 2)()
        read_buffer = (c_ubyte * 4096)()
        write_buffer[0] = addr0
        write_buffer[1] = addr1
        nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 4096)
        return read_buffer
    def mem_read(self):
        smp_lst = ['smp ddc output', 'smp tiskew corr', 'initial mem to 0', 'initial mem to 1', 'weight_rd', 'terminal clear']
        dialog = MainDialog1(smp_lst)
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
        elif sheet_idx == 4:
            self.weight_rd()
        elif sheet_idx == 5:
            self.ui.textBrowser.clear()
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
        if sheet_idx == 0:
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
        # if sheet_idx == 1:
        #     fd = open(r'C:\Project\reg_map\write\memory_dump_data.txt')
        #     all_data = [x.strip() for x in fd]
        #     fd.close()
        #     fo = open('mem.dat', 'w')
        #     for i in range(0, 2):
        #         for j in range(0, 2048):
        #             dout = ''
        #             for k in range(0, 8):
        #                 for m in range(0, 4):
        #                     idx = i * 65536 + j * 4 + k * 8192 + m
        #                     dout = all_data[idx] + dout
        #             fo.write(dout + '\n')
        #     fo.close()
            self.ui.textBrowser.insertPlainText(time.ctime()+': mem read done!\n')
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
    def background_test(self):
        self.cali_run = []
        self.cali_run.append(self.ui.checkBox.isChecked())
        self.cali_run.append(self.ui.checkBox_2.isChecked())
        self.cali_run.append(self.ui.checkBox_3.isChecked())
        self.cali_run.append(self.ui.checkBox_4.isChecked())
        self.cali_run.append(self.ui.checkBox_5.isChecked())
        if self.push_button_cnt == 'start':
            self.push_button_cnt = 'end'
            self.ui.pushButton.setStyleSheet("QPushButton{border-image: url(./ui_base/end.png)}")
            self.ui.textBrowser.insertPlainText(time.ctime()+': starting run ')
            if self.ui.checkBox.isChecked():
                self.ui.textBrowser.insertPlainText('DNC ')
            if self.ui.checkBox_2.isChecked():
                self.ui.textBrowser.insertPlainText('GEC ')
            if self.ui.checkBox_3.isChecked():
                self.ui.textBrowser.insertPlainText('TIOS ')
            if self.ui.checkBox_4.isChecked():
                self.ui.textBrowser.insertPlainText('TIGAIN ')
            if self.ui.checkBox_5.isChecked():
                self.ui.textBrowser.insertPlainText('TISKEW')
            self.ui.textBrowser.insertPlainText('\n')
            if self.cali_run[0] == 1:       ##DNC
                self.write_atom(0x810,0x1)
                time.sleep(5)
                self.write_atom(0x810,0x0)
            self.cali_thread = threading.Thread(target=self.cali_bk_run)
            self.cali_thread.start()
        else:
            self.push_button_cnt = 'start'
            self.ui.pushButton.setStyleSheet("QPushButton{border-image: url(./ui_base/start.png)}")
            self.ui.textBrowser.insertPlainText(time.ctime()+': pause cali\n')
            self.write_atom(0xb60, 0x0)
            self.write_atom(0xba0, 0x0)
            self.write_atom(0xbc0, 0x0)
            self.write_atom(0xbf0, 0x0)
            self.stop_thread(self.cali_thread)
    def cali_bk_run(self):
        for x in range(50):
            self.ui.textBrowser.insertPlainText(time.ctime()+': threading test'+str(x)+'!\n')
            if self.cali_run[1] == 1:       ##GEC
                self.write_atom(0xb60,0x1)
                time.sleep(1)
                self.write_atom(0xb60,0x0)
            if self.cali_run[2] == 1:       ##TIOS
                self.write_atom(0xba0,0x1)
                time.sleep(5)
                self.write_atom(0xba0,0x0)
            if self.cali_run[3] == 1:       ##TIGAIN
                self.write_atom(0xbd8,0x1)
                self.write_atom(0xbd9,0x1)
                self.write_atom(0xbda,0x1)
                self.write_atom(0xbdb,0x1)
                self.write_atom(0xbd8,0x0)
                self.write_atom(0xbd9,0x0)
                self.write_atom(0xbda,0x0)
                self.write_atom(0xbdb,0x0)
                self.write_atom(0xbc7,0x0)
                self.write_atom(0xbc0,0x1)
                time.sleep(1)
                self.write_atom(0xbc0,0x0)
            if self.cali_run[4] == 1:       ##TISKEW
                self.write_atom(0xbf0,0x1)
                for i in range(300):
                    time.sleep(1)
                    read_value = self.read_atom(0xbf1)
                    if read_value[0] == 1:
                        break
                    if i == 299:
                        self.ui.textBrowser.insertPlainText('after 5min, wait event not done! force quit\n')
                self.write_atom(0xbf0,0x0)
            time.sleep(5)
    def _async_raise(self,tid,exctype):
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,ctypes.py_object(exctype))
        if res == 0:
            raise ValueError('invalid thread id')
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
    def stop_thread(self,thread):
        self._async_raise(thread.ident, SystemExit)
    def para_read(self):
        dialog = MainDialog()
        dialog.Signal_parp.connect(self.deal_emit_sheet)
        dialog.show()
        dialog.exec_()
        self.ui.lineEdit.setText(self.para_lst[0])
        self.ui.lineEdit_2.setText(self.para_lst[1])
        self.ui.lineEdit_3.setText(self.para_lst[2])
        self.ui.lineEdit_4.setText(self.para_lst[3])
        if self.para_lst[0] != '' and self.para_lst[1] != '':
            fs = float(self.para_lst[0])
            fin = float(self.para_lst[1])
            direct2 = (np.sign(np.sin(2*np.pi*fin/fs))*-1+1)/2
            direct1 = (np.sign(np.sin(2*np.pi*2*fin/fs))*-1+1)/2
            direct0 = (np.sign(np.sin(2*np.pi*fin/fs))*-1+1)/2
            direct = int(direct2*4+direct1*2+direct0)
            self.write_atom(0xbf9,direct)
    def deal_emit_sheet(self, select_sheet):
        self.para_lst = select_sheet
        self.sheet_sel_lst = select_sheet
    def gen_waveform(self):
        self.F.plotsin()
        self.ui.gridLayout = QGridLayout(self.ui.groupBox)
        self.ui.gridLayout.addWidget(self.F,0,1)
        self.F0.plotfft()
        self.ui.gridLayout = QGridLayout(self.ui.groupBox_2)
        self.ui.gridLayout.addWidget(self.F0,0,1)
        
        

if __name__ == '__main__':
#    app = QtWidgets.QApplication(sys.argv) # 是PyQt的整个后台管理的命脉
##    app.setWindowIcon(QIcon('./images/cartoon1.ico')) # 设置窗口的头标
#    form = Ui_MainWindow() # 调用MainWindow类，并进行显示
#    form.show()
#    sys.exit(app.exec_()) # 运行主循环，必须调用此函数才可以开始事件处理
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

