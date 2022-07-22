from ctypes import *
from time import sleep
# Import module
import ControlSPI

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
   # exit()
else:
    print("Initialization device success!")


write_buffer = (c_ubyte * 1024)()
read_buffer = (c_ubyte * 8192)()


#### function define
def read_spi_reg(addr0,addr1):
    write_buffer = (c_ubyte * 2)()
    read_buffer = (c_ubyte * 2)()
    write_buffer[0] = addr0
    write_buffer[1] = addr1
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 2)
    return read_buffer

def write_spi_reg(addr0,addr1,data):
    write_buffer = (c_ubyte * 3)()
    read_buffer = (c_ubyte * 2)()
    write_buffer[0] = addr0
    write_buffer[1] = addr1
    write_buffer[2] = data
    nRet = ControlSPI.VSI_WriteBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 3)










#####TP set
write_spi_reg(0x11,0x59,0x0e)
write_spi_reg(0x10,0x86,0x80)  ##CH0 DLL testpoint enabled
##write_spi_reg(0x10,0x86,0x90)  ##CH1 DLL testpoint enabled
##write_spi_reg(0x10,0x86,0xa0)  ##CH2 DLL testpoint enabled
##write_spi_reg(0x10,0x86,0xb0)  ##CH3 DLL testpoint enabled
##write_spi_reg(0x10,0x86,0xc0)  ##CH4 DLL testpoint enabled
##write_spi_reg(0x10,0x86,0xd0)  ##CH5 DLL testpoint enabled
##write_spi_reg(0x10,0x86,0xe0)  ##CH6 DLL testpoint enabled
##write_spi_reg(0x10,0x86,0xf0)  ##CH7 DLL testpoint enabled

write_spi_reg(0x10,0x93,0x08)      ##CH0 DLL test voltage, 8-f
##write_spi_reg(0x10,0x9d,0x08)  ##CH1 DLL test voltage, 8-f
##write_spi_reg(0x10,0xa7,0x08)  ##CH2 DLL test voltage, 8-f
##write_spi_reg(0x10,0xb1,0x08)  ##CH3 DLL test voltage, 8-f
##write_spi_reg(0x10,0xbb,0x08)  ##CH4 DLL test voltage, 8-f
##write_spi_reg(0x10,0xc5,0x08)  ##CH5 DLL test voltage, 8-f
##write_spi_reg(0x10,0xcf,0x08)   ##CH6 DLL test voltage, 8-f
##write_spi_reg(0x10,0xd9,0x08)  ##CH7 DLL test voltage, 8-f

