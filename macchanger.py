import subprocess
import optparse
import time
import random
import sys
from socket import socket
# windows 11 üzerinden bu işi yaptığım için subprocess call kütüphanesini kullanmaya gerek duymadım. 
# virtualbox üzerinden kali için denemiş olduğum bu script'i gereksiz ama kendim için faydalı buluyorum.
# daha gelişmiş ve süper iyi macchanger ve dhcp spoofing script'ler elbette var. fakat bunu python yolculuğumda 1-2 aylık temel seviyede iken, dökümantasyon yardımı almadan yaptım.
# o yüzden faydalı buluyorum.
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
        parser = optparse.OptionParser()
        parser.add_option("-i", "--interface", dest="interface", help="Interface to change its")
        parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
        asking = input("enter you're mac : ")
        print("this is you're current mac" , asking)
        sys.exit()
mcChanger = MacChanger()
mcChanger.asking_questing()
