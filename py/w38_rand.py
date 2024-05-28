#!/usr/bin/python
print('Content-type: text/html\n')

import random


x = random.randrange(219,358)
new = " "
new += "President Trump will get "
new += str(x)
new += " Electoral Votes in November"
print(new)

