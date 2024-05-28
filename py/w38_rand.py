#!/usr/bin/python
print('Content-type: text/html\n')

import random
print("<head>")
print("""<meta charset="utf-8>""")
print("<title>w38_rand.py</title>")
print("\n")
print("<body>")

x = random.randrange(219,358)
print("<p>")
new = " "
new += "President Trump will get "
new += str(x)
new += " Electoral Votes in November"
print(new)
print("</p>")
print("</body>")
print("</head>")

