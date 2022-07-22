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



##DCCDLL setting from CH0 to CH7, calibration enable and dac enable
write_spi_reg(0x10,0x92,0x84)
write_spi_reg(0x10,0x9c,0x84)
write_spi_reg(0x10,0xa6,0x84)
write_spi_reg(0x10,0xb0,0x84)
write_spi_reg(0x10,0xba,0x84)
write_spi_reg(0x10,0xc4,0x84)
write_spi_reg(0x10,0xce,0x84)
write_spi_reg(0x10,0xd8,0x84)

##DCCDLL overwrite
write_spi_reg(0x10,0xdf,0x0f)  ##CH0: reg_dll_accum_bit
write_spi_reg(0x10,0xeb,0x0f)  ##CH1: reg_dll_accum_bit
write_spi_reg(0x10,0xf7,0x0f)  ##CH2: reg_dll_accum_bit
write_spi_reg(0x11,0x03,0x0f)  ##CH3: reg_dll_accum_bit
write_spi_reg(0x11,0x0f,0x0f)  ##CH4: reg_dll_accum_bit
write_spi_reg(0x11,0x1b,0x0f)  ##CH5: reg_dll_accum_bit
write_spi_reg(0x11,0x27,0x0f)  ##CH6: reg_dll_accum_bit
write_spi_reg(0x11,0x33,0x0f)  ##CH7: reg_dll_accum_bit

write_spi_reg(0x10,0xe0,0xc0)  ##CH0: reg_dll_gm_ov, delay_ow
write_spi_reg(0x10,0xec,0xc0)  ##CH1: reg_dll_gm_ov, delay_ow
write_spi_reg(0x10,0xf8,0xc0)  ##CH2: reg_dll_gm_ov, delay_ow
write_spi_reg(0x11,0x04,0xc0)  ##CH3: reg_dll_gm_ov, delay_ow
write_spi_reg(0x11,0x10,0xc0)  ##CH4: reg_dll_gm_ov, delay_ow
write_spi_reg(0x11,0x1c,0xc0)  ##CH5: reg_dll_gm_ov, delay_ow
write_spi_reg(0x11,0x28,0xc0)  ##CH6: reg_dll_gm_ov, delay_ow
write_spi_reg(0x11,0x34,0xc0)  ##CH7: reg_dll_gm_ov, delay_ow

###write_spi_reg(0x10,0xe1,0x6f)  ##CH0: reg_dll_go_on, reg_dll_gm_c, reg_dll_delay_c
write_spi_reg(0x10,0xe1,0x2f)  ##CH0: reg_dll_go_on, reg_dll_gm_c, reg_dll_delay_c
write_spi_reg(0x10,0xed,0x2f)  ##CH1: reg_dll_go_on, reg_dll_gm_c, reg_dll_delay_c
write_spi_reg(0x10,0xf9,0x2f)  ##CH2: reg_dll_go_on, reg_dll_gm_c, reg_dll_delay_c
write_spi_reg(0x11,0x05,0x2f)  ##CH3: reg_dll_go_on, reg_dll_gm_c, reg_dll_delay_c
write_spi_reg(0x11,0x11,0x2f)  ##CH4: reg_dll_go_on, reg_dll_gm_c, reg_dll_delay_c
write_spi_reg(0x11,0x1d,0x2f)  ##CH5: reg_dll_go_on, reg_dll_gm_c, reg_dll_delay_c
write_spi_reg(0x11,0x29,0x2f)  ##CH6: reg_dll_go_on, reg_dll_gm_c, reg_dll_delay_c
write_spi_reg(0x11,0x35,0x2f)  ##CH7: reg_dll_go_on, reg_dll_gm_c, reg_dll_delay_c

####dccdll trigger
write_spi_reg(0x10,0xe3,0x02)
write_spi_reg(0x10,0xef,0x02)
write_spi_reg(0x10,0xfb,0x02)
write_spi_reg(0x11,0x07,0x02)
write_spi_reg(0x11,0x13,0x02)
write_spi_reg(0x11,0x1f,0x02)
write_spi_reg(0x11,0x2b,0x02)
write_spi_reg(0x11,0x37,0x02)
sleep(1)
####toggle
write_spi_reg(0x10,0xe3,0x00)
write_spi_reg(0x10,0xef,0x00)
write_spi_reg(0x10,0xfb,0x00)
write_spi_reg(0x11,0x07,0x00)
write_spi_reg(0x11,0x13,0x00)
write_spi_reg(0x11,0x1f,0x00)
write_spi_reg(0x11,0x2b,0x00)
write_spi_reg(0x11,0x37,0x00)

write_spi_reg(0x10,0xe5,0x02)
write_spi_reg(0x10,0xe5,0x0a)
read_buffer = read_spi_reg(0x91, 0x5F)
print("dll_dac_bin val=%02X " % (read_buffer[0]))