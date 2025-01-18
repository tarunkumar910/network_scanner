#! /usr/bin/emv pyhton


import scapy.all as scapy
import argparse

 

def get_argu():

    parser=argparse.ArgumentParser()
    parser.add_argument("-t","--target", dest="target",help="target IP/IP range.")
    (options)=parser.parse_args()
    return options






def sc(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=broadcast/arp_request
    ans_list =scapy.srp(arp_request_broadcast, timeout=1, verbose=False )[0]
    
    
    ip_list=[]
    for element in ans_list:
        ip_dic={"IP:":element[1].psrc,"Mac:":element[1].hwsrc}
        ip_list.append(ip_dic)

       
        
    return(ip_list)
    



def print_result(result_list):
    print("IP\t\t\tMac Addres\n-----------------------------------------")
    for ip in result_list:
        print(ip["IP:"]+"\t\t"+ip["Mac:"])


options=get_argu()
scan_reult=sc(options.target)
print_result(scan_reult)