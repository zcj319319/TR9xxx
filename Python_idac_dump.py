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



#offset read in coe list
with open('F:\\work\\python\\write\\offset_coe_list.txt','r+') as fw:
    result = fw.read()
    new_result = result.replace('bcd','python')
    new_code = result.split(' ')

    write_buffer[0] = 0xC0
    write_buffer[1] = 0x00
    write_buffer[2] = 0x00
    write_buffer[3] = 0x00
    write_buffer[4] = 0x78
for q in range(0, 24):
    write_buffer[5+q] = int(new_code[q],16)

print(hex(write_buffer[28]))
print(hex(write_buffer[18]))
print(hex(write_buffer[5]))

Ret = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 29, read_buffer, 2)




#read in coe list
with open('F:\\work\\python\\write\\offset_idac_list.txt','r+') as fw:
    result = fw.read()
    new_result = result.replace('bcd','python')
    new_code = result.split(' ')

    write_buffer[0] = 0xC0
    write_buffer[1] = 0x00
    write_buffer[2] = 0x00
    write_buffer[3] = 0x00
    write_buffer[4] = 0x20
for q in range(0, 24):
    write_buffer[5+q] = int(new_code[q],16)

# print(hex(write_buffer[28]))
# print(hex(write_buffer[18]))
# print(hex(write_buffer[5]))

Ret = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 29, read_buffer, 2)


write_mem_reg(0x00,0x70,0x00,0x00,0x00,0x04)

### low mis
#write_spi_reg(0x80,0x60)

fp = open('F:\\work\\python\\write\\adc_example.out', 'w')

#dump mode select  a2[2]   0:normal mode  1:original code
#enable one dump
write_buffer[0] = 0xa2   #reg56
write_buffer[1] = 0x00
write_buffer[2] = 0xa2   #reg56
write_buffer[3] = 0x01
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 4, read_buffer, 2)

import math



sleep(0.01)

for q in range(0, 4):
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