# IPFuscator

## Author

Vincent Yiu (@vysecurity)

Modded for Python3 (@nu11secur1ty)

## Blog Post
https://vincentyiu.co.uk/ipfuscation/

## What is IPFuscator?

IPFuscation is a technique that allows for IP addresses to be represented in hexadecimal or decimal instead of the decimal encoding we are used to. IPFuscator allows us to easily convert to these alternative formats that are interpreted in the same way.

## Usage

1) `git clone https://github.com/vysec/ipfuscator`
2) `python ipfuscator.py 127.0.0.1` or `python3 ipfuscator3.py 127.0.0.1` 

```
IPFuscator
Author: Vincent Yiu (@vysecurity)
https://www.github.com/vysec/IPFuscator
Version: 0.1.0

IP Address:     127.0.0.1

Decimal:        2130706433
Hexadecimal:    0x7f000001
Octal:          017700000001

Full Hex:       0x7f.0x0.0x0.0x1
Full Oct:       0177.0.0.01

Random Padding:
Hex:    0x000000000007f.0x000000000000000000000000000000.0x0000.0x0000000000000000000000001
Oct:    00000000000000000000000177.000000000000000000.00000000000000000000000000000.000001

Random base:
#1:     0x7f.0x0.0.01
#2:     0x7f.0x0.0x0.1
#3:     0177.0x0.0x0.0x1
#4:     0x7f.0.0.01
#5:     127.0x0.0.0x1

Random base with random padding:
#1:     127.0x00000000.000000.000000000000000001
#2:     127.0x0000000000000.0x00000000000000000000000000000.0001
#3:     0000000000000000177.0x0000000000000000000000.0x00000000000000000000000000.1
#4:     0000000000000000000177.0.000000.1
#5:     127.0000000000000000000000.0x0000000000000000000.000000000000000000000000000001
```

## IPFuscator3

![](https://github.com/nu11secur1ty/IPFuscator/blob/master/docs/Screenshot%202022-09-15%20171819.png)

```
IPFuscator3
Author: Vincent Yiu (@vysecurity)
https://www.github.com/vysec/IPFuscator
Modded for Python3 (@nu11secur1ty)
https://github.com/nu11secur1ty/IPFuscator
Version: 0.1.4

IP Address:     127.0.0.1

Decimal:        2130706433
Hexadecimal:    0x7f000001
Octal:          0o17700000001

Full Hex:       0x7f.0x0.0x0.0x1
Full Oct:       0o177.0o0.0o0.0o1

Random Padding:
Hex:    0x0000000007f.0x00000000000000000000000000.0x000000000000000000.0x000000000000001
Oct:    00o177.000000000000000000000000o0.000000000000000000000000o0.000000o1

Random base:
#1:     127.0x0.0x0.0x1
#2:     0x7f.0o0.0o0.0o1
#3:     0x7f.0o0.0o0.1
#4:     127.0.0x0.0o1
#5:     0x7f.0x0.0o0.0o1

Random base with random padding:
#1:     000o177.0.0000000000000000000000000o0.1
#2:     0x000000000000000000000000000007f.000000000000000000000000o0.0x00000000000.000000000000000000o1
#3:     0x0000000000000000000007f.0x000000000000000000000000000000.0.0x0001
#4:     0x000000000000000000000007f.0.00000000000000o0.0000o1
#5:     0x0000000000000000007f.0000o0.0.1
```

3) Take any representation and use it in commands such as `ping`. You can also use it for a command and control endpoint.
