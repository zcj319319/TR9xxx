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

use_4g=0;
only_test_serdes_prbs7=0;




import os
os.system('D:\projects\DIQUN\write\zhangchao\zanalog_set.py')
sleep(0.5)


if use_4g == 1:
    os.system('D:\projects\DIQUN\write\zhangchao\diqun_serdes_tx_test_PLL_4GHz_HalfRate0101z.py')
else:
    os.system('D:\projects\DIQUN\write\zhangchao\diqun_serdes_tx_test_PLL_8GHz_HalfRate0101z.py')


sleep(0.5)
os.system('D:\projects\DIQUN\write\zhangchao\diqun_serdes_tx_test_step1_PRBS7_1tap_onlyFFEsettingsz.py')
sleep(0.5)
if use_4g == 1:
    os.system('D:\projects\DIQUN\write\zhangchao\diqun_serdes_tx_test_step2_PRBS7_FULLRATE_1TAPz0.py')
else:
    os.system('D:\projects\DIQUN\write\zhangchao\diqun_serdes_tx_test_step2_PRBS7_HALFRATE_1TAPz.py')

sleep(0.5)

if only_test_serdes_prbs7==1:
    os.system('D:\projects\DIQUN\write\zhangchao\diqun_serdes_tx_test_step3_PRBS7z.py')
else:
    write_spi_reg(0x10,0x8d,0x00)#serdes send normal data
    write_spi_reg(0x10,0x97,0x00)
    write_spi_reg(0x10,0xa1,0x00)
    write_spi_reg(0x10,0xab,0x00)
    write_spi_reg(0x10,0xb5,0x00)
    write_spi_reg(0x10,0xbf,0x00)
    write_spi_reg(0x10,0xc9,0x00)
    write_spi_reg(0x10,0xd3,0x00)

    write_spi_reg(0x10, 0x00, 0x00)#reset dig
    write_spi_reg(0x10, 0x00, 0x03)
#analog config ends






#ddc config begins
    ddc_nco_bypass = 1 # use nco test data , not adc source
    if ddc_nco_bypass == 1:
        write_spi_reg(0x03,0x27,0x00)
        write_spi_reg(0x02,0x00,0x01)
        write_spi_reg(0x03,0x10,0x37)
        write_spi_reg(0x03,0x11,0xf4)
        write_spi_reg(0x03,0x16,0x00)
        write_spi_reg(0x03,0x17,0x55)
        write_spi_reg(0x03,0x18,0x55)
        write_spi_reg(0x03,0x19,0x55)
        write_spi_reg(0x03,0x1a,0x55)
        write_spi_reg(0x03,0x1b,0x00)

    ddc_test_bypass = 0# is ramp, not sin
    if ddc_test_bypass == 1:
        write_spi_reg(0x03, 0x27, 0x07)
        write_spi_reg(0x02, 0x00, 0x00)
        write_spi_reg(0x03, 0x10, 0x10)
        write_spi_reg(0x03, 0x11, 0x04)
        write_spi_reg(0x05, 0x50, 0x0f)
        write_spi_reg(0x05, 0x50, 0x0f)
        write_spi_reg(0x03, 0x10, 0x37)
        write_spi_reg(0x03, 0x11, 0xf4)
#ddc config end







#204b config begins
    write_spi_reg(0x05, 0xf9, 0x00)#sysref_came_delay
    if use_4g == 1:
        write_spi_reg(0x0f, 0x0d, 0x08)#204b clk div
    else:
        write_spi_reg(0x0f, 0x0d, 0x02)#204b clk div
    write_spi_reg(0x05, 0x72, 0x00)
    write_spi_reg(0x05, 0x8b, 0x87)#scr/l_reg
    write_spi_reg(0x05, 0x8e, 0x01)#m_reg
    write_spi_reg(0x05, 0x8c, 0x01)#f_reg
    write_spi_reg(0x05, 0x91, 0x03)#s_reg
    write_spi_reg(0x05, 0x8d, 0x1f)#k_reg
    write_spi_reg(0x05, 0x8f, 0x0f)#n_reg
    write_spi_reg(0x05, 0x90, 0x0f)#n_total_reg
    write_spi_reg(0x05, 0xe4, 0x40)
    write_spi_reg(0x05, 0xb2, 0x45)#lane cross
    write_spi_reg(0x05, 0xb3, 0x76)
    write_spi_reg(0x05, 0xb5, 0x03)
    write_spi_reg(0x05, 0xb6, 0x12)
    write_spi_reg(0x05, 0x77, 0x00)#serdes test pattern



    write_spi_reg(0x05, 0x71, 0x05)  # long_test, enablemodule
