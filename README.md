# geoip
Python script for extracting info about IP addresses or domains using freegeoip.net

### Help
```
usage: geoip.py [-h] [-v] <ip> [<ip> ...]

Extract IP or domain information using freegeoip.net

positional arguments:
  <ip>           ip address or domain

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
```

### Example
`$ python geoip.py google.com`
```
                                   IP:  172.217.7.238
                         Country Code:  US
                         Country Name:  United States
                          Region Code:  CA
                          Region Name:  California
                                 City:  Mountain View
                             ZIP Code:  94043
                            Time Zone:  America/Los_Angeles
                             Latitude:  37.4192
                            Longitude:  -122.0574
                           Metro Code:  807

```
