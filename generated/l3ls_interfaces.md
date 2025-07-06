# Lab l3ls - Interfaces configuration

## a-spine-1

```
interface et1
 no switchport
 ip address 10.1.0.0/31

interface et2
 no switchport
 ip address 10.1.0.4/31

interface et3
 no switchport
 ip address 10.1.0.9/31

interface et4
 no switchport
 ip address 10.1.0.13/31

```

## a-spine-2

```
interface et1
 no switchport
 ip address 10.1.0.1/31

interface et2
 no switchport
 ip address 10.1.0.6/31

interface et3
 no switchport
 ip address 10.1.0.11/31

interface et4
 no switchport
 ip address 10.1.0.15/31

interface et5
 no switchport
 ip address 10.1.0.29/31

```

## b-spine-1

```
interface et1
 no switchport
 ip address 10.1.0.2/31

interface et2
 no switchport
 ip address 10.1.0.5/31

interface et3
 no switchport
 ip address 10.1.0.19/31

interface et4
 no switchport
 ip address 10.1.0.23/31

interface et5
 no switchport
 ip address 10.1.0.35/31

```

## b-spine-2

```
interface et1
 no switchport
 ip address 10.1.0.3/31

interface et2
 no switchport
 ip address 10.1.0.7/31

interface et3
 no switchport
 ip address 10.1.0.21/31

interface et4
 no switchport
 ip address 10.1.0.25/31

interface et5
 no switchport
 ip address 10.1.0.31/31

```

## a-leaf-1

```
interface et1
 no switchport
 ip address 10.1.0.8/31

interface et2
 no switchport
 ip address 10.1.0.10/31

interface et3
 no switchport
 ip address 10.1.0.16/31

interface et4
 no ip address
 switchport

```

## a-leaf-2

```
interface et1
 no switchport
 ip address 10.1.0.12/31

interface et2
 no switchport
 ip address 10.1.0.14/31

interface et3
 no switchport
 ip address 10.1.0.17/31

interface et4
 no ip address
 switchport

```

## b-leaf-1

```
interface et1
 no switchport
 ip address 10.1.0.18/31

interface et2
 no switchport
 ip address 10.1.0.20/31

interface et3
 no switchport
 ip address 10.1.0.26/31

interface et4
 no ip address
 switchport

```

## b-leaf-2

```
interface et1
 no switchport
 ip address 10.1.0.22/31

interface et2
 no switchport
 ip address 10.1.0.24/31

interface et3
 no switchport
 ip address 10.1.0.27/31

interface et4
 no ip address
 switchport

```

## c-leaf-1

```
interface et1
 no switchport
 ip address 10.1.0.28/31

interface et3
 no switchport
 ip address 10.1.0.32/31

interface et4
 no ip address
 switchport

```

## c-leaf-2

```
interface et1
 no switchport
 ip address 10.1.0.30/31

interface et3
 no switchport
 ip address 10.1.0.33/31

interface et4
 no ip address
 switchport

```

## d-leaf-1

```
interface et1
 no switchport
 ip address 10.1.0.34/31

interface et4
 no ip address
 switchport

```

## a-host-1

```
interface et1
 no ip address
 switchport

interface et2
 no ip address
 switchport

```

## b-host-1

```
interface et1
 no ip address
 switchport

interface et2
 no ip address
 switchport

```

## c-host-1

```
interface et1
 no ip address
 switchport

interface et2
 no ip address
 switchport

```

## d-host-1

```
interface et1
 no ip address
 switchport

```
