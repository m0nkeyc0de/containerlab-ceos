# Arista cEOS magic packets
Interface operational state in cEOS is not linked to the OS-level network interfaces, which stay up all the time.

Following frame is sent when an interface is `shutdown`:
```
0000  01 1c 73 ff ff ff 00 1c 73 e9 b1 91 d2 8b e1 ba   ..s.....s.......
0010  00 00 00                                          ...


Ethernet II, Src: AristaNetwor_e9:b1:91 (00:1c:73:e9:b1:91), Dst: AristaNetwor_ff:ff:ff (01:1c:73:ff:ff:ff)
    Destination: AristaNetwor_ff:ff:ff (01:1c:73:ff:ff:ff)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast)
    Source: AristaNetwor_e9:b1:91 (00:1c:73:e9:b1:91)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: Arista Vendor Specific Protocol (0xd28b)
    [Stream index: 1]
Arista Vendor Specific Protocol
    Subtype: Unknown (0xe1ba)
    [Expert Info (Warning/Sequence): Unknown subtype: 0xe1ba]
        [Unknown subtype: 0xe1ba]
        [Severity level: Warning]
        [Group: Sequence]
```

Following frame is sent when an interface is `no shutdown`:
```
0000  01 1c 73 ff ff ff 00 1c 73 e9 b1 91 d2 8b e1 ba   ..s.....s.......
0010  00 00 01                                          ...


Ethernet II, Src: AristaNetwor_e9:b1:91 (00:1c:73:e9:b1:91), Dst: AristaNetwor_ff:ff:ff (01:1c:73:ff:ff:ff)
    Destination: AristaNetwor_ff:ff:ff (01:1c:73:ff:ff:ff)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast)
    Source: AristaNetwor_e9:b1:91 (00:1c:73:e9:b1:91)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: Arista Vendor Specific Protocol (0xd28b)
    [Stream index: 1]
Arista Vendor Specific Protocol
    Subtype: Unknown (0xe1ba)
    [Expert Info (Warning/Sequence): Unknown subtype: 0xe1ba]
        [Unknown subtype: 0xe1ba]
        [Severity level: Warning]
        [Group: Sequence]
```
