"""
Program test environment
Pyhone version:3.4.1
Firmware version:2.2.12
Dependent files(MacOSX):libGinkgo_Driver.dylib,libusb-0.1.4.dylib,libusb-1.0.0.dylib,ControlSPI.py
Dependent files(Windows):Ginkgo_Driver.dll,ControlSPI.py
Dependent files(Linux):libGinkgo_Driver.so,libusb-1.0.so,ControlSPI.py
More Infomation:www.viewtool.com
"""
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
def read_spi_reg(addr,data):
    write_buffer = (c_ubyte * 4)()
    read_buffer = (c_ubyte * 1)()
    write_buffer[0] = addr
    write_buffer[1] = data
    write_buffer[2] = 0x00
    write_buffer[3] = 0x00
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 4, read_buffer, 1)
    return read_buffer

def write_spi_reg(addr,data):
    write_buffer = (c_ubyte * 2)()
    read_buffer = (c_ubyte * 2)()
    write_buffer[0] = addr
    write_buffer[1] = data
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 2)

def write_mem_reg(addr0,addr1,data0,data1,data2,data3):
    write_buffer = (c_ubyte * 9)()
    read_buffer = (c_ubyte * 2)()
    write_buffer[0] = 0xc0
    write_buffer[1] = 0x00
    write_buffer[2] = 0x00
    write_buffer[3] = addr0
    write_buffer[4] = addr1
    write_buffer[5] = data0
    write_buffer[6] = data1
    write_buffer[7] = data2
    write_buffer[8] = data3
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

def read_mem_reg(addr0, addr1):
    write_buffer = (c_ubyte * 6)()
    read_buffer = (c_ubyte * 4)()
    write_buffer[0] = 0xc1
    write_buffer[1] = 0x00
    write_buffer[2] = 0x00
    write_buffer[3] = addr0
    write_buffer[4] = addr1
    write_buffer[5] = 0x00
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 4)
    return read_buffer

#print("%02x " % (read_buffer[0]))
#print("%02x " % (read_buffer[1]))
#exit()



############################################ initial config  #############################
#### debug for demux
#write_spi_reg(0x82,0xe0)

# 100m mode config below   also need take care when kick dac cali and offset cali. (0x08 0x0c 0x18 0x1c)

# mode1v
write_buffer[0]=0x8a  #reg18
write_buffer[1]=0x04
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 2)

#clock mode /  vref trim fre
write_buffer[0]=0x92  #reg18
write_buffer[1]=0x05
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 2)

#clk sel
write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x08
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x10
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x0c
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x10
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x18
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x02
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x1c
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x02
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)
#

#################################################### mian code start from here #########################################

############################################ power on control #############################
write_spi_reg(0x80,0x0C)  #ans_rst1v
sleep(1)
write_spi_reg(0x84,0x55)  #del_ctrl1v,44 for tt, 77 for ff
write_spi_reg(0x88,0x0f)  #int_rst  int_pd
write_spi_reg(0x8e,0x15)  #op_sel1v
write_spi_reg(0x90,0x78)  #demux_cksel1v pd1v  vcm_sel1v
# write_spi_reg(0x98,0x02)
# write_spi_reg(0x9e,0x80)  #dcc_trim_dccp
# write_spi_reg(0xa0,0x80)  #dcc_trim_dccn

# write_buffer[0]=0x80  #reg0
# write_buffer[1]=0x0C
# write_buffer[2]=0x84  #reg2
# write_buffer[3]=0x55  #del_ctrl1v
# write_buffer[4]=0x88  #reg4
# write_buffer[5]=0x0f  #int_rst  int_pd
# write_buffer[6]=0x8e  #reg8
# write_buffer[7]=0x15  #op_sel1v
# write_buffer[8]=0x90  #reg8
# write_buffer[9]=0x78  #demux_cksel1v pd1v  vcm_sel1v
# write_buffer[10]=0x9e  #reg15
# write_buffer[11]=0x80  #dcc_trim_dccp
# write_buffer[12]=0xa0  #reg16
# write_buffer[13]=0x80  #dcc_trim_dccn
# nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 14, read_buffer, 2)

write_mem_reg(0x00,0x10,0x00,0x00,0x00,0x05)  #filter enable
write_mem_reg(0x00,0x14,0x00,0x00,0x00,0x05)  #filter enable

write_buffer[0] = 0xa2   #reg56
write_buffer[1] = 0x04
write_buffer[2] = 0xa2   #reg56
write_buffer[3] = 0x05
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 4, read_buffer, 2)
#exit()


################## dcc cali #########################

write_spi_reg(0x98,0x03)  #en dcc, org 0x07,change to 0x03
write_spi_reg(0x9a,0x03)  #dcc start
sleep(1)

###################################################################
write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x08
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x1C  #dac nt_sel
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x0c
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x1C  #dac nt_sel
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

sleep(1)

############################################ rc cali  #############################

write_spi_reg(0xa4,0x02)  #clear fsm
sleep(0.1)
write_spi_reg(0xa4,0x00)
#kick rc cali once
write_buffer[0]=0xa4  #reg18
write_buffer[1]=0x01
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 2)

###############################################################################################
sleep(0.3)
#check rc cali done
write_buffer[0]=0xa7  #reg18
write_buffer[1]=0x00
write_buffer[2]=0x00
write_buffer[3]=0x00
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 4, read_buffer, 1)

if(read_buffer[0] == 0x15 or read_buffer[0] == 0x35):
    print("rc cali done!")
else:
    print("rc cali undone!")

sleep(0.1)
#### bypass rccali
write_spi_reg(0x92,0x07)  #spi en
write_spi_reg(0x94,0x87)  #ct cali,8b/a7;87/af; 6f/af for lt?; tt04: try1 57/ab;ff02 8d/b2
write_spi_reg(0x96,0xaf)  #vref

############################################ offset cali  #############################

#kick offset cali once

# I channel
write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x18
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x03
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

sleep(1)

# Q channel
write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x1c
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x03
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)
###############################################################################################

sleep(1)
write_buffer[0] = 0xc1
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x9c
write_buffer[5] = 0x00

nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 4)

print("Q path status")
print("%02x " % (read_buffer[3]))
if(read_buffer[3] == 0x04):
    print("q path offset cali done!")
else:
    print("q path offset cali undone!")

#check offset cali done
write_buffer[0] = 0xc1
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x98
write_buffer[5] = 0x00

nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 4)

if(read_buffer[3] == 0x04):
    print("i path offset cali done!")
else:
    print("i path offset cali undone!")

sleep(0.1)

############################################ idac cali  #############################

#kick idac cali once

# I channel
write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x08
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x1d # set time
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

# Q channel
write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x0c
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x1d
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)
###############################################################################################
sleep(4)

#check idac cali done
write_buffer[0] = 0xc1
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x98
write_buffer[5] = 0x00

nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 4)

if(read_buffer[3] == 0x05):
    print("idac cali done!")
else:
    print("idac cali undone!")
#print (hex(read_buffer[3]))
###############################################################################################

########################### normal work ############################
write_spi_reg(0x86,0x04)  #low noise
write_spi_reg(0x88,0x0c)  # ff -> 0c
write_spi_reg(0x90,0x48)  # 78 -> 48
write_spi_reg(0x80,0xc0)  #c0 -> 40
sleep(0.1)
write_spi_reg(0x8a,0x34)  #od control,100M mode
#write_spi_reg(0x8a,0x30)  #od control,200M mode
write_spi_reg(0x88,0x00)  #fc -> f0
write_spi_reg(0x80,0x40)  #0c -> 40
### debug mode
#write_spi_reg(0x86,0x07)  #04 -> 07

### debug,ckdiv128
#write_spi_reg(0xaa,0x04)  #0c -> 40
#write_spi_reg(0xac,0x0d)

### debug, atb
# write_spi_reg(0x82,0x0a)

### dcc atb
#write_spi_reg(0xac,0x0a)

###  delay code debug
#write_spi_reg(0x84,0x66)

### od option
write_spi_reg(0x8c,0x1c)

### power control
write_spi_reg(0x8e,0x00)

### vcm sel
write_spi_reg(0x90,0x47)

### ldo output set
# write_spi_reg(0x88,0xc0)

### low mis
# write_spi_reg(0x80,0x60)

###### set default idac/offset value
# write_mem_reg(0x00,0x74,0x00,0x00,0x00,0x1e)
# write_mem_reg(0x00,0x6c,0x04,0x08,0x10,0x20)
# write_mem_reg(0x00,0x64,0x40,0x81,0x02,0x04)
# write_mem_reg(0x00,0x5c,0x08,0x10,0x20,0x40)
# write_mem_reg(0x00,0x54,0x00,0x00,0x00,0x02)
# write_mem_reg(0x00,0x4c,0x04,0x08,0x10,0x20)
# write_mem_reg(0x00,0x44,0x40,0x81,0x02,0x04)
# write_mem_reg(0x00,0x3c,0x08,0x10,0x20,0x40)
# write_mem_reg(0x00,0x34,0x00,0x08,0x20,0x82)
# write_mem_reg(0x00,0x2c,0x08,0x20,0x82,0x08)
# write_mem_reg(0x00,0x24,0x20,0x82,0x08,0x20)
# write_mem_reg(0x00,0x8c,0x00,0xff,0xfd,0xef)  #Q path off
# write_mem_reg(0x00,0x84,0x1e,0xf7,0xbd,0xef)
# write_mem_reg(0x00,0x7c,0x1e,0xf7,0xbd,0xef)

# write_mem_reg(0x00,0x70,0x00,0x00,0x00,0x1e)
# write_mem_reg(0x00,0x68,0x04,0x08,0x10,0x20)
# write_mem_reg(0x00,0x60,0x40,0x81,0x02,0x04)
# write_mem_reg(0x00,0x58,0x08,0x10,0x20,0x40)
# write_mem_reg(0x00,0x50,0x00,0x00,0x00,0x02)
# write_mem_reg(0x00,0x48,0x04,0x08,0x10,0x20)
# write_mem_reg(0x00,0x40,0x40,0x81,0x02,0x04)
# write_mem_reg(0x00,0x38,0x08,0x10,0x20,0x40)
# write_mem_reg(0x00,0x30,0x00,0x08,0x20,0x82)
# write_mem_reg(0x00,0x28,0x08,0x20,0x82,0x08)
# write_mem_reg(0x00,0x20,0x20,0x82,0x08,0x20)
# write_mem_reg(0x00,0x88,0x00,0xff,0xfd,0xef) # i path off
# write_mem_reg(0x00,0x80,0x1e,0xf7,0xbd,0xef)
# write_mem_reg(0x00,0x78,0x1e,0xf7,0xbd,0xef)

sleep(0.1)
write_spi_reg(0x8a,0x24)  #od control,100M mode
#write_spi_reg(0x8a,0x20)  #od control,200M mode
sleep(0.1)

#### add od option
#write_spi_reg(0x8a,0x2c)  #od control,100M mode

#### reset again before work
write_spi_reg(0x80,0x4c)
sleep(0.1)
write_spi_reg(0x80,0x40)
sleep(0.1)

### pd Q path
# write_spi_reg(0x80,0x48)
# write_spi_reg(0x86,0x14)
# write_spi_reg(0x88,0x22)
# write_spi_reg(0x8a,0xa4)  ## 100M mode
# write_spi_reg(0x8c,0x9f)
# write_spi_reg(0x90,0x68)

### pd I path
# write_spi_reg(0x80,0x44)
# write_spi_reg(0x86,0xc4)
# write_spi_reg(0x88,0x11)
# write_spi_reg(0x8a,0x64)  ## 100M mode
# write_spi_reg(0x8c,0x5f)
# write_spi_reg(0x90,0x58)
sleep(0.1)

########## debug dig power  #############
write_mem_reg(0x00,0x10,0x00,0x00,0x00,0x01)  #filter disable
# write_mem_reg(0x00,0x14,0x00,0x00,0x00,0x01)  #filter disable
###########################################

###############################################################################################
#########################################dump data to memory##################################
fp = open('adc_example.out', 'w')

#dump mode select  a2[2]   0:normal mode  1:original code
#enable one dump
write_buffer[0] = 0xa2   #reg56
write_buffer[1] = 0x00
write_buffer[2] = 0xa2   #reg56
write_buffer[3] = 0x01
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 4, read_buffer, 2)

import math

sleep(1)

for q in range(0, 32):
        write_buffer[0] = 0xc1
        write_buffer[1] = 0x00
        high_bit = math.floor((q*2048*4+8192)/65536)
        middle_bit = math.floor((q * 2048*4 + 8192 -high_bit*65536)/ 256)
        low_bit = q * 2048*4 + 8192 - high_bit * 65536 - middle_bit *256
        write_buffer[2] = math.trunc(high_bit)
        write_buffer[3] = math.trunc(middle_bit)
        write_buffer[4] = math.trunc(low_bit)
        # print (hex(write_buffer[2]))
        # print (hex(write_buffer[3]))
        # print (hex(write_buffer[4]))
        # if (q > 6 ):
        #     write_buffer[2] = 0x01
        # else:
        #     write_buffer[2] = 0x00
        # if (q == 15):
        #     write_buffer[2] = 0x02
        #
        # write_buffer[3] = 0x20 + q*0x20
        # write_buffer[4] = 0x00
        write_buffer[5] = 0x00

            # nRet = ControlSPI.VSI_WriteBytes(ControlSPI.VSI_USBSPI,0,0,write_buffer,2)
        nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 4096*2)

        ####################################################################################


        if (nRet != ControlSPI.ERR_SUCCESS):
                print("Write&Read data error :%d" % nRet)
                exit()
        # else:
        #         print("%d : Read data from spi:" % q)
        for i in range(0, 4096*2):
            fp.write("%02x " % (read_buffer[i]))
            fp.write("\n")


print("Write data to example.out")


fp.close()

###############################################################################################






















