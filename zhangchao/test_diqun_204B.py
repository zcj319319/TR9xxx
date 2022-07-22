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

fold_all_mode=1;

test_serdes_prbs7=1;
test_digana_prbs15=0;#test point is above phy, but in serdes clk domain, dig ana interface is included,serdes fifo is not included

test_1611_dcm4=0;
test_1611_dcm5=0;
test_1611_dcm6=0;
test_1611_dcm8=0;
test_1611_dcm10=0;
test_1611_dcm12=0;
test_1611_dcm16=0;
test_1611_dcm20=0;
test_1611_dcm24=0;
test_1612=0;
test_1613_dcm2=0;
test_1613_dcm3=0;
test_1613_dcm6=0;
test_1614=0;
test_1615_dcm1=0;
test_1615_dcm2=0;
test_1615_dcm3=0;
test_1616=0;
test_1617_dcm1=0;
test_1617_dcm2=0;
test_1617_dcm3=0;
test_1618=0;
test_1621_dcm8=0;
test_1621_dcm12=0;
test_1621_dcm20=0;
test_1622=0;
test_1623_dcm4=0;
test_1623_dcm6=0;
test_1623_dcm8=0;
test_1624=0;
test_1625_dcm2=0;
test_1625_dcm3=0;
test_1625_dcm5=0;
test_1626=0;
test_1627_dcm1=0;
test_1627_dcm2=0;
test_1627_dcm3=0;
test_1628=1;#full speed mode
test_1628_dcm4=0;
test_fsx4=0;
test_1628_cbit=0;
test_1641_dcm16=0;
test_1641_dcm24=0;
test_1641_dcm40=0;
test_1642_dcm8=0;
test_1642_dcm12=0;
test_1642_dcm16=0;
test_1643=0;
test_1644_dcm4=0;
test_1644_dcm6=0;
test_1644_dcm8=0;
test_1645=0;
test_1646_dcm2=0;
test_1646_dcm3=0;
test_1646_dcm4=0;
test_1647=0;
test_1681_dcm48=0;
test_1682_dcm16=0;
test_1682_dcm24=0;
test_1682_dcm40=0;
test_1683_dcm8=0;
test_1683_dcm12=0;
test_1683_dcm16=0;
test_1684=0;
test_1685_dcm4=0;
test_1685_dcm6=0;
test_1685_dcm8=0;
test_1686=0;
test_1211_dcm3=0;
test_1211_dcm6=0;
test_1212_dcm3=0;
test_1212_dcm6=0;
test_1213_dcm3=0;
test_1214_dcm1=0;
test_1214_dcm2=0;
test_1214_dcm3=0;
test_1221_dcm6=0;
test_1221_dcm12=0;
test_1221_dcm24=0;
test_1222_dcm3=0;
test_1222_dcm6=0;
test_1222_dcm12=0;
test_1223_dcm2=0;
test_1223_dcm3=0;
test_1223_dcm4=0;
test_1224_dcm3=0;
test_1224_dcm6=0;
test_1241_dcm12=0;
test_1241_dcm24=0;
test_1241_dcm48=0;
test_1242_dcm6=0;
test_1242_dcm12=0;
test_1242_dcm24=0;
test_1243_dcm4=0;
test_1243_dcm6=0;
test_1243_dcm8=0;
test_1244_dcm3=0;
test_1244_dcm6=0;
test_1244_dcm12=0;
test_1281_dcm12=0;
test_1281_dcm24=0;
test_1281_dcm48=0;
test_1282_dcm6=0;
test_1282_dcm12=0;
test_1282_dcm24=0;
test_0811_dcm2=0;
test_0811_dcm3=0;
test_0811_dcm4=0;
test_0812=0;
test_0813_dcm1=0;
test_0813_dcm2=0;
test_0813_dcm3=0;
test_0814=0;
test_0815=0;
test_0816_dcm1=0;
test_0816_dcm2=0;
test_0817=0;

test_0821_dcm4=0;
test_0821_dcm6=0;
test_0821_dcm8=0;
test_0822_dcm2=0;
test_0822_dcm3=0;
test_0822_dcm4=0;
test_0823=0;
test_0824_dcm1=0;
test_0824_dcm2=0;
test_0824_dcm3=0;
test_0825=0;
test_0826=0;



import os

####basic analog set
os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\zanalog_set.py')
#write_spi_reg(0x10, 0x85, 0x01)  ## fake sysref
#write_spi_reg(0x10, 0x85, 0x03)  ## fake sysref
sleep(0.5)



#serdes lane rate setting
if fold_all_mode == 1:
    if test_1628 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1611_dcm4 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10,0x7d,0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11,0x48,0x3c) ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1611_dcm5 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x30)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1611_dcm6 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10,0x7d,0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11,0x48,0x28) ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1611_dcm8 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10,0x7d,0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11,0x48,0x3C) ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1611_dcm10 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10,0x7d,0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11,0x48,0x30) ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1611_dcm12 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1611_dcm16 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')

    if test_1611_dcm20 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x30)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')

    if test_1611_dcm24 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')

    if test_fsx4 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10,0x7d,0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11,0x48,0x30) ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1612 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1613_dcm2 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1613_dcm3 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1613_dcm6 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1614 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1615_dcm1 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1615_dcm2 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1615_dcm3 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1616 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1617_dcm1 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1617_dcm2 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')


    if test_1617_dcm3 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')


    if test_1618 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1621_dcm8 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1621_dcm12 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1621_dcm20 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x30)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1622 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1623_dcm4 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1623_dcm6 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1623_dcm8 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1624 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1625_dcm2 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1625_dcm3 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1625_dcm5 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x30)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1626 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1627_dcm1 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1627_dcm2 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1627_dcm3 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1628_dcm4 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')


    if test_1628_cbit == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')



    if test_1641_dcm16 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1641_dcm24 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1641_dcm40 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x30)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')



    if test_1642_dcm8 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1642_dcm12 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1642_dcm16== 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1643== 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1644_dcm4== 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1644_dcm6== 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1644_dcm8== 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1645== 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1646_dcm2== 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1646_dcm3 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1646_dcm4 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1647 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1681_dcm48 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1682_dcm16 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1682_dcm24 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1682_dcm40 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x30)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1683_dcm8 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1683_dcm12 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1683_dcm16 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')



    if test_1684 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1685_dcm4 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')



    if test_1685_dcm6 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1685_dcm8 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')



    if test_1686 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1211_dcm3 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1211_dcm6 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1212_dcm3 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1212_dcm6 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')


    if test_1213_dcm3 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1214_dcm1 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1214_dcm2 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1214_dcm3 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1221_dcm6 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1221_dcm12 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')



    if test_1221_dcm24 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')


    if test_1222_dcm3 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1222_dcm6 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1222_dcm12 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')


    if test_1223_dcm2 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1223_dcm3 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1223_dcm4 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1224_dcm3 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1224_dcm6 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')


    if test_1241_dcm12 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1241_dcm24 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1241_dcm48 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')


    if test_1242_dcm6 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')



    if test_1242_dcm12 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')



    if test_1242_dcm24 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')


    if test_1243_dcm4 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1243_dcm6 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1243_dcm8 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')



    if test_1244_dcm3 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')



    if test_1244_dcm6 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1244_dcm12 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')


    if test_1281_dcm12 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1281_dcm24 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1281_dcm48 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')


    if test_1282_dcm6 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_1282_dcm12 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_1282_dcm24 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')

    if test_0811_dcm2 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_0811_dcm3 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_0811_dcm4 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_0812 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_0813_dcm1 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_0813_dcm2 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_0813_dcm3 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_0814 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_0815 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_0816_dcm1 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_0816_dcm2 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4minus.py')


    if test_0817 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_0821_dcm4 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_0821_dcm6 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_0821_dcm8 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')



    if test_0822_dcm2 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_0822_dcm3 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')



    if test_0822_dcm4 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_0823 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_0824_dcm1 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_0824_dcm2 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_0824_dcm3 == 1:
        use_full_rate = 1;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x28)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')


    if test_0825 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')

    if test_0826 == 1:
        use_full_rate = 0;
        write_spi_reg(0x10, 0x7d, 0x0C)  ## refclk divider div 0x0c=24
        write_spi_reg(0x11, 0x48, 0x3c)  ######PLL FBC divider by 0x3c=60
        os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_PLL_lane4plus.py')
sleep(0.5)
if use_full_rate == 1:
    os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_step2_PRBS7_FULLRATE_1TAPz.py')
else:
    os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_step2_PRBS7_HALFRATE_1TAPz.py')
sleep(0.5)


####### ffe setting
os.system('D:\projects\DIQUN\diqun_fpga\write\zhangchao\diqun_serdes_tx_test_step1_PRBS7_1tap_onlyFFEsettingsz.py')
sleep(0.5)




if test_serdes_prbs7==1:
    write_spi_reg(0x10, 0x8d, 0x80)
    write_spi_reg(0x10, 0x97, 0x80)
    write_spi_reg(0x10, 0xa1, 0x80)
    write_spi_reg(0x10, 0xab, 0x80)
    write_spi_reg(0x10, 0xb5, 0x80)
    write_spi_reg(0x10, 0xbf, 0x80)
    write_spi_reg(0x10, 0xc9, 0x80)
    write_spi_reg(0x10, 0xd3, 0x80)
    sleep(1)
    write_spi_reg(0x10, 0x8d, 0xa0)
    write_spi_reg(0x10, 0x97, 0xa0)
    write_spi_reg(0x10, 0xa1, 0xa0)
    write_spi_reg(0x10, 0xab, 0xa0)
    write_spi_reg(0x10, 0xb5, 0xa0)
    write_spi_reg(0x10, 0xbf, 0xa0)
    write_spi_reg(0x10, 0xc9, 0xa0)
    write_spi_reg(0x10, 0xd3, 0xa0)
else:
    write_spi_reg(0x10,0x8d,0x00)#serdes send normal data
    write_spi_reg(0x10,0x97,0x00)
    write_spi_reg(0x10,0xa1,0x00)
    write_spi_reg(0x10,0xab,0x00)
    write_spi_reg(0x10,0xb5,0x00)
    write_spi_reg(0x10,0xbf,0x00)
    write_spi_reg(0x10,0xc9,0x00)
    write_spi_reg(0x10,0xd3,0x00)
#analog config ends
write_spi_reg(0x10, 0x00, 0x00)#reset dig
write_spi_reg(0x10, 0x00, 0x03)




#sysref,crg configuration and stablizing wait
write_spi_reg(0x0f, 0x31, 0x08)  # [0]:jitter filter en, [2]:force root sysref to 0.
if fold_all_mode ==1 :
    if test_1611_dcm4 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)  # 204b clk div
    if test_1611_dcm5 == 1:
        write_spi_reg(0x0f, 0x0d, 0x05)  # 204b clk div
        write_spi_reg(0x0f, 0x0a, 0x01)  # 5/2 clock; divmult2_en
    if test_1611_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03)  # 204b clk div
    if test_1611_dcm8 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04)  # 204b clk div
    if test_1611_dcm10 == 1:
        write_spi_reg(0x0f, 0x0d, 0x05)  # 204b clk div
    if test_1611_dcm12 == 1:
        write_spi_reg(0x0f, 0x0d, 0x06)  # 204b clk div
    if test_1611_dcm16 == 1:
        write_spi_reg(0x0f, 0x0d, 0x08)  # 204b clk div
    if test_1611_dcm20 == 1:
        write_spi_reg(0x0f, 0x0d, 0x0a)  # 204b clk div
    if test_1611_dcm24 == 1:
        write_spi_reg(0x0f, 0x0d, 0x0c)  # 204b clk div
    if test_1612 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)#204b clk div
    if test_1613_dcm2 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)#204b clk div
    if test_1613_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03)#204b clk div
    if test_1613_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x06)#204b clk div
    if test_1614 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)#204b clk div
    if test_1615_dcm1 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)#204b clk div
    if test_1615_dcm2 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04)#204b clk div
    if test_1615_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x06)#204b clk div
    if test_1616 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)#204b clk div
    if test_1617_dcm1 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04)#204b clk div
    if test_1617_dcm2 == 1:
        write_spi_reg(0x0f, 0x0d, 0x08)#204b clk div
    if test_1617_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x0c)#204b clk div
    if test_1618 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04)#204b clk div
    if test_1621_dcm8 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)#204b clk div
    if test_1621_dcm12 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03)#204b clk div
    if test_1621_dcm20 == 1:
        write_spi_reg(0x0f, 0x0d, 0x05)#204b clk div
    if test_1622 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)#204b clk div
    if test_1623_dcm4 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)#204b clk div
    if test_1623_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03)#204b clk div
    if test_1623_dcm8 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04)#204b clk div
    if test_1624 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)#204b clk div
    if test_1625_dcm2 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)#204b clk div
    if test_1625_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03)#204b clk div
    if test_1625_dcm5 == 1:
        write_spi_reg(0x0f, 0x0d, 0x05)#204b clk div
    if test_1626 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)#204b clk div
    if test_1627_dcm1 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)#204b clk div
    if test_1627_dcm2 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04)#204b clk div
    if test_1627_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x06)#204b clk div
    if test_1628 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1628_dcm4 == 1:
        write_spi_reg(0x0f, 0x0d, 0x08) #204b clk div
    if test_fsx4 == 1:
        write_spi_reg(0x0f, 0x0d, 0x05)# 204b clk div
    if test_1628_cbit == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1641_dcm16 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1641_dcm24 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03) #204b clk div
    if test_1641_dcm40 == 1:
        write_spi_reg(0x0f, 0x0d, 0x05) #204b clk div
    if test_1642_dcm8 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1642_dcm12 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03) #204b clk div
    if test_1642_dcm16 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1643 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1644_dcm4 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1644_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03) #204b clk div
    if test_1644_dcm8 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1645 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1646_dcm2 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1646_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03) #204b clk div
    if test_1646_dcm4 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1647 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1681_dcm48 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03) #204b clk div
    if test_1682_dcm16 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1682_dcm24 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03) #204b clk div
    if test_1682_dcm40 == 1:
        write_spi_reg(0x0f, 0x0d, 0x05) #204b clk div
    if test_1683_dcm8 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1683_dcm12 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03) #204b clk div
    if test_1683_dcm16 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1684 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1685_dcm4 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1685_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03) #204b clk div
    if test_1685_dcm8 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1686 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1211_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1211_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1212_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1212_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x08) #204b clk div
    if test_1213_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1214_dcm1 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1214_dcm2 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1214_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x06) #204b clk div
    if test_1221_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1221_dcm12 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1221_dcm24 == 1:
        write_spi_reg(0x0f, 0x0d, 0x08) #204b clk div
    if test_1222_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1222_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1222_dcm12== 1:
        write_spi_reg(0x0f, 0x0d, 0x08) #204b clk div
    if test_1223_dcm2 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1223_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03) #204b clk div
    if test_1223_dcm4 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1224_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1224_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x08) #204b clk div
    if test_1241_dcm12 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1241_dcm24 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1241_dcm48 == 1:
        write_spi_reg(0x0f, 0x0d, 0x08) #204b clk div
    if test_1242_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1242_dcm12 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1242_dcm24 == 1:
        write_spi_reg(0x0f, 0x0d, 0x08) #204b clk div
    if test_1243_dcm4 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1243_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03) #204b clk div
    if test_1243_dcm8 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1244_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_1244_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_1244_dcm12 == 1:
        write_spi_reg(0x0f, 0x0d, 0x08) #204b clk div
    if test_1281_dcm12 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)  # 204b clk div
    if test_1281_dcm24 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04)  # 204b clk div
    if test_1281_dcm48 == 1:
        write_spi_reg(0x0f, 0x0d, 0x08)  # 204b clk div
    if test_1282_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)  # 204b clk div
    if test_1282_dcm12 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04)  # 204b clk div
    if test_1282_dcm24 == 1:
        write_spi_reg(0x0f, 0x0d, 0x08)  # 204b clk div
    if test_0811_dcm2 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_0811_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03) #204b clk div
    if test_0811_dcm4 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_0812 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_0813_dcm1 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_0813_dcm2 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_0813_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x06) #204b clk div
    if test_0814 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_0815 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02) #204b clk div
    if test_0816_dcm1 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04) #204b clk div
    if test_0816_dcm2 == 1:
        write_spi_reg(0x0f, 0x0d, 0x08)  # 204b clk div
    if test_0817 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04)  # 204b clk div
    if test_0821_dcm4 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)  # 204b clk div
    if test_0821_dcm6 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03)  # 204b clk div
    if test_0821_dcm8 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04)  # 204b clk div
    if test_0822_dcm2 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)  # 204b clk div
    if test_0822_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x03)  # 204b clk div
    if test_0822_dcm4 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04)  # 204b clk div
    if test_0823 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)  # 204b clk div
    if test_0824_dcm1 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)  # 204b clk div
    if test_0824_dcm2 == 1:
        write_spi_reg(0x0f, 0x0d, 0x04)  # 204b clk div
    if test_0824_dcm3 == 1:
        write_spi_reg(0x0f, 0x0d, 0x06)  # 204b clk div
    if test_0825 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)  # 204b clk div
    if test_0826 == 1:
        write_spi_reg(0x0f, 0x0d, 0x02)  # 204b clk div


#ddc config begins
ddc_nco_bypass = 1 # use nco test data , not adc source
if ddc_nco_bypass == 1:
    write_spi_reg(0x03, 0x16, 0x00)#nco 0
    write_spi_reg(0x03, 0x17, 0x55)
    write_spi_reg(0x03, 0x18, 0x55)
    write_spi_reg(0x03, 0x19, 0x55)
    write_spi_reg(0x03, 0x1a, 0x55)
    write_spi_reg(0x03, 0x1b, 0x00)

    write_spi_reg(0x03, 0x36, 0x00)#nco 1
    write_spi_reg(0x03, 0x37, 0x55)
    write_spi_reg(0x03, 0x38, 0x55)
    write_spi_reg(0x03, 0x39, 0x55)
    write_spi_reg(0x03, 0x3a, 0x55)
    write_spi_reg(0x03, 0x3b, 0x00)

    write_spi_reg(0x03, 0x56, 0x00)#nco 2
    write_spi_reg(0x03, 0x57, 0x55)
    write_spi_reg(0x03, 0x58, 0x55)
    write_spi_reg(0x03, 0x59, 0x55)
    write_spi_reg(0x03, 0x5a, 0x55)
    write_spi_reg(0x03, 0x5b, 0x00)

    write_spi_reg(0x03, 0x76, 0x00)#nco 3
    write_spi_reg(0x03, 0x77, 0x55)
    write_spi_reg(0x03, 0x78, 0x55)
    write_spi_reg(0x03, 0x79, 0x55)
    write_spi_reg(0x03, 0x7a, 0x55)
    write_spi_reg(0x03, 0x7b, 0x00)

    write_spi_reg(0x03,0x27,0x00)
    if fold_all_mode ==1 :
        if test_1611_dcm4 == 1:#m and dcm
            write_spi_reg(0x03, 0x10, 0x30)#dcm
            write_spi_reg(0x02, 0x00, 0x01)#m
        if test_1611_dcm5 == 1:  # m and dcm
            write_spi_reg(0x03, 0x10, 0x37)  # dcm 5
            write_spi_reg(0x03, 0x11, 0xa0)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1611_dcm6 == 1:#m and dcm
            write_spi_reg(0x03, 0x10, 0x34)#dcm 6
            write_spi_reg(0x02, 0x00, 0x01)#m
        if test_1611_dcm8 == 1:#m and dcm
            write_spi_reg(0x03, 0x10, 0x31)#dcm 8
            write_spi_reg(0x02, 0x00, 0x01)#m
        if test_1611_dcm10 == 1:#m and dcm
            write_spi_reg(0x03, 0x10, 0x37)#dcm 10
            write_spi_reg(0x03, 0x11, 0x20)  #
            write_spi_reg(0x02, 0x00, 0x01)#m
        if test_1611_dcm12 == 1:  # m and dcm
            write_spi_reg(0x03, 0x10, 0x35)  # dcm 12
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1611_dcm16 == 1:  # m and dcm
            write_spi_reg(0x03, 0x10, 0x32)  # dcm 16
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1611_dcm20 == 1:  # m and dcm
            write_spi_reg(0x03, 0x10, 0x37)  # dcm
            write_spi_reg(0x03, 0x11, 0x30)  # dcm 20
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1611_dcm24 == 1:  # m and dcm
            write_spi_reg(0x03, 0x10, 0x36)  # dcm 24
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1612 == 1:
            write_spi_reg(0x03, 0x10, 0x30)
            write_spi_reg(0x02, 0x00, 0x01)#m
        if test_1613_dcm2 == 1:
            write_spi_reg(0x03, 0x10, 0x33)
            write_spi_reg(0x02, 0x00, 0x01)#m
        if test_1613_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)
            write_spi_reg(0x03, 0x11, 0x70)
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1613_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1614 == 1:
            write_spi_reg(0x03, 0x10, 0x33)
            write_spi_reg(0x02, 0x00, 0x01)#m
        if test_1615_dcm1 == 1:
            write_spi_reg(0x03, 0x10, 0x37)
            write_spi_reg(0x03, 0x11, 0xf4)
            write_spi_reg(0x02, 0x00, 0x01)#m
        if test_1615_dcm2 == 1:
            write_spi_reg(0x03, 0x10, 0x33)
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1615_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)
            write_spi_reg(0x03, 0x11, 0x74)
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1616 == 1:
            write_spi_reg(0x03, 0x10, 0x37)
            write_spi_reg(0x03, 0x11, 0xf4)
            write_spi_reg(0x02, 0x00, 0x01)#m

        if test_1617_dcm1 == 1:
            write_spi_reg(0x03, 0x10, 0x37)
            write_spi_reg(0x03, 0x11, 0xf4)
            write_spi_reg(0x02, 0x00, 0x01)#m

        if test_1617_dcm2 == 1:
            write_spi_reg(0x03, 0x10, 0x33)
            write_spi_reg(0x02, 0x00, 0x01)#m

        if test_1617_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)
            write_spi_reg(0x03, 0x11, 0x74)
            write_spi_reg(0x02, 0x00, 0x01)#m

        if test_1618 == 1:
            write_spi_reg(0x03, 0x10, 0x37)
            write_spi_reg(0x03, 0x11, 0xf4)
            write_spi_reg(0x02, 0x00, 0x01)#m

        if test_1621_dcm8 == 1:
            write_spi_reg(0x03, 0x10, 0x31)
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1621_dcm12 == 1:
            write_spi_reg(0x03, 0x10, 0x35)
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1621_dcm20 == 1:
            write_spi_reg(0x03, 0x10, 0x37)
            write_spi_reg(0x03, 0x11, 0x30)
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1622 == 1:
            write_spi_reg(0x03, 0x10, 0x31)
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1623_dcm4 == 1:
            write_spi_reg(0x03, 0x10, 0x30)#dcm
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1623_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)#dcm
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1623_dcm8 == 1:
            write_spi_reg(0x03, 0x10, 0x31)#dcm
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1624 == 1:
            write_spi_reg(0x03, 0x10, 0x30)  # dcm
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1625_dcm2 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  # dcm
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1625_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm
            write_spi_reg(0x03, 0x11, 0x74)  # dcm
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1625_dcm5 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm
            write_spi_reg(0x03, 0x11, 0xa0)  # dcm
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1626 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  # dcm
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1627_dcm1 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm=1
            write_spi_reg(0x03, 0x11, 0xf4)  # dcm=1
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1627_dcm2 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1627_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1628 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm=1
            write_spi_reg(0x03, 0x11, 0xf4)  # dcm=1
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_1628_dcm4 == 1:
            write_spi_reg(0x03, 0x10, 0x30)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_fsx4 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm=1
            write_spi_reg(0x03, 0x11, 0xf4)  # dcm=1
            write_spi_reg(0x02, 0x00, 0x00)  # m
        if test_1628_cbit == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm=1
            write_spi_reg(0x03, 0x11, 0xf4)  # dcm=1
            write_spi_reg(0x02, 0x00, 0x00)  # m
        if test_1641_dcm16 == 1:#iq相位差1
            write_spi_reg(0x03, 0x10, 0x32)  # dcm=16
            write_spi_reg(0x03, 0x30, 0x32)  # dcm=16
            write_spi_reg(0x02, 0x00, 0x02)  # m
        if test_1641_dcm24 == 1:
            write_spi_reg(0x03, 0x10, 0x36)  # dcm
            write_spi_reg(0x03, 0x30, 0x36)  # dcm
            write_spi_reg(0x02, 0x00, 0x02)  # m
        if test_1641_dcm40 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm
            write_spi_reg(0x03, 0x11, 0x44)  # dcm
            write_spi_reg(0x03, 0x30, 0x37)  # dcm
            write_spi_reg(0x03, 0x31, 0x44)  # dcm
            write_spi_reg(0x02, 0x00, 0x02)  # m
        if test_1642_dcm8 == 1:
            write_spi_reg(0x03, 0x10, 0x31)  # dcm=8
            write_spi_reg(0x03, 0x30, 0x31)  # dcm=8
            write_spi_reg(0x02, 0x00, 0x02)  # m

        if test_1642_dcm12 == 1:
            write_spi_reg(0x03, 0x10, 0x35)  #
            write_spi_reg(0x03, 0x30, 0x35)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m

        if test_1642_dcm16 == 1:
            write_spi_reg(0x03, 0x10, 0x32)  #
            write_spi_reg(0x03, 0x30, 0x32)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m

        if test_1643 == 1:
            write_spi_reg(0x03, 0x10, 0x31)  # dcm=8
            write_spi_reg(0x03, 0x30, 0x31)  # dcm=8
            write_spi_reg(0x02, 0x00, 0x02)  # m
        if test_1644_dcm4 == 1:
            write_spi_reg(0x03, 0x10, 0x30)  # dcm=4
            write_spi_reg(0x03, 0x30, 0x30)  # dcm=4
            write_spi_reg(0x02, 0x00, 0x02)  # m
        if test_1644_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)  # dcm
            write_spi_reg(0x03, 0x30, 0x34)  # dcm
            write_spi_reg(0x02, 0x00, 0x02)  # m
        if test_1644_dcm8 == 1:
            write_spi_reg(0x03, 0x10, 0x31)  # dcm
            write_spi_reg(0x03, 0x30, 0x31)  # dcm
            write_spi_reg(0x02, 0x00, 0x02)  # m

        if test_1645 == 1:
            write_spi_reg(0x03, 0x10, 0x30)  # dcm=4
            write_spi_reg(0x03, 0x30, 0x30)  # dcm=4
            write_spi_reg(0x02, 0x00, 0x02)  # m

        if test_1646_dcm2 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  # dcm=2
            write_spi_reg(0x03, 0x30, 0x33)  # dcm=2
            write_spi_reg(0x02, 0x00, 0x02)  # m

        if test_1646_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x03, 0x30, 0x37)  #
            write_spi_reg(0x03, 0x31, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m

        if test_1646_dcm4 == 1:
            write_spi_reg(0x03, 0x10, 0x30)  #
            write_spi_reg(0x03, 0x30, 0x30)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m
        if test_1647 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  # dcm=2
            write_spi_reg(0x03, 0x30, 0x33)  # dcm=2
            write_spi_reg(0x02, 0x00, 0x02)  # m
        if test_1681_dcm48 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x04)  #
            write_spi_reg(0x03, 0x30, 0x37)  #
            write_spi_reg(0x03, 0x31, 0x04)  #
            write_spi_reg(0x03, 0x50, 0x37)  #
            write_spi_reg(0x03, 0x51, 0x04)  #
            write_spi_reg(0x03, 0x70, 0x37)  #
            write_spi_reg(0x03, 0x71, 0x04)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m


        if test_1682_dcm16 == 1:
            write_spi_reg(0x03, 0x10, 0x32)  # dcm=16
            write_spi_reg(0x03, 0x30, 0x32)  #
            write_spi_reg(0x03, 0x50, 0x32)  #
            write_spi_reg(0x03, 0x70, 0x32)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m

        if test_1682_dcm24 == 1:
            write_spi_reg(0x03, 0x10, 0x36)  #
            write_spi_reg(0x03, 0x30, 0x36)  #
            write_spi_reg(0x03, 0x50, 0x36)  #
            write_spi_reg(0x03, 0x70, 0x36)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m


        if test_1682_dcm40 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x44)  #
            write_spi_reg(0x03, 0x30, 0x37)  #
            write_spi_reg(0x03, 0x31, 0x44)  #
            write_spi_reg(0x03, 0x50, 0x37)  #
            write_spi_reg(0x03, 0x51, 0x44)  #
            write_spi_reg(0x03, 0x70, 0x37)  #
            write_spi_reg(0x03, 0x71, 0x44)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m



        if test_1683_dcm8 == 1:
            write_spi_reg(0x03, 0x10, 0x31)  # dcm=8
            write_spi_reg(0x03, 0x30, 0x31)  #
            write_spi_reg(0x03, 0x50, 0x31)  #
            write_spi_reg(0x03, 0x70, 0x31)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m

        if test_1683_dcm12 == 1:
            write_spi_reg(0x03, 0x10, 0x35)  #
            write_spi_reg(0x03, 0x30, 0x35)  #
            write_spi_reg(0x03, 0x50, 0x35)  #
            write_spi_reg(0x03, 0x70, 0x35)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m


        if test_1683_dcm16 == 1:
            write_spi_reg(0x03, 0x10, 0x32)  #
            write_spi_reg(0x03, 0x30, 0x32)  #
            write_spi_reg(0x03, 0x50, 0x32)  #
            write_spi_reg(0x03, 0x70, 0x32)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m


        if test_1684 == 1:
            write_spi_reg(0x03, 0x10, 0x31)  # dcm=8
            write_spi_reg(0x03, 0x30, 0x31)  #
            write_spi_reg(0x03, 0x50, 0x31)  #
            write_spi_reg(0x03, 0x70, 0x31)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m


        if test_1685_dcm4 == 1:
            write_spi_reg(0x03, 0x10, 0x30)  # dcm=4
            write_spi_reg(0x03, 0x30, 0x30)  #
            write_spi_reg(0x03, 0x50, 0x30)  #
            write_spi_reg(0x03, 0x70, 0x30)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m

        if test_1685_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)  #
            write_spi_reg(0x03, 0x30, 0x34)  #
            write_spi_reg(0x03, 0x50, 0x34)  #
            write_spi_reg(0x03, 0x70, 0x34)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m

        if test_1685_dcm8 == 1:
            write_spi_reg(0x03, 0x10, 0x31)  #
            write_spi_reg(0x03, 0x30, 0x31)  #
            write_spi_reg(0x03, 0x50, 0x31)  #
            write_spi_reg(0x03, 0x70, 0x31)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m

        if test_1686 == 1:
            write_spi_reg(0x03, 0x10, 0x30)  # dcm=4
            write_spi_reg(0x03, 0x30, 0x30)  #
            write_spi_reg(0x03, 0x50, 0x30)  #
            write_spi_reg(0x03, 0x70, 0x30)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m

        if test_1211_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1211_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1212_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1212_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_1213_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1214_dcm1 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm=1
            write_spi_reg(0x03, 0x11, 0xf4)  # dcm=1
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1214_dcm2 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1214_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_1221_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_1221_dcm12 == 1:
            write_spi_reg(0x03, 0x10, 0x35)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_1221_dcm24 == 1:
            write_spi_reg(0x03, 0x10, 0x36)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_1222_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_1222_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_1222_dcm12 == 1:
            write_spi_reg(0x03, 0x10, 0x35)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_1223_dcm2 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  # dcm=2
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1223_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_1223_dcm4 == 1:
            write_spi_reg(0x03, 0x10, 0x30)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_1224_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_1224_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_1241_dcm12 == 1:
            write_spi_reg(0x03, 0x10, 0x35)  #
            write_spi_reg(0x03, 0x30, 0x35)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m


        if test_1241_dcm24 == 1:
            write_spi_reg(0x03, 0x10, 0x36)  #
            write_spi_reg(0x03, 0x30, 0x36)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m


        if test_1241_dcm48 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x04)  #
            write_spi_reg(0x03, 0x30, 0x37)  #
            write_spi_reg(0x03, 0x31, 0x04)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m


        if test_1242_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)  #
            write_spi_reg(0x03, 0x30, 0x34)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m


        if test_1242_dcm12 == 1:
            write_spi_reg(0x03, 0x10, 0x35)  #
            write_spi_reg(0x03, 0x30, 0x35)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m


        if test_1242_dcm24 == 1:
            write_spi_reg(0x03, 0x10, 0x36)  #
            write_spi_reg(0x03, 0x30, 0x36)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m



        if test_1243_dcm4 == 1:
            write_spi_reg(0x03, 0x10, 0x30)  # dcm=4
            write_spi_reg(0x03, 0x30, 0x30)  # dcm=4
            write_spi_reg(0x02, 0x00, 0x02)  # m

        if test_1243_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)  #
            write_spi_reg(0x03, 0x30, 0x34)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m

        if test_1243_dcm8 == 1:
            write_spi_reg(0x03, 0x10, 0x31)  #
            write_spi_reg(0x03, 0x30, 0x31)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m

        if test_1244_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x03, 0x30, 0x37)  #
            write_spi_reg(0x03, 0x31, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m


        if test_1244_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)  #
            write_spi_reg(0x03, 0x30, 0x34)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m


        if test_1244_dcm12 == 1:
            write_spi_reg(0x03, 0x10, 0x35)  #
            write_spi_reg(0x03, 0x30, 0x35)  #
            write_spi_reg(0x02, 0x00, 0x02)  # m


        if test_1281_dcm12 == 1:
            write_spi_reg(0x03, 0x10, 0x35)  #
            write_spi_reg(0x03, 0x30, 0x35)  #
            write_spi_reg(0x03, 0x50, 0x35)  #
            write_spi_reg(0x03, 0x70, 0x35)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m



        if test_1281_dcm24 == 1:
            write_spi_reg(0x03, 0x10, 0x36)  #
            write_spi_reg(0x03, 0x30, 0x36)  #
            write_spi_reg(0x03, 0x50, 0x36)  #
            write_spi_reg(0x03, 0x70, 0x36)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m



        if test_1281_dcm48 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x04)  #
            write_spi_reg(0x03, 0x30, 0x37)  #
            write_spi_reg(0x03, 0x31, 0x04)  #
            write_spi_reg(0x03, 0x50, 0x37)  #
            write_spi_reg(0x03, 0x51, 0x04)  #
            write_spi_reg(0x03, 0x70, 0x37)  #
            write_spi_reg(0x03, 0x71, 0x04)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m

        if test_1282_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)  #
            write_spi_reg(0x03, 0x30, 0x34)  #
            write_spi_reg(0x03, 0x50, 0x34)  #
            write_spi_reg(0x03, 0x70, 0x34)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m


        if test_1282_dcm12 == 1:
            write_spi_reg(0x03, 0x10, 0x35)  #
            write_spi_reg(0x03, 0x30, 0x35)  #
            write_spi_reg(0x03, 0x50, 0x35)  #
            write_spi_reg(0x03, 0x70, 0x35)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m


        if test_1282_dcm24 == 1:
            write_spi_reg(0x03, 0x10, 0x36)  #
            write_spi_reg(0x03, 0x30, 0x36)  #
            write_spi_reg(0x03, 0x50, 0x36)  #
            write_spi_reg(0x03, 0x70, 0x36)  #
            write_spi_reg(0x02, 0x00, 0x03)  # m


        if test_0811_dcm2 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  # dcm=2
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0811_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0811_dcm4 == 1:
            write_spi_reg(0x03, 0x10, 0x30)
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0812 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  # dcm=2
            write_spi_reg(0x02, 0x00, 0x01)  # m



        if test_0813_dcm1 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm=1
            write_spi_reg(0x03, 0x11, 0xf4)  # dcm=1
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0813_dcm2 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0813_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0814 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm=1
            write_spi_reg(0x03, 0x11, 0xf4)  # dcm=1
            write_spi_reg(0x02, 0x00, 0x01)  # m
        if test_0815 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm=1
            write_spi_reg(0x03, 0x11, 0xf4)  # dcm=1
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0816_dcm1 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm=1
            write_spi_reg(0x03, 0x11, 0xf4)  # dcm=1
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0816_dcm2 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0817 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm=1
            write_spi_reg(0x03, 0x11, 0xf4)  # dcm=1
            write_spi_reg(0x02, 0x00, 0x01)  # m



        if test_0821_dcm4 == 1:
            write_spi_reg(0x03, 0x10, 0x30)  # dcm=4
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_0821_dcm6 == 1:
            write_spi_reg(0x03, 0x10, 0x34)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0821_dcm8 == 1:
            write_spi_reg(0x03, 0x10, 0x31)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0822_dcm2 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  # dcm=2
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0822_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_0822_dcm4 == 1:
            write_spi_reg(0x03, 0x10, 0x30)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_0823 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  # dcm=2
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0824_dcm1 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm=1
            write_spi_reg(0x03, 0x11, 0xf4)  # dcm=1
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0824_dcm2 == 1:
            write_spi_reg(0x03, 0x10, 0x33)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_0824_dcm3 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  #
            write_spi_reg(0x03, 0x11, 0x74)  #
            write_spi_reg(0x02, 0x00, 0x01)  # m


        if test_0825 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm=1
            write_spi_reg(0x03, 0x11, 0xf4)  # dcm=1
            write_spi_reg(0x02, 0x00, 0x01)  # m

        if test_0826 == 1:
            write_spi_reg(0x03, 0x10, 0x37)  # dcm=1
            write_spi_reg(0x03, 0x11, 0xf4)  # dcm=1
            write_spi_reg(0x02, 0x00, 0x01)  # m

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

write_spi_reg(0x03, 0x00, 0x10)#reset nco
write_spi_reg(0x03, 0x00, 0x00)
#ddc config end
sleep(0.1)# Reserve some time for ddc to get stable. Non-stable valid will harm down stream 204b permanently





#204b config begins
if fold_all_mode ==1 :
    if test_1611_dcm4 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1611_dcm5 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1611_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1611_dcm8 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length


    if test_1611_dcm10 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length


    if test_1611_dcm12 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length


    if test_1611_dcm16 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1611_dcm20 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1611_dcm24 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1612 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)#m_reg
        write_spi_reg(0x05, 0x8c, 0x03)#f_reg
        write_spi_reg(0x05, 0x91, 0x01)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length

    if test_1613_dcm2 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1613_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1613_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1614 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)#m_reg
        write_spi_reg(0x05, 0x8c, 0x01)#f_reg
        write_spi_reg(0x05, 0x91, 0x01)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1615_dcm1 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x01)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1615_dcm2 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x01)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1615_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x01)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1616 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)#m_reg
        write_spi_reg(0x05, 0x8c, 0x01)#f_reg
        write_spi_reg(0x05, 0x91, 0x03)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1617_dcm1 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x03)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1617_dcm2 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x03)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length


    if test_1617_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x03)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1618 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)#m_reg
        write_spi_reg(0x05, 0x8c, 0x01)#f_reg
        write_spi_reg(0x05, 0x91, 0x07)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1621_dcm8 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x03)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length

    if test_1621_dcm12 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x03)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length

    if test_1621_dcm20 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x03)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length

    if test_1622 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x07)#f_reg
        write_spi_reg(0x05, 0x91, 0x01)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x00)#multiframe length
        write_spi_reg(0x05, 0xe5, 0x01)#multiframe length

    if test_1623_dcm4 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x01)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length


    if test_1623_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x01)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1623_dcm8 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x01)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1624 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x03)#f_reg
        write_spi_reg(0x05, 0x91, 0x01)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length

    if test_1625_dcm2 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1625_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1625_dcm5 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1626 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x01)#f_reg
        write_spi_reg(0x05, 0x91, 0x01)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1627_dcm1 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x01)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1627_dcm2 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x01)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length


    if test_1627_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x00)#f_reg
        write_spi_reg(0x05, 0x91, 0x01)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length


    if test_1628 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x01)#f_reg
        write_spi_reg(0x05, 0x91, 0x03)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length


    if test_1628_dcm4 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x01)#f_reg
        write_spi_reg(0x05, 0x91, 0x03)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_fsx4 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x01)#f_reg
        write_spi_reg(0x05, 0x91, 0x03)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)#n_reg
        write_spi_reg(0x05, 0x90, 0x0f)#n_total_reg
        write_spi_reg(0x05, 0x70, 0xfe)#enable fsx4 mode in ddc
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1628_cbit == 1:
        write_spi_reg(0x05, 0x8b, 0x87)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)#m_reg
        write_spi_reg(0x05, 0x8c, 0x01)#f_reg
        write_spi_reg(0x05, 0x91, 0x03)#s_reg
        write_spi_reg(0x05, 0x8f, 0x8c)# cs_number,n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0x59, 0x25)  # cbit:0 means 0;1 overrange; 2 sig mon, 3 fd , 5 sysref pedge
        write_spi_reg(0x02, 0x70, 0x00)  # sigmon en. in mpw, you dont enable it and can see 01111111
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length


    if test_1641_dcm16 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)#m_reg
        write_spi_reg(0x05, 0x8c, 0x07)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x00)#multiframe length
        write_spi_reg(0x05, 0xe5, 0x01)#multiframe length

    if test_1641_dcm24 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)#m_reg
        write_spi_reg(0x05, 0x8c, 0x07)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x00)#multiframe length
        write_spi_reg(0x05, 0xe5, 0x01)#multiframe length

    if test_1641_dcm40 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)#m_reg
        write_spi_reg(0x05, 0x8c, 0x07)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x00)#multiframe length
        write_spi_reg(0x05, 0xe5, 0x01)#multiframe length

    if test_1642_dcm8 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)#m_reg
        write_spi_reg(0x05, 0x8c, 0x03)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length

    if test_1642_dcm12 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)#m_reg
        write_spi_reg(0x05, 0x8c, 0x03)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length


    if test_1642_dcm16 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)#m_reg
        write_spi_reg(0x05, 0x8c, 0x03)#f_reg
        write_spi_reg(0x05, 0x91, 0x00)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length


    if test_1643 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)#scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)#m_reg
        write_spi_reg(0x05, 0x8c, 0x07)#f_reg
        write_spi_reg(0x05, 0x91, 0x01)#s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)# n_reg
        write_spi_reg(0x05, 0x90, 0x0f)# n_total_reg
        write_spi_reg(0x05, 0xe4, 0x00)#multiframe length
        write_spi_reg(0x05, 0xe5, 0x01)#multiframe length

    if test_1644_dcm4 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1644_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length


    if test_1644_dcm8 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_1645 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x03)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length

    if test_1646_dcm2 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length


    if test_1646_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length


    if test_1646_dcm4 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1647 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1681_dcm48 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x0f)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x00)#multiframe length
        write_spi_reg(0x05, 0xe5, 0x02)#multiframe length

    if test_1682_dcm16 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x07)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x00)#multiframe length
        write_spi_reg(0x05, 0xe5, 0x01)#multiframe length

    if test_1682_dcm24 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x07)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x00)#multiframe length
        write_spi_reg(0x05, 0xe5, 0x01)#multiframe length

    if test_1682_dcm40 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x07)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x00)#multiframe length
        write_spi_reg(0x05, 0xe5, 0x01)#multiframe length

    if test_1683_dcm8 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x03)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length

    if test_1683_dcm12 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x03)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length


    if test_1683_dcm16 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x03)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length


    if test_1684 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x07)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x00)#multiframe length
        write_spi_reg(0x05, 0xe5, 0x01)#multiframe length


    if test_1685_dcm4 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length


    if test_1685_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length


    if test_1685_dcm8 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length


    if test_1686 == 1:
        write_spi_reg(0x05, 0x8b, 0x87)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x03)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0f)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0f)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length


    if test_1211_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1211_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1212_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x03)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1212_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x03)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1213_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x05)  # f_reg
        write_spi_reg(0x05, 0x91, 0x07)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0xc0)#multiframe length


    if test_1214_dcm1 == 1:
        write_spi_reg(0x05, 0x8b, 0x82)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_1214_dcm2 == 1:
        write_spi_reg(0x05, 0x8b, 0x82)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length


    if test_1214_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x82)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length


    if test_1221_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1221_dcm12 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1221_dcm24 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1222_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1222_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1222_dcm12== 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length




    if test_1223_dcm2 == 1:
        write_spi_reg(0x05, 0x8b, 0x82)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length


    if test_1223_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x82)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length


    if test_1223_dcm4 == 1:
        write_spi_reg(0x05, 0x8b, 0x82)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length


    if test_1224_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x03)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1224_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x03)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1241_dcm12 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x05)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0xc0)#multiframe length


    if test_1241_dcm24 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x05)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0xc0)#multiframe length


    if test_1241_dcm48 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x05)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0xc0)#multiframe length


    if test_1242_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1242_dcm12 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length



    if test_1242_dcm24 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length





    if test_1243_dcm4 == 1:
        write_spi_reg(0x05, 0x8b, 0x82)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length



    if test_1243_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x82)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length



    if test_1243_dcm8 == 1:
        write_spi_reg(0x05, 0x8b, 0x82)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length



    if test_1244_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1244_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1244_dcm12 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x03)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length

    if test_1281_dcm12 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x05)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0xc0)#multiframe length


    if test_1281_dcm24 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x05)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0xc0)#multiframe length


    if test_1281_dcm48 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x05)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0xc0)#multiframe length


    if test_1282_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1282_dcm12 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_1282_dcm24 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x07)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x02)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x0b)  # n_reg
        write_spi_reg(0x05, 0x90, 0x0b)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x60)#multiframe length


    if test_0811_dcm2 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_0811_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_0811_dcm4 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_0812 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_0813_dcm1 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_0813_dcm2 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_0813_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_0814 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x03)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_0815 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x03)  # f_reg
        write_spi_reg(0x05, 0x91, 0x07)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length


    if test_0816_dcm1 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x03)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_0816_dcm2 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x03)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_0817 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x00)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x07)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_0821_dcm4 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length


    if test_0821_dcm6 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length


    if test_0821_dcm8 == 1:
        write_spi_reg(0x05, 0x8b, 0x80)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length


    if test_0822_dcm2 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_0822_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length


    if test_0822_dcm4 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length



    if test_0823 == 1:
        write_spi_reg(0x05, 0x8b, 0x81)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x00)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_0824_dcm1 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length


    if test_0824_dcm2 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length


    if test_0824_dcm3 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x00)  # f_reg
        write_spi_reg(0x05, 0x91, 0x01)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x20)#multiframe length

    if test_0825 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x01)  # f_reg
        write_spi_reg(0x05, 0x91, 0x03)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x40)#multiframe length

    if test_0826 == 1:
        write_spi_reg(0x05, 0x8b, 0x83)  # scr/l_reg
        write_spi_reg(0x05, 0x8e, 0x01)  # m_reg
        write_spi_reg(0x05, 0x8c, 0x03)  # f_reg
        write_spi_reg(0x05, 0x91, 0x07)  # s_reg
        write_spi_reg(0x05, 0x8f, 0x07)  # n_reg
        write_spi_reg(0x05, 0x90, 0x07)  # n_total_reg
        write_spi_reg(0x05, 0xe4, 0x80)#multiframe length


write_spi_reg(0x05, 0x8d, 0x1f)#k_reg
write_spi_reg(0x05, 0xb2, 0x45)#lane cross, specificly for zcu102 board
write_spi_reg(0x05, 0xb3, 0x76)
write_spi_reg(0x05, 0xb5, 0x03)
write_spi_reg(0x05, 0xb6, 0x12)
#write_spi_reg(0x0f, 0x58, 0x02)#fsx4 vld delay
write_spi_reg(0x05, 0xf9, 0x02)  # sysref_came_delay
write_spi_reg(0x05, 0x71, 0x45)  # tail_bits pn, enablemodule

if test_digana_prbs15 == 1:
    write_spi_reg(0x05, 0x77, 0x02)#prbs15 test pattern

#read sync status
#turn off sysref
write_spi_reg(0x0f, 0x31, 0x0c)  # [0]:jitter filter en, [2]:force root sysref to 0.

