import usb.core
import usb.util
import sys
interface = 0
#dev = usb.core.find(idVendor=0x1532, idProduct=0x0017)
dev = usb.core.find(idVendor=0x046d, idProduct=0xc52b)

def main():
        
    if dev is None:
        print ("device not found")

    else:
        print ("device found")
    if dev.is_kernel_driver_active(interface) is True:
        print ("but we need to detach kernel driver")
        dev.detach_kernel_driver(interface)
        print ("claiming device")
        usb.util.claim_interface(dev, interface)


        print ("release claimed interface")
        usb.util.release_interface(dev, interface)
        print ("now attaching the kernel driver again")
        dev.attach_kernel_driver(interface)
        print ("all done")
#    return 0

if __name__ == '__main__':
    main()
