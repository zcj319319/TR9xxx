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
##TXDRV status: [7] PWD_PREC, [6] PWD_MC, [5] PWD_POST1C, [4] PWD_POST2C, [3] QRATE, [2] HRATE, [1] FRATE [0] TXREADY
read_spi_reg(0x11,0x6F)  ##CH0: TXDRV status
read_spi_reg(0x11,0x70)  ##CH1: TXDRV status
read_spi_reg(0x11,0x71)  ##CH2: TXDRV status
read_spi_reg(0x11,0x72)  ##CH3: TXDRV status
read_spi_reg(0x11,0x73)  ##CH4: TXDRV status
read_spi_reg(0x11,0x74)  ##CH5: TXDRV status
read_spi_reg(0x11,0x75)  ##CH6: TXDRV status
read_spi_reg(0x11,0x76)  ##CH7: TXDRV status

##DCCDLL status
read_spi_reg(0x11,0x5F)  ##CH0: DCCDLL status
read_spi_reg(0x11,0x60)  ##CH0: DCCDLL status
read_spi_reg(0x11,0x61)  ##CH1: DCCDLL status
read_spi_reg(0x11,0x62)  ##CH1: DCCDLL status
read_spi_reg(0x11,0x63)  ##CH2: DCCDLL status
read_spi_reg(0x11,0x64)  ##CH2: DCCDLL status
read_spi_reg(0x11,0x65)  ##CH3: DCCDLL status
read_spi_reg(0x11,0x66)  ##CH3: DCCDLL status
read_spi_reg(0x11,0x67)  ##CH4: DCCDLL status
read_spi_reg(0x11,0x68)  ##CH4: DCCDLL status
read_spi_reg(0x11,0x69)  ##CH5: DCCDLL status
read_spi_reg(0x11,0x6a)  ##CH5: DCCDLL status
read_spi_reg(0x11,0x6b)  ##CH6: DCCDLL status
read_spi_reg(0x11,0x6c)  ##CH6: DCCDLL status
read_spi_reg(0x11,0x6d)  ##CH7: DCCDLL status
read_spi_reg(0x11,0x6e)  ##CH7: DCCDLL status

## PLL status
read_spi_reg(0x11,0x77)  ##PLL status
read_spi_reg(0x11,0x78)  ##PLL status