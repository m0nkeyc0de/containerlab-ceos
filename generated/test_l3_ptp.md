# L3 PTP interfaces configuration

## leaf1

```
interface et1
 ip address 10.1.0.0/31

interface et5
 ip address 10.1.0.3/31

```

## leaf2

```
interface et1
 ip address 10.1.0.1/31

interface et5
 ip address 10.1.0.5/31

```

## host1

```
interface et1
 ip address 10.1.0.2/31

interface et2
 ip address 10.1.0.4/31

```
