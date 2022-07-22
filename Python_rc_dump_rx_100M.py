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

############################################ power on control #############################
write_spi_reg(0x80,0x40)
write_spi_reg(0x82,0x00)
write_spi_reg(0x84,0x88)  # adc clock delay set, ss corner 22, tt corner 88?
write_spi_reg(0x86,0x80)  # set idac cali range
write_spi_reg(0x88,0x00)  # I path ldo value set
write_spi_reg(0x8a,0x24)  # od_sw_rstn set & mode set
write_spi_reg(0x8e,0x00)  # int power set
write_spi_reg(0x90,0x47)  # vcm set
write_spi_reg(0x92,0x01)  # spi select & mode set
write_spi_reg(0xaa,0x88)  # quantizer reference set
write_spi_reg(0xac,0x88)  # quantizer power set & dem set
write_spi_reg(0xb6,0x00)  # dem clock delay set

write_mem_reg(0x00,0x10,0x00,0x00,0x00,0x05)  #filter enable
write_mem_reg(0x00,0x14,0x00,0x00,0x00,0x05)  #filter enable

# ################### offset cali  ######################################
# #kick offset cali once
# # I channel
# write_buffer[0] = 0xc0  # write
# write_buffer[1] = 0x00
# write_buffer[2] = 0x00
# write_buffer[3] = 0x00
# write_buffer[4] = 0x18
# write_buffer[5] = 0x00
# write_buffer[6] = 0x00
# write_buffer[7] = 0x00
# write_buffer[8] = 0x01
# nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)
# # Q channel
# write_buffer[0] = 0xc0
# write_buffer[1] = 0x00
# write_buffer[2] = 0x00
# write_buffer[3] = 0x00
# write_buffer[4] = 0x1c
# write_buffer[5] = 0x00
# write_buffer[6] = 0x00
# write_buffer[7] = 0x00
# write_buffer[8] = 0x01
# nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)
# sleep(0.001)
# ###############################################################################################
######## debug offset cali
write_mem_reg(0x00,0x8c,0x00,0xff,0xfd,0xef)  ## Q off
write_mem_reg(0x00,0x84,0x1e,0xf7,0xbd,0xef)
write_mem_reg(0x00,0x7c,0x1e,0xf7,0xbd,0xef)
write_mem_reg(0x00,0x88,0x00,0xff,0xfd,0xef)  ## I off
write_mem_reg(0x00,0x80,0x1e,0xf7,0xbd,0xef)
write_mem_reg(0x00,0x78,0x1e,0xf7,0xbd,0xef)
########################### normal work ############################

#read in coe list
with open('F:\\Work\\TR_worklib\\Pangu\\pangu_v3_test\\write\\coe_list.txt','r+') as fw:
    result = fw.read()
    new_result = result.replace('bcd','python')
    new_code = result.split(' ')

code0 = int(new_code[0],16)
code1 = int(new_code[1],16)
code2 = int(new_code[2],16)

code0_hex = hex(code0);
code1_hex = hex(code1);
code2_hex = hex(code2);

write_buffer[0] = 0x92
write_buffer[1] = code0
write_buffer[2] = 0x94
write_buffer[3] = code1
write_buffer[4] = 0x96
write_buffer[5] = code2
write_buffer[6] = 0xb0
write_buffer[7] = 0x0c
write_buffer[8] = 0xb2
write_buffer[9] = 0x00
write_buffer[10] = 0xb4
write_buffer[11] = 0xff

Ret = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 12, read_buffer, 2)

#### work mode set,default rx 200M  !!!!!!!!!!!!!!! ######################
# ###  delay code set
# write_spi_reg(0x84,0x66)

# ### rx 100M mode
# write_spi_reg(0x8a,0x24)
# write_spi_reg(0x92,0x03)
# write_mem_reg(0x00,0x08,0x00,0x00,0x00,0x10)

# ### orx mode
# write_spi_reg(0xb0,0x8c)

#### set to work
write_spi_reg(0xae,0x22)  # sleep
sleep(0.001)
write_spi_reg(0xae,0x20)  # work
sleep(0.001)

fp = open('F:\\work\\python\\write\\adc_example.out', 'w')
# fp = open('adc_example.out', 'w')

#dump mode select  a2[2]   0:normal mode  1:original code
#enable one dump
write_buffer[0] = 0xa2   #reg56
write_buffer[1] = 0x00
write_buffer[2] = 0xa2   #reg56
write_buffer[3] = 0x01
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 4, read_buffer, 2)

import math



sleep(0.001)

for q in range(16, 20):     # 0,4 for i path, 16,20 for q path
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
        nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 8192)

        ####################################################################################


        if (nRet != ControlSPI.ERR_SUCCESS):
                print("Write&Read data error :%d" % nRet)
                exit()
        # else:
        #         print("%d : Read data from spi:" % q)
        for i in range(0, 8192):
            fp.write("%02x " % (read_buffer[i]))
            fp.write("\n")

print("Write data to example.out")


fp.close()