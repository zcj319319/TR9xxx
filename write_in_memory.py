"""
Program test environment
Pyhone version:3.4.1
Firmware version:2.2.12
Dependent files(MacOSX):libGinkgo_Driver.dylib,libusb-0.1.4.dylib,libusb-1.0.0.dylib,ControlSPI.py
Dependent files(Windows):Ginkgo_Driver.dll,ControlSPI.py
Dependent files(Linux):libGinkgo_Driver.so,libusb-1.0.so,ControlSPI.py
More Infomation:www.viewtool.com
"""
from ctypes import *
from time import sleep
# Import module
import ControlSPI

# Scan device
nRet = ControlSPI.VSI_ScanDevice(1)
if(nRet <= 0):
    print("No device connect!")
else:
    print("Connected device number is:"+repr(nRet))

# Open device
nRet = ControlSPI.VSI_OpenDevice(ControlSPI.VSI_USBSPI,0,0)
if(nRet != ControlSPI.ERR_SUCCESS):
    print("Open device error!")
    exit()
else:
    print("Open device success!")
# Initialize device
SPI_Init = ControlSPI.VSI_INIT_CONFIG()
SPI_Init.ClockSpeed = 450000;
SPI_Init.ControlMode = 1;
SPI_Init.CPHA = 0;
SPI_Init.CPOL = 0;
SPI_Init.LSBFirst = 0;
SPI_Init.MasterMode = 1;
SPI_Init.SelPolarity = 0;
SPI_Init.TranBits = 8;

nRet = ControlSPI.VSI_InitSPI(ControlSPI.VSI_USBSPI,0,byref(SPI_Init))
if(nRet != ControlSPI.ERR_SUCCESS):
    print("Initialization device error!")
else:
    print("Initialization device success!")


write_buffer = (c_ubyte * 4196)()
read_buffer = (c_ubyte * 4096)()



#### function define
def read_spi_reg(addr,data):
    write_buffer = (c_ubyte * 4)()
    read_buffer = (c_ubyte * 1)()
    write_buffer[0] = addr
    write_buffer[1] = data
    write_buffer[2] = 0x00
    write_buffer[3] = 0x00
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 4, read_buffer, 1)
    return read_buffer

def write_spi_reg(addr,data):
    write_buffer = (c_ubyte * 2)()
    read_buffer = (c_ubyte * 2)()
    write_buffer[0] = addr
    write_buffer[1] = data
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 2)

def write_mem_reg(addr0,addr1,data0,data1,data2,data3):
    write_buffer = (c_ubyte * 9)()
    read_buffer = (c_ubyte * 2)()
    write_buffer[0] = 0xc0
    write_buffer[1] = 0x00
    write_buffer[2] = 0x00
    write_buffer[3] = addr0
    write_buffer[4] = addr1
    write_buffer[5] = data0
    write_buffer[6] = data1
    write_buffer[7] = data2
    write_buffer[8] = data3
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

def read_mem_reg(addr0, addr1):
    write_buffer = (c_ubyte * 6)()
    read_buffer = (c_ubyte * 4)()
    write_buffer[0] = 0xc1
    write_buffer[1] = 0x00
    write_buffer[2] = 0x00
    write_buffer[3] = addr0
    write_buffer[4] = addr1
    write_buffer[5] = 0x00
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 4)
    return read_buffer


############################# main code start here ##############################################

write_spi_reg(0x84,0x80)   #itrim_i
write_spi_reg(0x86,0x80)   #itrim_q
write_spi_reg(0x88,0x81)   # sync in

write_mem_reg(0x00,0x20,0x00,0x00,0x00,0x27)  #encode mode
write_mem_reg(0x00,0x24,0x00,0x00,0x00,0x27)  # thermal 01/rotation  03/shuffle  27

write_mem_reg(0x00,0x38,0x00,0x00,0x00,0x0c)  #encode enable
write_mem_reg(0x00,0x3c,0x00,0x00,0x00,0x0c)  # [3] [2] enable

write_mem_reg(0x00,0x08,0x00,0x00,0x00,0xc3)  #[7:6] nco en   [1:0] filter en
write_mem_reg(0x00,0x0c,0x00,0x00,0x00,0xc3)  # 03 from memory data

write_mem_reg(0x00,0x40,0x3c,0xc0,0x00,0x00)  #nco freq i
write_mem_reg(0x00,0x44,0x3c,0xc0,0x00,0x00)  #nco freq i

write_mem_reg(0x00,0x18,0x00,0x00,0x00,0x53)  #cali num select i
write_mem_reg(0x00,0x1c,0x00,0x00,0x00,0x53)  #cali num select q

write_mem_reg(0x00,0x10,0x00,0x00,0x00,0x01)  #cali start i
write_mem_reg(0x00,0x14,0x00,0x00,0x00,0x01)  #cali start q

sleep(1)
import math
f = open("dac_mem_data_in.txt" , "r")
line = f.readline()
while line:
        # print line
         line_new = line.replace("\n","")
         buf = line_new.split(' ')
         line = f.readline()
for q in range(0, 65536):
        write_buffer[0] = 0xc0
        write_buffer[1] = 0x00
        high_bit = math.floor((q*1*4+8192)/65536)
        middle_bit = math.floor((q * 1*4 + 8192 - high_bit*65536)/ 256)
        low_bit = q * 1*4 + 8192 - high_bit * 65536 - middle_bit *256
        write_buffer[2] = math.trunc(high_bit)
        write_buffer[3] = math.trunc(middle_bit)
        write_buffer[4] = math.trunc(low_bit)
        #print(hex(write_buffer[2]))
       # print(hex(write_buffer[3]))
       # print(hex(write_buffer[4]))
        for i in range(0, 4):
            write_buffer[i + 5] = int(buf[i+q*4], 16)
        nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)


print("Read from txt data")

if(nRet != ControlSPI.ERR_SUCCESS):
	print("Write&Read data error :%d"%nRet)
	exit()
else:
	print("Write to dac memory")


print("Finish config")




















