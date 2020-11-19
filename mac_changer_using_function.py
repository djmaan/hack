#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:44:26 2020

@author: djmaan
"""


import subprocess
import optparse

def change_ac(interface, new_mac):
    print("[+] Changing MAC address for" +interface + "to" +new_mac)
    
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])


parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest = "interface",help "Interface to change its MAC address")
parser.add_option("-m","--new_mac", dest = "new_mac" ,help="New MAC address")

(options, arguments) = parser.parse_args()

change_mac(options.interface, options.new_mac)


