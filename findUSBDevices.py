#!/usr/bin/python
import sys
import usb.core
# find USB devices
dev = usb.core.find(find_all=True)


#vendors = {}
#with open('usb_vid.txt') as f:
#    next(f)
#    for line in f:
#        vendors.update(f.readline().strip().split('\t'))
#
#vendors['0001']

# loop through devices, printing vendor and product ids in decimal and hex
for cfg in dev:
  sys.stdout.write('Decimal VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct) + '\n')
  sys.stdout.write('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')
