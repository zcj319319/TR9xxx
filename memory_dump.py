from ctypes import *
from time import sleep
# Import module
import ControlSPI
import time
import random

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

def write_mem_reg(addr0,addr1,data0):
    write_buffer = (c_ubyte * 3)()
    read_buffer = (c_ubyte * 1)()
    write_buffer[0] = addr0
    write_buffer[1] = addr1
    write_buffer[2] = data0
    #print(write_buffer[0],write_buffer[1],write_buffer[2])
   # print(str(addr0)+' '+str(addr1)+' '+str(data0))
    nRet = ControlSPI.VSI_WriteBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 3)

def read_mem_reg(addr0, addr1):
    write_buffer = (c_ubyte * 2)()
    read_buffer = (c_ubyte * 4096)()
    write_buffer[0] = addr0
    write_buffer[1] = addr1
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 4096)
    return read_buffer

def read_mem_reg_single(addr0, addr1):
    write_buffer = (c_ubyte * 2)()
    read_buffer = (c_ubyte * 1)()
    write_buffer[0] = addr0
    write_buffer[1] = addr1
    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 1)
    return read_buffer


##cfg ana
power_on = 0
if power_on == 1 :
    write_mem_reg(0x10,0x7c,0x37)   # ldodiv  7:4 = 4 buff_div 3:0 =8
    write_mem_reg(0x10,0x35,0x00)   #  a channel por=0
    write_mem_reg(0x10,0x35,0x18)   # a  channelpor=1
    write_mem_reg(0x10,0x71,0x00)   #  b chan por=0
    write_mem_reg(0x10,0x71,0x18)   #  b chan por=1

    write_mem_reg(0x10, 0x06, 0x01)  # 01= bk comp os cal enable
    write_mem_reg(0x10, 0x01, 0x01)  # 01= mdac comp os cal enable

    write_mem_reg(0x10, 0x0b, 0x01)  # 01= mdac comp os cal enable
    write_mem_reg(0x10, 0x10, 0x01)  # 01= bk comp os cal enable

    write_mem_reg(0x10, 0x06, 0x01)  # 01= bk comp os cal enable
    write_mem_reg(0x10, 0x01, 0x01)  # 01= mdac comp os cal enable

    write_mem_reg(0x10, 0x06, 0x01)  # 01= bk comp os cal enable
    write_mem_reg(0x10, 0x01, 0x01)  # 01= mdac comp os cal enable

    write_mem_reg(0x10, 0x06, 0x01)  # 01= bk comp os cal enable
    write_mem_reg(0x10, 0x01, 0x01)  # 01= mdac comp os cal enable


    write_mem_reg(0x10,0x85,0x01)   #  sysref top
    write_mem_reg(0x10,0x85,0x03)   #   sysref top


    write_mem_reg(0x00,0x40,0x00)  # pd dig clock test
    write_mem_reg(0x03,0x11,0x04)  #
    write_mem_reg(0x00,0x08,0x03)  #








## ddc test data bypass


ddc_test_data = 0
if ddc_test_data == 1:
    write_mem_reg(0x03,0x27,0x07)
    write_mem_reg(0x03,0x47,0x07)
    write_mem_reg(0x03,0x67,0x07)
    write_mem_reg(0x03,0x87,0x07)
    write_mem_reg(0x03,0x11,0x04)
    write_mem_reg(0x05,0x50,0x0f)

write_mem_reg(0x02,0x00,0x00)

ddc_nco_bypass = 0
if ddc_nco_bypass == 1:
    write_mem_reg(0x03,0x27,0x00)
    write_mem_reg(0x03,0x47,0x00)
    write_mem_reg(0x03,0x67,0x00)
    write_mem_reg(0x03,0x87,0x00)
    write_mem_reg(0x02,0x00,0x03)
    write_mem_reg(0x03,0x10,0x30)
    write_mem_reg(0x03,0x30,0x30)
    write_mem_reg(0x03,0x50,0x30)
    write_mem_reg(0x03,0x70,0x30)
    write_mem_reg(0x03,0x16,0x00)
    write_mem_reg(0x03,0x17,0x55)
    write_mem_reg(0x03,0x18,0x55)
    write_mem_reg(0x03,0x19,0x55)
    write_mem_reg(0x03,0x1a,0x55)
    write_mem_reg(0x03,0x1b,0x00)

## cali enable part

dnc_cali_enable    = 0
gec_cali_enable    = 0
chopper_enable     = 0
tios_cali_enable   = 0
tigian_cali_enable = 0
tiskew_cali_enable = 0


if dnc_cali_enable == 1:
    write_mem_reg(0x08,0x10,0x01)
    sleep(1)

    read_buffer = read_mem_reg_single(0x88, 0x11)
    print("dnc cali states: %02x\n" % (read_buffer[0]))
    write_mem_reg(0x08,0x10,0x00)


if gec_cali_enable == 1:
    write_mem_reg(0x0b, 0x60, 0x01)
    sleep(1)

    read_buffer = read_mem_reg_single(0x8b, 0x61)
    print("gec cali states: %02x\n" % (read_buffer[0]))
    write_mem_reg(0x0b, 0x60, 0x00)

if chopper_enable == 1:
    write_mem_reg(0x0b, 0x80, 0x01)
    sleep(1)

    read_buffer = read_mem_reg_single(0x8b, 0x81)
    print("chopper cali states: %02x\n" % (read_buffer[0]))
    write_mem_reg(0x0b, 0x80, 0x00)

if tios_cali_enable == 1:
    write_mem_reg(0x0b, 0xa0, 0x01)
    sleep(1)

    read_buffer = read_mem_reg_single(0x8b, 0xa2)
    print("tios cali states: %02x\n" % (read_buffer[0]))
    write_mem_reg(0x0b, 0xa0, 0x00)

if tigian_cali_enable == 1:
    write_mem_reg(0x0b, 0xc0, 0x01)
    sleep(10)

    read_buffer = read_mem_reg_single(0x8b, 0xc1)
    print("tigian cali states: %02x\n" % (read_buffer[0]))
    write_mem_reg(0x0b, 0xc0, 0x00)

if tiskew_cali_enable == 1:
    write_mem_reg(0x0b, 0xf0, 0x01)
    sleep(10)

    read_buffer = read_mem_reg_single(0x8b, 0xf1)
    print("tiskew cali states: %02x\n" % (read_buffer[0]))
    write_mem_reg(0x0b, 0xf0, 0x00)

## DDC smp trig
smp_ddc_trig = 1
if smp_ddc_trig ==1 :
    write_mem_reg(0x0f, 0x18, 0x00)
    write_mem_reg(0x0f, 0x16, 0x00)
    write_mem_reg(0x0f, 0x1d,0x1)
    write_mem_reg(0x0f, 0x1c, 0x1)
    write_mem_reg(0x0f,0x16,0x08)
    write_mem_reg(0x0f,0x17,0x40)
    #write_mem_reg(0x0f, 0x17, 0x40)
    write_mem_reg(0x0f,0x19,0x3c)
    write_mem_reg(0x0f,0x1a,0x00)
    write_mem_reg(0x0f,0x1b,0x10)
    write_mem_reg(0x0f, 0x1d,0x0)
    write_mem_reg(0x0f, 0x1c, 0x0)
    #write_mem_reg(0x03,0x01,0x00)
    write_mem_reg(0x0f,0x18,0x02)
    time.sleep(5)
    read_buffer = read_mem_reg(0x8f, 0x25)
    read_buffer = read_mem_reg(0x8f, 0x24)
    print("addr(0xf24)=%02x\n" % (read_buffer[0]))
    read_buffer = read_mem_reg(0x8f, 0x16)
    print("addr(0xf16)=%02x\n" % (read_buffer[0]))
    # while (1):
    #     time.sleep(1)
    #     read_buffer = read_mem_reg(0x8f, 0x25)
    #     print("%02x\n" % (read_buffer[0]))

## memory write test
mem_wr_test = 0
if mem_wr_test == 1:
    write_mem_reg(0x0f,0x16,0x10)
    write_mem_reg(0x0f,0x11,0x01)
    write_mem_reg(0x0f,0x10,0x01)
    write_mem_reg(0x0f,0x11,0x00)
    write_mem_reg(0x0f,0x10,0x00)
    fp=open('memory_dump_wr.txt','w')
    deepth = 131072
    for i in range(0,deepth):
        rdata=int(random.randint(0,255))
        write_mem_reg(0x0f, 0x24, rdata)
        fp.write("%02x\n" % (rdata))
    fp.close()

write_mem_reg(0x0f,0x11,0x01)
write_mem_reg(0x0f,0x10,0x01)
write_mem_reg(0x0f,0x16,0x10)
write_mem_reg(0x0f,0x11,0x00)
write_mem_reg(0x0f,0x10,0x00)
fp=open('memory_dump_data.txt','w')


'''import math
fp=open('memory_dump.txt','w')
for i in range(0, 4):
    
read_buffer = read_mem_reg(0x8f, 0x24)
print (type(read_buffer))

print (len(read_buffer))
read_buffer = read_mem_reg(0x8f, 0x24)

'''
offset = 0x00
data_old = 0x55
read_buffer = read_mem_reg(0x8f, 0x16)
#print(read_buffer[0])
for i in range(0, 32):
    data_new = i*4 + offset
    write_mem_reg(0x0f,0x11,data_old)
    write_mem_reg(0x0f,0x11,data_new)
    #print("%02x\n" % (data_new))
    read_buffer = read_mem_reg(0x8f, 0x24)
    for k in range(0, len(read_buffer)):
        fp.write("%02x\n" % (read_buffer[k]))
fp.close()


