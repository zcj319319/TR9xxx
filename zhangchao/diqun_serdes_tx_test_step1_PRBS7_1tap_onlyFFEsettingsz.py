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

####1-tap default settings####
####post1c and post2c weight
write_spi_reg(0x10,0x90,0x3c)         
write_spi_reg(0x10,0x9a,0x3c)
write_spi_reg(0x10,0xa4,0x3c)
write_spi_reg(0x10,0xae,0x3c)
write_spi_reg(0x10,0xb8,0x3c)
write_spi_reg(0x10,0xc2,0x3c)
write_spi_reg(0x10,0xcc,0x3c)
write_spi_reg(0x10,0xd6,0x3c)

####maincursor and precursor weight
write_spi_reg(0x10,0x8f,0xf4)
write_spi_reg(0x10,0x99,0xf4)
write_spi_reg(0x10,0xa3,0xf4)
write_spi_reg(0x10,0xad,0xf4)
write_spi_reg(0x10,0xb7,0xf4)
write_spi_reg(0x10,0xc1,0xf4)
write_spi_reg(0x10,0xcb,0xf4)
write_spi_reg(0x10,0xd5,0xf4)

####fine tune
write_spi_reg(0x10,0x8e,0x00)
write_spi_reg(0x10,0x98,0x00)
write_spi_reg(0x10,0xa2,0x00)
write_spi_reg(0x10,0xac,0x00)
write_spi_reg(0x10,0xb6,0x00)
write_spi_reg(0x10,0xc0,0x00)
write_spi_reg(0x10,0xca,0x00)
write_spi_reg(0x10,0xd4,0x00)
