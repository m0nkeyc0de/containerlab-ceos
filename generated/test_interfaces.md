# Lab test - Interfaces configuration

## leaf1

```
interface et1
 no switchport
 ip address 10.1.0.0/31

interface et5
 no ip address
 switchport

```

## leaf2

```
interface et1
 no switchport
 ip address 10.1.0.1/31

interface et5
 no ip address
 switchport

```

## host1

```
interface et1
 no ip address
 switchport

interface et2
 no ip address
 switchport

```
