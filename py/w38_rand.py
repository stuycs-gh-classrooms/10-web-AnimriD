#!/usr/bin/python
print('Content-type: text/html\n')

import random
print("<head>")
print("""<meta charset="utf-8>""")
print("<title>w38_rand.py</title>")
print("\n")
print("<body>")

x = random.randrange(219,358)
new = " "
new += "President Trump will get "
new += str(x)
new += " Electoral Votes in November"
print("<p>" + new + "</p>")
print("</body>")
print("</head>")

