# Must be run as root
# sudo .venv/bin/python arista_magic_packets.py shutdown ceos-operdown
import sys
from scapy.layers import inet
from scapy.all import sendp

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:")
        print(f"{sys.argv[0]} [shutdown|noshutdown] [bridge]")
        exit(1)

    frm_key = sys.argv[1]
    iface = sys.argv[2]

    # Build asked Scapy frame from bytes taken from PCAP file
    frames = {
        'shutdown' : '011c73ffffff001c73e9b191d28be1ba000000',
        'noshutdown' : '011c73ffffff001c73e9b191d28be1ba000001',
    }

    packet = shut_frm = inet.Ether(inet.raw(bytes.fromhex(frames[frm_key])))

    print(f"Arista magic packet for {frm_key} will be send on {iface}")
    print(packet)

    sendp(packet, iface=iface)
