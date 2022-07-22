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

# print("%02x " % (read_buffer[0]))
# print("%02x " % (read_buffer[1]))
# exit()

#################################################### mian code start from here #########################################

############################################ power on control #############################
write_spi_reg(0x80,0x40)
write_spi_reg(0x82,0x00)
write_spi_reg(0x84,0x44)  # adc clock delay set
write_spi_reg(0x86,0x40)  # set idac cali range
write_spi_reg(0x88,0x00)  # I path ldo value set
write_spi_reg(0x8a,0x20)  # od_sw_rstn set & mode set
write_spi_reg(0x8e,0x15)  # int power set
write_spi_reg(0x90,0x47)  # vcm set
write_spi_reg(0x92,0x00)  # spi select & mode set
write_spi_reg(0xaa,0x88)  # quantizer reference set
write_spi_reg(0xac,0x80)  # quantizer power set & dem set
write_spi_reg(0xb6,0x04)  # dem clock delay set
write_spi_reg(0xb0,0x84)  # set to orx mode

write_mem_reg(0x00,0x10,0x00,0x00,0x00,0x05)  #filter enable
write_mem_reg(0x00,0x14,0x00,0x00,0x00,0x05)  #filter enable

# write_buffer[0] = 0xa2   #reg56
# write_buffer[1] = 0x04
# write_buffer[2] = 0xa2   #reg56
# write_buffer[3] = 0x05
# nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 4, read_buffer, 2)

# exit()

############################################ rc cali  #############################
write_spi_reg(0xae,0x00)  # set work condition
write_spi_reg(0xb0,0x04)  # set rx for orx cali

write_spi_reg(0xa4,0x02)  #clear fsm
sleep(0.01)
write_spi_reg(0xa4,0x00)
# kick rc cali once
write_buffer[0]=0xa4  #reg18
write_buffer[1]=0x01
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 2)

sleep(0.001)
# check rc cali done
write_buffer[0]=0xa7  #reg18
write_buffer[1]=0x00
write_buffer[2]=0x00
write_buffer[3]=0x00
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 4, read_buffer, 1)

write_spi_reg(0xb0,0x84)  # reset to orx

if(read_buffer[0] == 0x10):
    print("rc cali done!")
else:
    print("rc cali undone!")
### show rc cali result
write_buffer[0]=0xbb  #
write_buffer[1]=0x00
write_buffer[2]=0x00
write_buffer[3]=0x00
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 4, read_buffer, 1)
print("rc cali of Cap: %02d " % (read_buffer[0]))
write_buffer[0]=0xa9  #
write_buffer[1]=0x00
write_buffer[2]=0x00
write_buffer[3]=0x00
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 4, read_buffer, 1)
print("rc cali of Vref: %02d " % (read_buffer[0]))


############################################ offset cali  #############################
write_spi_reg(0xae,0x00)  # set work condition
sleep(0.01)
# kick offset cali once
# I channel
write_buffer[0] = 0xc0  # write
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x18
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x01
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)
sleep(0.1)
write_buffer[0] = 0xc1  # read
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0xa0
write_buffer[5] = 0x00

nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 4)

print("I path status")
print("%02x " % (read_buffer[3]))

# Q channel
write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x1c
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x01
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)
###############################################################################################

# import time
# start = time.time()
# read_buffer = read_mem_reg(0x00,0x9c)
# done_sign = read_buffer[3]
# while done_sign != 0x04:
#     read_buffer = read_mem_reg(0x00, 0x9c)
#     done_sign = read_buffer[3]
# end = time.time()
# print("2st cali time: %.9f"%(end-start))

#check offset cali done
write_buffer[0] = 0xc1
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0xa4
write_buffer[5] = 0x00

nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 4)

print("Q path status")
print("%02x " % (read_buffer[3]))
if(read_buffer[3] == 0x04):
    print("offset cali done!")
else:
    print("offset cali undone!")
sleep(0.01)
############################################ idac cali  #############################
# kick idac cali once
# I channel
write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0x08
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x0D # count time 1024:0x0D
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
write_buffer[8] = 0x0D
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)
###############################################################################################

#### cali time cal
# import time
# start = time.time()
# read_buffer = read_mem_reg(0x00,0x98)
# done_sign = read_buffer[3]
# while done_sign != 0x05:
#     read_buffer = read_mem_reg(0x00, 0x9c)
#     done_sign = read_buffer[3]
# end = time.time()
# print("idac cali time: %.9f"%(end-start))

sleep(2)
#check i path idac cali done
write_buffer[0] = 0xc1
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0xa0
write_buffer[5] = 0x00

nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 4)

if(read_buffer[3] == 0x05):
    print("idac cali done!")
else:
    print("idac cali undone!")

# check q path idac cali done
write_buffer[0] = 0xc1
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x00
write_buffer[4] = 0xa4
write_buffer[5] = 0x00

nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 4)

if (read_buffer[3] == 0x05):
    print("q path idac cali done!")
else:
    print("q path idac cali undone!")

#print (hex(read_buffer[3]))
###############################################################################################
######## debug offset cali
write_mem_reg(0x00,0x8c,0x00,0xff,0xfd,0xef)  ## Q off
write_mem_reg(0x00,0x84,0x1e,0xf7,0xbd,0xef)
write_mem_reg(0x00,0x7c,0x1e,0xf7,0xbd,0xef)
write_mem_reg(0x00,0x88,0x00,0xff,0xfd,0xef)  ## I off
write_mem_reg(0x00,0x80,0x1e,0xf7,0xbd,0xef)
write_mem_reg(0x00,0x78,0x1e,0xf7,0xbd,0xef)
########################### normal work ############################
# #### bypass rccali
# write_spi_reg(0x92,0x02)  #spi en
# write_spi_reg(0x94,0x28)  #ct cali,
# write_spi_reg(0x96,0xb4)  #vref,org:cd,need add 128
# write_spi_reg(0xb0,0x0c)  #cap_t
# write_spi_reg(0xb2,0x00)  #cap_t
# write_spi_reg(0xb4,0xff)  #cap_t

write_spi_reg(0xae,0x22)  # sleep
sleep(0.01)
write_spi_reg(0xae,0x20)  # work
sleep(0.01)
write_spi_reg(0x80,0x80)  # clock sync 0xc0 for dem on; 0x80 for dem off

# ### debug, atb
# write_spi_reg(0x82,0x0e)
# write_spi_reg(0xb8,0x00)

# ###  delay code debug
# write_spi_reg(0x84,0x66)

### od option
write_spi_reg(0x8c,0x07)

# ### power control
# write_spi_reg(0x8e,0x3f)

### ldo output set
# write_spi_reg(0x88,0xc0)
# write_spi_reg(0x8a,0x03)

# ### gpio clk test
# write_spi_reg(0x48,0xff)  # new addr????

########## debug dig power  #############
# write_mem_reg(0x00,0x10,0x00,0x00,0x00,0x01)  #filter disable
# write_mem_reg(0x00,0x14,0x00,0x00,0x00,0x01)  #filter disable

###############################################################################################
#########################################dump data to memory##################################
sleep(0.1)
fp = open('adc_example.out', 'w')

########## sleep mode set
### 0xae [5:4] for sleep mode; 0xb0 [0] for sleep reset time 1 for 3.2us; 0 for 2us

# ### case1 sleep mode 0 to work
# write_spi_reg(0xae,0x02)
# write_spi_reg(0xb0,0x84) # [7] for rx/orx select; [2] for od set; [0] for 3.2us/2us select
# sleep(0.01)
### case2 sleep mode 1 to work
write_spi_reg(0xae,0x12)
write_spi_reg(0xb0,0x84) # [7] for rx/orx select; [2] for od set; [0] for 3.2us/2us select
sleep(0.01)
# ### case3 sleep mode 2 to work, 1us time
# write_spi_reg(0xae,0x22)
# sleep(0.01)
# ### case4 sleep mode 2 to work, 0.5us time
# write_spi_reg(0xae,0x32)
# sleep(0.01)

#dump mode select  a2[2]   0:normal mode  1:original code
#enable one dump
# write_spi_reg(0xae,0x00)  # case1 work
# write_spi_reg(0xae,0x10)  # case2 work
# write_spi_reg(0xae,0x20)  # case3 work
# write_spi_reg(0xae,0x30)  # case4 work
write_buffer[0] = 0xa2   #reg56
write_buffer[1] = 0x00   # 04 for raw data/ 00 for filtered data
write_buffer[2] = 0xa2   #reg56
write_buffer[3] = 0x01   # 05 for raw data/ 01 for filtered data
write_buffer[4] = 0xae   # refer to up
write_buffer[5] = 0x10   #
nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 2)


import math

write_buffer = (c_ubyte * 1024)()
read_buffer = (c_ubyte * 8192)()

sleep(1)

for q in range(0, 32):
        write_buffer[0] = 0xc1
        write_buffer[1] = 0x00
        high_bit = math.floor((q*2048*4+8192)/65536)
        middle_bit = math.floor((q * 2048*4 + 8192 -high_bit*65536)/ 256)
        low_bit = q * 2048*4 + 8192 - high_bit * 65536 - middle_bit *256
        write_buffer[2] = high_bit
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






















