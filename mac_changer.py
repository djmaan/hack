#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:09:52 2020

@author: djmaan
"""
import subprocess

Interface = int("interface>")

New_mac = int("new_MAC")

print("[+] Changing mac address of "+ Interface + "to" + New_mac )

subprocess.call(["ifconfig",Interface,"down"])
subprocess.call(["ifconfig",Interface,"hw ether",New_mac])
subprocess.call(["ifconfig",Interface,"up"])

