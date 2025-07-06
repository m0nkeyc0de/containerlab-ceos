# Lab l3lsmini - Interfaces configuration
## spine1
```
interface et1
  description leaf1:et1
  no switchport
  ip address 10.1.0.0/31
interface et2
  description leaf2:et1
  no switchport
  ip address 10.1.0.2/31

```
## leaf1
```
interface et1
  description spine1:et1
  no switchport
  ip address 10.1.0.1/31
interface et2
  description leaf2:et2
  switchport
  no ip address
interface et3
  description host1:et1
  switchport
  no ip address
interface et4
  description host2:et1
  switchport
  no ip address

```
## leaf2
```
interface et1
  description spine1:et2
  no switchport
  ip address 10.1.0.3/31
interface et2
  description leaf1:et2
  switchport
  no ip address
interface et3
  description host1:et2
  switchport
  no ip address
interface et4
  description host2:et2
  switchport
  no ip address

```
## host1
```
interface et1
  description leaf1:et3
  switchport
  no ip address
interface et2
  description leaf2:et3
  switchport
  no ip address

```
## host2
```
interface et1
  description leaf1:et4
  switchport
  no ip address
interface et2
  description leaf2:et4
  switchport
  no ip address

```
