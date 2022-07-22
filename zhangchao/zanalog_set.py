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

##### to test PLL clock


write_spi_reg(0x10,0x79,0x6a)
write_spi_reg(0x10,0x7C,0x31)
write_spi_reg(0x10,0x01,0x01)
write_spi_reg(0x10,0x03,0x50)
write_spi_reg(0x10,0x03,0x53)
write_spi_reg(0x10,0x06,0x01)
write_spi_reg(0x10,0x08,0x03)
write_spi_reg(0x10,0x08,0x83)
write_spi_reg(0x10,0x0b,0x01)
write_spi_reg(0x10,0x0d,0x50)
write_spi_reg(0x10,0x0d,0x53)
write_spi_reg(0x10,0x10,0x01)
write_spi_reg(0x10,0x12,0x03)
write_spi_reg(0x10,0x12,0x83)
write_spi_reg(0x10,0x15,0x01)
write_spi_reg(0x10,0x17,0x50)
write_spi_reg(0x10,0x17,0x53)
write_spi_reg(0x10,0x1a,0x01)
write_spi_reg(0x10,0x1c,0x03)
write_spi_reg(0x10,0x1c,0x83)
write_spi_reg(0x10,0x1f,0x01)
write_spi_reg(0x10,0x21,0x50)
write_spi_reg(0x10,0x21,0x53)
write_spi_reg(0x10,0x24,0x01)
write_spi_reg(0x10,0x26,0x03)
write_spi_reg(0x10,0x26,0x83)
write_spi_reg(0x10,0x35,0x20)
write_spi_reg(0x10,0x35,0x28)
write_spi_reg(0x10,0x3D,0x01)
write_spi_reg(0x10,0x3F,0x50)
write_spi_reg(0x10,0x3F,0x53)
write_spi_reg(0x10,0x42,0x01)
write_spi_reg(0x10,0x44,0x03)
write_spi_reg(0x10,0x44,0x83)
write_spi_reg(0x10,0x47,0x01)
write_spi_reg(0x10,0x49,0x50)
write_spi_reg(0x10,0x49,0x53)
write_spi_reg(0x10,0x4C,0x01)
write_spi_reg(0x10,0x4E,0x03)
write_spi_reg(0x10,0x4E,0x83)
write_spi_reg(0x10,0x51,0x01)
write_spi_reg(0x10,0x53,0x50)
write_spi_reg(0x10,0x53,0x53)
write_spi_reg(0x10,0x56,0x01)
write_spi_reg(0x10,0x58,0x03)
write_spi_reg(0x10,0x58,0x83)
write_spi_reg(0x10,0x5B,0x01)
write_spi_reg(0x10,0x5D,0x50)
write_spi_reg(0x10,0x5D,0x53)
write_spi_reg(0x10,0x60,0x01)
write_spi_reg(0x10,0x62,0x03)
write_spi_reg(0x10,0x62,0x83)
write_spi_reg(0x10,0x71,0x20)
write_spi_reg(0x10,0x71,0x28)
write_spi_reg(0x10,0x7a,0x43)
write_spi_reg(0x10,0x80,0x00)
#write_spi_reg(0x10,0x85,0x01)#virtual sysref, to open dig clock
#write_spi_reg(0x10,0x85,0x03)
write_spi_reg(0x10,0x81,0xff)