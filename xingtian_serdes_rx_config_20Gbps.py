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

####################################
#fp=open('bist_chk_error.txt','w')
### Top Registers
write_spi_reg(0x00,0x00,0x00)
write_spi_reg(0x00,0x01,0x1F)

####################################
### RX0 Registers
### demux resetn register is released.
write_spi_reg(0x00,0x36,0XC2)

write_spi_reg(0x00,0x38,0X7C)
sleep(0.5)
write_spi_reg(0x00,0x38,0XF4)

write_spi_reg(0x00,0x02,0x40)  ### According to measurement result, term register should be set to 0.
write_spi_reg(0x00,0x04,0x7F)
write_spi_reg(0x00,0x05,0x88)
write_spi_reg(0x00,0x06,0x01)
write_spi_reg(0x00,0x07,0xE)
write_spi_reg(0x00,0x08,0x0)

### dll0 gm overwrite enabled, gm_c is set to 101(1 - overwrite).
write_spi_reg(0x00,0x09,0x70)

### dll0 delay overwrite enabled, delay_c is set to 1111(1 - overwrite).
write_spi_reg(0x00,0x0A,0x1F)

write_spi_reg(0x00,0x0B,0x10)
write_spi_reg(0x00,0x0C,0x80)
write_spi_reg(0x00,0x0D,0x0F)
write_spi_reg(0x00,0x0E,0x0)
write_spi_reg(0x00,0x0F,0x0)
write_spi_reg(0x00,0x10,0X80)

### dcc0_ctrl_ow=1
write_spi_reg(0x00,0x11,0X88)

write_spi_reg(0x00,0x12,0X80)
write_spi_reg(0x00,0x13,0X80)

### dll0 state machine is triggered initially and then released.
write_spi_reg(0x00,0x14,0X60)
sleep(0.2)
write_spi_reg(0x00,0x14,0X20)
#sleep(0.2)
#write_spi_reg(0x00,0x14,0X25)  ### Read dll_dac_bin status

write_spi_reg(0x00,0x15,0X0)
write_spi_reg(0x00,0x16,0X24)
write_spi_reg(0x00,0x17,0X0F) ### Seems affecting RX function if test is enabled.
write_spi_reg(0x00,0x18,0X2)

### dll gm overwrite enabled, gm_c is set to 101(1 - overwrite).
write_spi_reg(0x00,0x19,0X70)

### dll1 delay overwrite enabled, delay_c is set to 1111(1 - overwrite).
write_spi_reg(0x00,0x1A,0X1F)

write_spi_reg(0x00,0x1B,0X10)
write_spi_reg(0x00,0x1C,0X80)
write_spi_reg(0x00,0x1D,0X0F)
write_spi_reg(0x00,0x1E,0X0)
write_spi_reg(0x00,0x1F,0X0)
write_spi_reg(0x00,0x20,0X80)

### dcc1_ctrl_ow=1
write_spi_reg(0x00,0x21,0X88)

write_spi_reg(0x00,0x22,0X80)
write_spi_reg(0x00,0x23,0X80)

### dll1 state machine is triggered initially and then released
write_spi_reg(0x00,0x24,0X60)
sleep(0.2)
write_spi_reg(0x00,0x24,0X20)

write_spi_reg(0x00,0x25,0X0)
write_spi_reg(0x00,0x26,0X24)
write_spi_reg(0x00,0x27,0X0)
write_spi_reg(0x00,0x28,0X2)

### CDR settings
write_spi_reg(0x00,0x29,0X02)
write_spi_reg(0x00,0x2A,0X00)

write_spi_reg(0x00,0x2B,0X0)
write_spi_reg(0x00,0x2C,0X0)
write_spi_reg(0x00,0x2D,0X0)
write_spi_reg(0x00,0x2E,0X0)

### slicer calibration reset_n=1
write_spi_reg(0x00,0x30,0X81)

write_spi_reg(0x00,0x31,0X60)

### Before slicer calibration, CTLE is temporarlly disabled.
write_spi_reg(0x00,0x03,0x82)

### slicer calibration trigger. Should return to 0 after calibration.
write_spi_reg(0x00,0x32,0X40)
sleep(0.2)
write_spi_reg(0x00,0x32,0X0)
sleep(1)

### After slicer calibration, CTLE is enabled.
write_spi_reg(0x00,0x03,0xF5)  ### F5 means ctle s1 r is set to the lowest.

write_spi_reg(0x00,0x33,0X0)
write_spi_reg(0x00,0x34,0X2)
write_spi_reg(0x00,0x35,0X0)

### CDR resetn is released.
write_spi_reg(0x00,0x2F,0X80)
print("CDR resetn is released.")
sleep(5)

### PRBS7 check enabled
write_spi_reg(0x00,0x36,0XC6)
sleep(0.2)
### Error counter initialization
write_spi_reg(0x00,0x37,0X0)
sleep(0.2)
### Error counter clear
write_spi_reg(0x00,0x37,0X20)
sleep(0.2)
### Error counter ready
write_spi_reg(0x00,0x37,0X24)
sleep(5)
### Read error counter value
write_spi_reg(0x00,0x37,0x26)
sleep(0.2)
read_buffer = read_spi_reg(0x81,0xdd)
print("addr(0x1dd)=%02x\n" % (read_buffer[0]))
read_buffer = read_spi_reg(0x81,0xde)
print("addr(0x1de)=%02x\n" % (read_buffer[0]))
read_buffer = read_spi_reg(0x81,0xdf)
print("addr(0x1df)=%02x\n" % (read_buffer[0]))
read_buffer = read_spi_reg(0x81,0xe0)
print("addr(0x1e0)=%02x\n" % (read_buffer[0]))

sleep(0.2)
### Error counter insert error
write_spi_reg(0x00,0x37,0x34)
sleep(0.2)
### Read error counter value again
write_spi_reg(0x00,0x37,0x36)
sleep(0.2)
read_buffer = read_spi_reg(0x81,0xdd)
print("addr(0x1dd)=%02x\n" % (read_buffer[0]))
read_buffer = read_spi_reg(0x81,0xde)
print("addr(0x1de)=%02x\n" % (read_buffer[0]))
read_buffer = read_spi_reg(0x81,0xdf)
print("addr(0x1df)=%02x\n" % (read_buffer[0]))
read_buffer = read_spi_reg(0x81,0xe0)
print("addr(0x1e0)=%02x\n" % (read_buffer[0]))






####################################
### RX3 Registers
write_spi_reg(0x00,0xDD,0X7C)
sleep(0.5)
write_spi_reg(0x00,0xDD,0XF4)

write_spi_reg(0x00,0xA7,0X70)  ### term vcm set to 11 (0.75V)
write_spi_reg(0x00,0xA9,0X7F)
write_spi_reg(0x00,0xAA,0X88)
write_spi_reg(0x00,0xAB,0X1)  ### ctle s2 current setting
write_spi_reg(0x00,0xAC,0XE)
write_spi_reg(0x00,0xAD,0X0)

### RX3 dll0 gm overwrite enabled, gm_c is set to 101(1 - overwrite).
write_spi_reg(0x00,0xAE,0XB0)

### RX3 dll0 delay overwrite enabled, delay_c is set to 1111(1 - overwrite).
write_spi_reg(0x00,0xAF,0X1F)
write_spi_reg(0x00,0xB0,0X10)
write_spi_reg(0x00,0xB1,0X80)
write_spi_reg(0x00,0xB2,0X0)
write_spi_reg(0x00,0xB3,0X0)
write_spi_reg(0x00,0xB4,0X0)
write_spi_reg(0x00,0xB5,0X80)

### RX3 dcc0_ctrl_ow=1
write_spi_reg(0x00,0xB6,0X88)

write_spi_reg(0x00,0xB7,0X80)
write_spi_reg(0x00,0xB8,0X80)

### RX3 dll0 state machine is triggered initially and then released
write_spi_reg(0x00,0xB9,0X60)
sleep(0.2)
write_spi_reg(0x00,0xB9,0X20)

write_spi_reg(0x00,0xBA,0X0)
write_spi_reg(0x00,0xBB,0X24)
write_spi_reg(0x00,0xBC,0X01)
write_spi_reg(0x00,0xBD,0X2)

### RX3 dll1 gm overwrite enabled, gm_c is set to 101(1 - overwrite).
write_spi_reg(0x00,0xBE,0Xb0)

### RX3 dll1 delay overwrite enabled, delay_c is set to 1111(1 - overwrite).
write_spi_reg(0x00,0xBF,0X1F)

write_spi_reg(0x00,0xC0,0X10)
write_spi_reg(0x00,0xC1,0X80)
write_spi_reg(0x00,0xC2,0X0)
write_spi_reg(0x00,0xC3,0X0)
write_spi_reg(0x00,0xC4,0X0)
write_spi_reg(0x00,0xC5,0X80)

### RX3 dcc1_ctrl_ow=1
write_spi_reg(0x00,0xC6,0X88)

write_spi_reg(0x00,0xC7,0X80)
write_spi_reg(0x00,0xC8,0X80)

### RX3 dll1 state machine is triggered initially and then released
write_spi_reg(0x00,0xC9,0X60)
sleep(0.2)
write_spi_reg(0x00,0xC9,0X20)

write_spi_reg(0x00,0xCA,0X0)
write_spi_reg(0x00,0xCB,0X24)
write_spi_reg(0x00,0xCC,0X0)
write_spi_reg(0x00,0xCD,0X2)
write_spi_reg(0x00,0xCE,0X2)
write_spi_reg(0x00,0xCF,0X0)
write_spi_reg(0x00,0xD0,0X0)
write_spi_reg(0x00,0xD1,0X0)
write_spi_reg(0x00,0xD2,0X0)
write_spi_reg(0x00,0xD3,0X0)
write_spi_reg(0x00,0xD4,0X80)

### RX3 slicer calibration reset_n=1
write_spi_reg(0x00,0xD5,0X81)

write_spi_reg(0x00,0xD6,0X20)

### Before slicer calibration, CTLE is temporarlly disabled.
write_spi_reg(0x00,0xA8,0X82)

### RX3 slicer calibration trigger. Should return to 0 after calibration.
write_spi_reg(0x00,0xD7,0X40)
sleep(0.2)
write_spi_reg(0x00,0xD7,0X0)
sleep(0.5)

### After slicer calibration, CTLE is enabled.
write_spi_reg(0x00,0xA8,0xF5)

write_spi_reg(0x00,0xD8,0X0)
write_spi_reg(0x00,0xD9,0X2)
write_spi_reg(0x00,0xDA,0X0)

### PRBS check disabled
write_spi_reg(0x00,0xDB,0XC2)

sleep(0.2)
### PRBS7 check enabled
write_spi_reg(0x00,0xDB,0XC6)

### Error counter initialization
write_spi_reg(0x00,0xDC,0X0)
sleep(0.2)
### Error counter clear
write_spi_reg(0x00,0xDC,0X20)
sleep(0.2)
### Error counter ready
write_spi_reg(0x00,0xDC,0X24)
sleep(5)
### Read error counter value
write_spi_reg(0x00,0xDC,0x26)





### PLL registers
write_spi_reg(0x01,0xba,0X00)
write_spi_reg(0x01,0xbb,0X14)
write_spi_reg(0x01,0xbc,0Xff)
write_spi_reg(0x01,0xbd,0X0f)
write_spi_reg(0x01,0xbe,0X00)
write_spi_reg(0x01,0xbf,0X00)
write_spi_reg(0x01,0xc0,0X00)
write_spi_reg(0x01,0xc1,0X00)
write_spi_reg(0x01,0xc2,0X00)
write_spi_reg(0x01,0xc3,0X10)
write_spi_reg(0x01,0xc4,0X0e)

### PLL REG11[7] - 1 Internal PLL clock for SerDes, 0 - Internal PLL for SerDes disabled.
write_spi_reg(0x01,0xc5,0X00)