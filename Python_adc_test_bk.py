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
    exit()
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
    exit()
else:
    print("Initialization device success!")


write_buffer = (c_ubyte * 1024)()
read_buffer = (c_ubyte * 4096)()

#write_buffer[0:21]0x88 0x05 0x8e 0x80 0x90 0x80 0x92 0x20 0x9c 0x29 0x9e 0x29 0xa0 0x01 0xa2 0x00  0xa6 0x50 0x88 0x00 0x88 0x01

write_buffer[0] = 0x88
write_buffer[1] = 0x05
write_buffer[2] = 0x8e
write_buffer[3] = 0x80
write_buffer[4] = 0x90
write_buffer[5] = 0x80
write_buffer[6] = 0x92
write_buffer[7] = 0x20
write_buffer[8] = 0x9c
write_buffer[9] = 0x29
write_buffer[10] = 0x9e
write_buffer[11] = 0x29
write_buffer[12] = 0xa0
write_buffer[13] = 0x01
write_buffer[14] = 0xa2
write_buffer[15] = 0x00
write_buffer[16] = 0xa6
write_buffer[17] = 0x50
write_buffer[18] = 0x88
write_buffer[19] = 0x00
write_buffer[20] = 0x88
write_buffer[21] = 0x01
write_buffer[22] = 0x89
write_buffer[23] = 0x00
write_buffer[24] = 0x00
write_buffer[25] = 0x00
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 26, read_buffer, 2)

if(nRet != ControlSPI.ERR_SUCCESS):
	print("Write&Read data error :%d"%nRet)
	exit()
else:
	print("Read data(Hex):")

if(read_buffer[0] == 0x01):
    print("clock reset succuss!")
else:
    print("clock reset fail!")

#main code start here

f = open("icali_reg.txt" , "r")
line = f.readline()
fp = open('adc_data_mem.out', 'w')

index = 0
while line:
    # print line
    line_new = line.replace("\n","")
    buf = line_new.split(' ')

    # i1 cali
    write_buffer[0] = 0x54
    write_buffer[1] = int(buf[0],16)
    write_buffer[2] = 0x52
    write_buffer[3] = int(buf[1],16)
    write_buffer[4] = 0x50
    write_buffer[5] = int(buf[2],16)
    write_buffer[6] = 0x4e
    write_buffer[7] = int(buf[3],16)
    write_buffer[8] = 0x4c
    write_buffer[9] = int(buf[4],16)
    write_buffer[10] = 0x4a
    write_buffer[11] = int(buf[5],16)
    write_buffer[12] = 0x48
    write_buffer[13] = int(buf[6],16)
    write_buffer[14] = 0x46
    write_buffer[15] = int(buf[7],16)
    write_buffer[16] = 0x44
    write_buffer[17] = int(buf[8],16)
    write_buffer[18] = 0x42
    write_buffer[19] = int(buf[9],16)
    write_buffer[20] = 0x40
    write_buffer[21] = int(buf[10],16)
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 22, read_buffer, 2)

    # i2 cali
    write_buffer[0] = 0x6a
    write_buffer[1] = int(buf[0], 16)
    write_buffer[2] = 0x68
    write_buffer[3] = int(buf[1], 16)
    write_buffer[4] = 0x66
    write_buffer[5] = int(buf[2], 16)
    write_buffer[6] = 0x64
    write_buffer[7] = int(buf[3], 16)
    write_buffer[8] = 0x62
    write_buffer[9] = int(buf[4], 16)
    write_buffer[10] = 0x60
    write_buffer[11] = int(buf[5], 16)
    write_buffer[12] = 0x5e
    write_buffer[13] = int(buf[6], 16)
    write_buffer[14] = 0x5c
    write_buffer[15] = int(buf[7], 16)
    write_buffer[16] = 0x5a
    write_buffer[17] = int(buf[8], 16)
    write_buffer[18] = 0x58
    write_buffer[19] = int(buf[9], 16)
    write_buffer[20] = 0x56
    write_buffer[21] = int(buf[10], 16)
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 22, read_buffer, 2)

    # clock reset
    write_buffer[0] = 0x88
    write_buffer[1] = 0x00
    write_buffer[2] = 0x88
    write_buffer[3] = 0x01
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 4, read_buffer, 2)

    # memory auto read
    write_buffer[0] = 0xc0
    write_buffer[1] = 0x00
    write_buffer[2] = 0x00
    write_buffer[3] = 0x00
    write_buffer[4] = 0x04
    write_buffer[5] = 0x00
    write_buffer[6] = 0x00
    write_buffer[7] = 0x00
    write_buffer[8] = 0x01
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

    # read memory data
    write_buffer[0] = 0xc1
    write_buffer[1] = 0x00
    write_buffer[2] = 0x00
    write_buffer[3] = 0x20
    write_buffer[4] = 0x00
    write_buffer[5] = 0x00

    # nRet = ControlSPI.VSI_WriteBytes(ControlSPI.VSI_USBSPI,0,0,write_buffer,2)
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 4096)
    if (nRet != ControlSPI.ERR_SUCCESS):
        print("Write&Read data error :%d" % nRet)
        exit()
    else:
        print("Read data from spi:")

    for i in range(0, 4096):
        fp.write("%02X " % (read_buffer[i]))
    fp.write("\n")

    print("Write data to file data_mem.out")

    line = f.readline()

    index = index + 1
f.close()
fp.close()
print(index)





















