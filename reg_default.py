from ctypes import *
from time import sleep
# Import module
import ControlSPI
import time
import random

# Scan device
nRet = ControlSPI.VSI_ScanDevice(1)
if(nRet <= 0):
    print("No device connect!")
  #  exit()
else:
    print("Connected device number is:"+repr(nRet))

# Open device
nRet = ControlSPI.VSI_OpenDevice(ControlSPI.VSI_USBSPI,0,0)
if(nRet != ControlSPI.ERR_SUCCESS):
    print("Open device error!")
    #exit()
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

nRet = ControlSPI.VSI_InitSPI(ControlSPI.VSI_USBSPI,0,byref(SPI_Init))
if(nRet != ControlSPI.ERR_SUCCESS):
    print("Initialization device error!")
   # exit()
else:
    print("Initialization device success!")



write_buffer = (c_ubyte * 1024)()
read_buffer = (c_ubyte * 8192)()


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

def write_mem_reg(addr0,addr1,data0):
    write_buffer = (c_ubyte * 3)()
    read_buffer = (c_ubyte * 1)()
    write_buffer[0] = addr0
    write_buffer[1] = addr1
    write_buffer[2] = data0
    #print(write_buffer[0],write_buffer[1],write_buffer[2])
   # print(str(addr0)+' '+str(addr1)+' '+str(data0))
    nRet = ControlSPI.VSI_WriteBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 3)

def read_mem_reg(addr0, addr1):
    write_buffer = (c_ubyte * 2)()
    read_buffer = (c_ubyte * 4096)()
    write_buffer[0] = addr0
    write_buffer[1] = addr1
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 4096)
    return read_buffer

def read_mem_reg_single(addr0, addr1):
    write_buffer = (c_ubyte * 2)()
    read_buffer = (c_ubyte * 1)()
    write_buffer[0] = addr0
    write_buffer[1] = addr1
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 1)
    return read_buffer



fp=open('reg_default.csv','w')
#print(read_buffer[0])
for i in range(0, 93):
    addr_new = i+112
    read_buffer = read_mem_reg_single(0x81, addr_new)
    fp.write("%02x\n" % (read_buffer[0]))
fp.close()


#     write_mem_reg(0x0f,0x11,data_old)
#     write_mem_reg(0x0f,0x11,data_new)
#     #print("%02x\n" % (data_new))
#     read_buffer = read_mem_reg(0x8f, 0x24)
#     for k in range(0, len(read_buffer)):
#         fp.write("%02x\n" % (read_buffer[k]))
# fp.close()


