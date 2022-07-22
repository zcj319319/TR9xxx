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
SPI_Init.ClockSpeed = 9000000;
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
    read_buffer = (c_ubyte * 1)()
    write_buffer[0] = addr0
    write_buffer[1] = addr1
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 1)
    return read_buffer

def write_spi_reg(addr0,addr1,data):
    write_buffer = (c_ubyte * 3)()
    read_buffer = (c_ubyte * 2)()
    write_buffer[0] = addr0
    write_buffer[1] = addr1
    write_buffer[2] = data
    nRet = ControlSPI.VSI_WriteBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 3)



####################################
### RX0 Registers

write_spi_reg(0x00,0x36,0XC2)
sleep(0.1)
write_spi_reg(0x00,0x36,0XC6)
write_spi_reg(0x00, 0x37, 0X0)

fp=open('bist_chk_error.txt','w')
deepth=1
for i in range(0, deepth):
    sleep(0.1)
    write_spi_reg(0x00, 0x37, 0X20)
    sleep(0.1)
    write_spi_reg(0x00, 0x37, 0X24)
    sleep(1)
    write_spi_reg(0x00, 0x37, 0X26)

    read_buffer=read_spi_reg(0x81, 0xE0)
    fp.write("Err_Counter_Val=%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xDF)
    fp.write("%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xDE)
    fp.write("%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xDD)
    fp.write("%02X\n" % (read_buffer[0]))

fp.close()

fp=open('bist_chk_error.txt','a')
deepth=5
for i in range(0, deepth):
    sleep(0.1)
    write_spi_reg(0x00, 0x14, 0X20)
    sleep(0.1)
    write_spi_reg(0x00, 0x14, 0X25)

    read_buffer=read_spi_reg(0x81, 0xCE)
    fp.write("dll0_dac_bin=%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xCF)
    fp.write("dll0_dac_the=%02X " % (read_buffer[0]))

    sleep(0.1)
    write_spi_reg(0x00, 0x24, 0X20)
    sleep(0.1)
    write_spi_reg(0x00, 0x24, 0X25)

    read_buffer=read_spi_reg(0x81, 0xD0)
    fp.write("dll1_dac_bin=%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xD1)
    fp.write("dll1_dac_the=%02X\n" % (read_buffer[0]))

fp.close()

fp=open('bist_chk_error.txt','a')
write_spi_reg(0x00, 0x28, 0X0)
read_buffer=read_spi_reg(0x81, 0xE1)
fp.write("slicer0_cali_result=%02X\n" % (read_buffer[0]))
sleep(0.01)
write_spi_reg(0x00, 0x28, 0X04)
read_buffer=read_spi_reg(0x81, 0xE1)
fp.write("slicer1_cali_result=%02X\n" % (read_buffer[0]))
sleep(0.01)
write_spi_reg(0x00, 0x28, 0X08)
read_buffer=read_spi_reg(0x81, 0xE1)
fp.write("slicer2_cali_result=%02X\n" % (read_buffer[0]))
sleep(0.01)
write_spi_reg(0x00, 0x28, 0X0C)
read_buffer=read_spi_reg(0x81, 0xE1)
fp.write("slicer3_cali_result=%02X\n" % (read_buffer[0]))
sleep(0.01)
write_spi_reg(0x00, 0x28, 0X10)
read_buffer=read_spi_reg(0x81, 0xE1)
fp.write("slicer4_cali_result=%02X\n" % (read_buffer[0]))
sleep(0.01)
write_spi_reg(0x00, 0x28, 0X14)
read_buffer=read_spi_reg(0x81, 0xE1)
fp.write("slicer5_cali_result=%02X\n" % (read_buffer[0]))
sleep(0.01)
write_spi_reg(0x00, 0x28, 0X18)
read_buffer=read_spi_reg(0x81, 0xE1)
fp.write("slicer6_cali_result=%02X\n" % (read_buffer[0]))
sleep(0.01)
write_spi_reg(0x00, 0x28, 0X1C)
read_buffer=read_spi_reg(0x81, 0xE1)
fp.write("slicer7_cali_result=%02X\n" % (read_buffer[0]))
fp.close()

### cdr accum status read
fp=open('bist_chk_error.txt','a')
deepth=5
for i in range(0, deepth):
    sleep(0.01)
    write_spi_reg(0x00, 0x2B, 0X20)
    sleep(0.01)
    write_spi_reg(0x00, 0x2B, 0X60)
    read_buffer=read_spi_reg(0x81, 0xD7)
    fp.write("cdr_i_accum_status=%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xD6)
    fp.write("%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xD5)
    fp.write("%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xD4)
    fp.write("%02X    " % (read_buffer[0]))

    sleep(0.01)
    write_spi_reg(0x00, 0x2B, 0X0)
    sleep(0.01)
    write_spi_reg(0x00, 0x2B, 0X40)
    read_buffer=read_spi_reg(0x81, 0xD7)
    fp.write("cdr_f_accum_status=%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xD6)
    fp.write("%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xD5)
    fp.write("%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xD4)
    fp.write("%02X\n" % (read_buffer[0]))

fp.close()



fp=open('bist_chk_error.txt','a')
deepth=5
for i in range(0, deepth):
    sleep(0.1)
    write_spi_reg(0x00, 0x36, 0XC2)
    sleep(0.1)
    write_spi_reg(0x00, 0x36, 0XCA)

    read_buffer=read_spi_reg(0x81, 0xD8)
    fp.write("UDP pattern=%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xD9)
    fp.write("%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xDA)
    fp.write("%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xDB)
    fp.write("%02X " % (read_buffer[0]))
    read_buffer=read_spi_reg(0x81, 0xDC)
    fp.write("%02X\n" % (read_buffer[0]))

fp.close()

