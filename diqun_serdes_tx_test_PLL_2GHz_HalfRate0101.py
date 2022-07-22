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

write_spi_reg(0x10,0x7d,0x06)  ## refclk divider div 0x0c=24

write_spi_reg(0x11,0x46,0x28) ####
####PLL FBC divider by 60
write_spi_reg(0x11,0x48,0x10) ####div  by 24
##write_spi_reg(0x11,0x48,0x3c) ####div  by 60
##write_spi_reg(0x11,0x48,0x40) ####div by 64

####PLL settings
write_spi_reg(0x11,0x3a,0x10) ####AMP_CTRL[1:0],[5] Reserved,BY_SLLP,BY_Freq,BY_AMP,BY_PLL,SHORT_RC
write_spi_reg(0x11,0x3b,0xfd) ####AMP_CALI_DIVR[1:0],AMPD_SEL[2:0],AMP_CTRL[2:0]
write_spi_reg(0x11,0x3c,0x0e) #### FREQ_LOAD[[5:0],AMP_CALI_DIVR[3:2]  #0x02 by default.
write_spi_reg(0x11,0x3d,0x7d) #### FREQ_LOAD[13:6]
write_spi_reg(0x11,0x3e,0x90) #### FREQ_CALI_CNT2_SIZE[2:0],CNT1_SIZE[2:0],FREQ_LOAD[15:14]
write_spi_reg(0x11,0x3f,0x84) #### FREQ_CALI_STEP2_SIZE[0],STEP1_SIZE[6:0]
write_spi_reg(0x11,0x40,0x00) #### TEMP_BY_SLLP[1:0],FREQ_CALI_STEP2_SIZE[6:1]
write_spi_reg(0x11,0x41,0x00) #### TEMP_BY_SLLP[9:2]

write_spi_reg(0x11,0x45,0x10) #### IND SW, 0x50 VCO high speed. 0x10 vco low speed
write_spi_reg(0x11,0x46,0x2f) #### REF_DIVR[3:0],KVCO_SLOW,KVCO[2:0]
write_spi_reg(0x11,0x49,0x40) #### LPF Res[0]=0,LPF_C2[2:0]=4，FBC_DIVR[11:8]
write_spi_reg(0x11,0x4a,0x72) #### Enable post divider. ICP[2:0]=2,LPF_Res[1]=0,
#write_spi_reg(0x11,0x4a,0x56) #### Enable post divider. ICP[2:0]=3,LPF_Res[1]=0,

##DCCDLL setting from CH0 to CH7, calibration enable and dac enable
write_spi_reg(0x10,0x92,0x84)
write_spi_reg(0x10,0x9c,0x84)
write_spi_reg(0x10,0xa6,0x84)
write_spi_reg(0x10,0xb0,0x84)
write_spi_reg(0x10,0xba,0x84)
write_spi_reg(0x10,0xc4,0x84)
write_spi_reg(0x10,0xce,0x84)
write_spi_reg(0x10,0xd8,0x84)



####datarate 40-quarter rate,60-halfrate,70-fullrate
write_spi_reg(0x10,0x91,0x60)
write_spi_reg(0x10,0x9b,0x60)
write_spi_reg(0x10,0xa5,0x60)
write_spi_reg(0x10,0xaf,0x60)
write_spi_reg(0x10,0xb9,0x60)
write_spi_reg(0x10,0xc3,0x60)
write_spi_reg(0x10,0xcd,0x60)
write_spi_reg(0x10,0xd7,0x60)

###TXREADY bypass
write_spi_reg(0x10,0x87,0x04)
## pattern generator clk pattern
## 0x91: pattern 01010101
## 0x94: pattern 00110011
## 0x98: pattern 00001111
## 0x9c: pattern 0000000011111111
## pattern generator prbs7 pattern
## first set 0x80 then set 0xa0

write_spi_reg(0x10,0x8d,0x91)
write_spi_reg(0x10,0x97,0x91)
write_spi_reg(0x10,0xa1,0x91)
write_spi_reg(0x10,0xab,0x91)
write_spi_reg(0x10,0xb5,0x91)
write_spi_reg(0x10,0xbf,0x91)
write_spi_reg(0x10,0xc9,0x91)
write_spi_reg(0x10,0xd3,0x91)

##enable and reset 


write_spi_reg(0x10,0x89,0xf0)
write_spi_reg(0x10,0x89,0xf1)

####dccdll trigger
write_spi_reg(0x10,0xe3,0x02)
write_spi_reg(0x10,0xef,0x02)
write_spi_reg(0x10,0xfb,0x02)
write_spi_reg(0x11,0x07,0x02)
write_spi_reg(0x11,0x13,0x02)
write_spi_reg(0x11,0x1f,0x02)
write_spi_reg(0x11,0x2b,0x02)
write_spi_reg(0x11,0x37,0x02)

####toggle
write_spi_reg(0x10,0xe3,0x00)
write_spi_reg(0x10,0xef,0x00)
write_spi_reg(0x10,0xfb,0x00)
write_spi_reg(0x11,0x07,0x00)
write_spi_reg(0x11,0x13,0x00)
write_spi_reg(0x11,0x1f,0x00)
write_spi_reg(0x11,0x2b,0x00)
write_spi_reg(0x11,0x37,0x00)

####txready enable
write_spi_reg(0x10,0x87,0x0c)



#####TP set
##write_spi_reg(0x11,0x59,0x0e)
##write_spi_reg(0x10,0x86,0x80)
##write_spi_reg(0x10,0x89,0xf2)
##write_spi_reg(0x11,0x4a,0xd6)
##write_spi_reg(0x11,0x4b,0xa9)
##write_spi_reg(0x10,0x89,0xf3)

## pattern generator prbs7 pattern
##write_spi_reg(0x10,0x8d,0x80)
##write_spi_reg(0x10,0x97,0x80)
##write_spi_reg(0x10,0xa1,0x80)
##write_spi_reg(0x10,0xab,0x80)
##write_spi_reg(0x10,0xb5,0x80)
##write_spi_reg(0x10,0xbf,0x80)
##write_spi_reg(0x10,0xc9,0x80)
##write_spi_reg(0x10,0xd3,0x80)

##write_spi_reg(0x10,0x8d,0xa0)
##write_spi_reg(0x10,0x97,0xa0)
##write_spi_reg(0x10,0xa1,0xa0)
##write_spi_reg(0x10,0xab,0xa0)
##write_spi_reg(0x10,0xb5,0xa0)
##write_spi_reg(0x10,0xbf,0xa0)
##write_spi_reg(0x10,0xc9,0xa0)
##write_spi_reg(0x10,0xd3,0xa0)