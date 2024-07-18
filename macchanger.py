import subprocess
import optparse
import time
import random
import sys
from socket import socket
# windows 11 üzerinden yaptığım için, subprocess call kütüphanesini kullanmayı iptal ettim.
# piyasada çok daha güzel macchanger script'ler var. fakat bu benim. ben python öğrenmeye başladıktan 1 ay sonra bu projeyi, dökümantasyon yardımı almadan kendim yaptım.
class MacChanger:
    def asking_questing(self):
        asking = input("""
        CHOOSE ; \n
        1. CHANGE MAC ADDRES RANDOMLY : '-r' or '--r',
        2  CHANGE MAC ADDRES MANUEL : '-m' or '--m'
                       """)
        if asking == '-r' or asking == '--r':
                MacChanger.random_mac(self)
        elif asking == "-m" or asking == "--m":
                MacChanger.manuel_mac(self)
        else:
            print("Invalid Syntax Error")
            print("Programming shutting down")
            sys.exit()        
    def random_mac(self):
        mac = "abcdef123456789"
        mac_list = mac.strip(":")
        random_mac = random.sample(mac_list,12)
        random_mac_str = ":".join(a+b for a,b in zip(random_mac[::2], random_mac[1::2]))
        print("new current mac : " , random_mac_str)
    def manuel_mac(self):
        interface = input("Enter the interface to change its MAC address: ")
        new_mac = input("Enter the new MAC address: ")
        asking = input("enter you're mac : ")
        print(f"Changing MAC address for {interface} to {new_mac}")
        sys.exit()
mcChanger = MacChanger()
mcChanger.asking_questing()
