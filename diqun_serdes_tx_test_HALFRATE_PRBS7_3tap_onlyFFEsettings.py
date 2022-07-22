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

##### to test PLL clock

####datarate 40-quarter rate,60-halfrate,70-fullrate
####2-tap: 3, 3-tap: 4, 4-tap: 8
write_spi_reg(0x10,0x91,0x64)
write_spi_reg(0x10,0x91,0x64)
write_spi_reg(0x10,0x9b,0x64)
write_spi_reg(0x10,0xa5,0x64)
write_spi_reg(0x10,0xaf,0x64)
write_spi_reg(0x10,0xb9,0x64)
write_spi_reg(0x10,0xc3,0x64)
write_spi_reg(0x10,0xcd,0x64)
write_spi_reg(0x10,0xd7,0x64)

####3-tap default settings####
####post1c and post2c weight
write_spi_reg(0x10,0x90,0x3f)
write_spi_reg(0x10,0x9a,0x3f)
write_spi_reg(0x10,0xa4,0x3f)
write_spi_reg(0x10,0xae,0x3f)
write_spi_reg(0x10,0xb8,0x3f)
write_spi_reg(0x10,0xc2,0x3f)
write_spi_reg(0x10,0xcc,0x3f)
write_spi_reg(0x10,0xd6,0x3f)

####maincursor and precursor weight
write_spi_reg(0x10,0x8f,0xb2)
write_spi_reg(0x10,0x99,0xb2)
write_spi_reg(0x10,0xa3,0xb2)
write_spi_reg(0x10,0xad,0xb2)
write_spi_reg(0x10,0xb7,0xb2)
write_spi_reg(0x10,0xc1,0xb2)
write_spi_reg(0x10,0xcb,0xb2)
write_spi_reg(0x10,0xd5,0xb2)

####fine tune
write_spi_reg(0x10,0x8e,0x00)
write_spi_reg(0x10,0x98,0x00)
write_spi_reg(0x10,0xa2,0x00)
write_spi_reg(0x10,0xac,0x00)
write_spi_reg(0x10,0xb6,0x00)
write_spi_reg(0x10,0xc0,0x00)
write_spi_reg(0x10,0xca,0x00)
write_spi_reg(0x10,0xd4,0x00)

## pattern generator clk pattern
## 0x91: pattern 01010101
## 0x94: pattern 00110011
## 0x98: pattern 00001111
## 0x9c: pattern 0000000011111111
## pattern generator prbs7 pattern
## first set 0x80 then set 0xa0

write_spi_reg(0x10,0x8d,0x80)
write_spi_reg(0x10,0x97,0x80)
write_spi_reg(0x10,0xa1,0x80)
write_spi_reg(0x10,0xab,0x80)
write_spi_reg(0x10,0xb5,0x80)
write_spi_reg(0x10,0xbf,0x80)
write_spi_reg(0x10,0xc9,0x80)
write_spi_reg(0x10,0xd3,0x80)

write_spi_reg(0x10,0x8d,0xa0)
write_spi_reg(0x10,0x97,0xa0)
write_spi_reg(0x10,0xa1,0xa0)
write_spi_reg(0x10,0xab,0xa0)
write_spi_reg(0x10,0xb5,0xa0)
write_spi_reg(0x10,0xbf,0xa0)
write_spi_reg(0x10,0xc9,0xa0)
write_spi_reg(0x10,0xd3,0xa0)