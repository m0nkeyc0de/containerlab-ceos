# Lab test - Interfaces configuration

## leaf1

```
interface et1
 description leaf2:et1
 no ip address
 switchport

interface et5
 description host1:et1
 no ip address
 switchport

```

## leaf2

```
interface et1
 description leaf1:et1
 no ip address
 switchport

interface et5
 description host1:et2
 no ip address
 switchport

```

## host1

```
interface et1
 description leaf1:et5
 no ip address
 switchport

interface et2
 description leaf2:et5
 no ip address
 switchport

```
