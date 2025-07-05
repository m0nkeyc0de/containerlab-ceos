# L3 PTP interfaces configuration

## a-spine-1

```
interface et1
 ip address 10.1.0.0/31

interface et2
 ip address 10.1.0.4/31

interface et3
 ip address 10.1.0.9/31

interface et4
 ip address 10.1.0.13/31

```

## a-spine-2

```
interface et1
 ip address 10.1.0.1/31

interface et2
 ip address 10.1.0.6/31

interface et3
 ip address 10.1.0.11/31

interface et4
 ip address 10.1.0.15/31

interface et5
 ip address 10.1.0.29/31

```

## b-spine-1

```
interface et1
 ip address 10.1.0.2/31

interface et2
 ip address 10.1.0.5/31

interface et3
 ip address 10.1.0.19/31

interface et4
 ip address 10.1.0.23/31

interface et5
 ip address 10.1.0.35/31

```

## b-spine-2

```
interface et1
 ip address 10.1.0.3/31

interface et2
 ip address 10.1.0.7/31

interface et3
 ip address 10.1.0.21/31

interface et4
 ip address 10.1.0.25/31

interface et5
 ip address 10.1.0.31/31

```

## a-leaf-1

```
interface et1
 ip address 10.1.0.8/31

interface et2
 ip address 10.1.0.10/31

interface et3
 ip address 10.1.0.16/31

interface et4
 ip address 10.1.0.37/31

```

## a-leaf-2

```
interface et1
 ip address 10.1.0.12/31

interface et2
 ip address 10.1.0.14/31

interface et3
 ip address 10.1.0.17/31

interface et4
 ip address 10.1.0.39/31

```

## b-leaf-1

```
interface et1
 ip address 10.1.0.18/31

interface et2
 ip address 10.1.0.20/31

interface et3
 ip address 10.1.0.26/31

interface et4
 ip address 10.1.0.41/31

```

## b-leaf-2

```
interface et1
 ip address 10.1.0.22/31

interface et2
 ip address 10.1.0.24/31

interface et3
 ip address 10.1.0.27/31

interface et4
 ip address 10.1.0.43/31

```

## c-leaf-1

```
interface et1
 ip address 10.1.0.28/31

interface et3
 ip address 10.1.0.32/31

interface et4
 ip address 10.1.0.45/31

```

## c-leaf-2

```
interface et1
 ip address 10.1.0.30/31

interface et3
 ip address 10.1.0.33/31

interface et4
 ip address 10.1.0.47/31

```

## d-leaf-1

```
interface et1
 ip address 10.1.0.34/31

interface et4
 ip address 10.1.0.49/31

```

## a-host-1

```
interface et1
 ip address 10.1.0.36/31

interface et2
 ip address 10.1.0.38/31

```

## b-host-1

```
interface et1
 ip address 10.1.0.40/31

interface et2
 ip address 10.1.0.42/31

```

## c-host-1

```
interface et1
 ip address 10.1.0.44/31

interface et2
 ip address 10.1.0.46/31

```

## d-host-1

```
interface et1
 ip address 10.1.0.48/31

```
