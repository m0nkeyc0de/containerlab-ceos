# Lab test - Interfaces configuration
## leaf1
```
interface et1
  description leaf2:et1
  switchport
  no ip address
interface et5
  description host1:et1
  switchport
  no ip address

```
## leaf2
```
interface et1
  description leaf1:et1
  switchport
  no ip address
interface et5
  description host1:et2
  switchport
  no ip address

```
## host1
```
interface et1
  description leaf1:et5
  switchport
  no ip address
interface et2
  description leaf2:et5
  switchport
  no ip address

```
