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
    exit()


# Open device
nRet = ControlSPI.VSI_OpenDevice(ControlSPI.VSI_USBSPI,0,0)
if(nRet != ControlSPI.ERR_SUCCESS):
    print("Open device error!")
    exit()

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
    exit()


write_buffer = (c_ubyte * 1024)()
read_buffer = (c_ubyte * 8192)()

# enable spi control skew code
write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x01
write_buffer[4] = 0x78
write_buffer[5] = 0x80
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x00

nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)



#read in coe list
with open('D:\\work\\ip_test\\nvwa\\python_dump\\coe_list.txt','r+') as fw:
    result = fw.read()
    new_result = result.replace('bcd','python')
    new_code = result.split(' ')

code0 = int(new_code[0],16)
code1 = int(new_code[1],16)
code2 = int(new_code[2],16)
code3 = int(new_code[3],16)

code0_hex = hex(code0);
code1_hex = hex(code1);
code2_hex = hex(code2);
code3_hex = hex(code3);


write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x01
write_buffer[4] = 0x80
write_buffer[5] = code0
write_buffer[6] = code1
write_buffer[7] = code2
write_buffer[8] = code3

Ret = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)






### turn on dnc enable
write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x01
write_buffer[4] = 0x5C
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x00
#nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x01
write_buffer[4] = 0x64
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x00
#nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x01
write_buffer[4] = 0x6c
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x00
#nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x01
write_buffer[4] = 0x74
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x00
#nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)







#dump mode select
write_buffer[0] = 0x72   #reg54
write_buffer[1] = 0x00


fp = open('D:\\work\\ip_test\\nvwa\python_dump\\adc_example.out', 'w')

for n in range(0,1):
    #enable one start
    write_buffer[2] = 0x70   #reg56
    write_buffer[3] = 0x80
    write_buffer[4] = 0x70   #reg56
    write_buffer[5] = 0x88


    nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 2)

    for q in range(0, 8):
            write_buffer[0] = 0xc1
            write_buffer[1] = 0x00
            if (q > 6 ):
                write_buffer[2] = 0x01
            else:
                write_buffer[2] = 0x00
            if (q == 15):
                write_buffer[2] = 0x02

            write_buffer[3] = 0x20 + q*0x20
            write_buffer[4] = 0x00
            write_buffer[5] = 0x00

                # nRet = ControlSPI.VSI_WriteBytes(ControlSPI.VSI_USBSPI,0,0,write_buffer,2)
            nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 6, read_buffer, 4096*2)

            ####################################################################################


            if (nRet != ControlSPI.ERR_SUCCESS):
                    print("Write&Read data error :%d" % nRet)
                    exit()
            #else:
            #       print("%d : Read data from spi:" % q)
                 #   print hex(write_buffer[2])
                 #   print hex(write_buffer[3])
            for i in range(0, 4096*2):
                fp.write("%02x " % (read_buffer[i]))
                fp.write("\n")




### turn on dnc enable
write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x01
write_buffer[4] = 0x5C
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x03
#nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x01
write_buffer[4] = 0x64
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x03
#nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x01
write_buffer[4] = 0x6c
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x03
#nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)

write_buffer[0] = 0xc0
write_buffer[1] = 0x00
write_buffer[2] = 0x00
write_buffer[3] = 0x01
write_buffer[4] = 0x74
write_buffer[5] = 0x00
write_buffer[6] = 0x00
write_buffer[7] = 0x00
write_buffer[8] = 0x03
#nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 9, read_buffer, 2)


fp.close()
###############################################################################################






















