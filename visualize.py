# Copyright 2017: Raphael M. Reischuk
#
# 
# This script converts the lines of a text file to an HTML output, where
# each line gets an individual color and an individual position.
#
# Input text file:
inputfile = "input.txt"
# Output HTML file:
results = "results.html"
#
#
# Run this script from your shell:
#
#   while true; do python visualize.py; sleep 2; done
#
# and open the output file in your browser.
#
#
#
# You can specify a random input salt to produce a different output.
# This can be any string.
salt = "Zke MA-Tag 2017"
#
# You can specify a blacklist of lines that shall not be displayed:
blacklist = {"UPC Wi-Free","Free_Swisscom_Auto_Login","zOne","zLocal","znet","zred"}
#
# You can tune the HTML output:
HTMLfontsize = 35
HTMLrefreshinterval = 2

import os
import md5
import time

# Read input file.
f = open(inputfile, "r")
lines = [line for line in f if line.strip()]
f.close()

# Create HTML output file.
html = open(results, "w")
html.write("<html>\n  <head>\n    <style type='text/css'>\n")
html.write("      body {\n        font-family: sans-serif;\n      }\n")
html.write("      span {\n        position: absolute;\n        z-index: 1;\n        display: block;\n        padding: 2px;\n        padding-left: 6px;\n        padding-right: 6px;\n        font-size: %dpx;\n        border-radius: 8px;\n        background: linear-gradient(#ffffff,#dddddd);\n      }\n" % HTMLfontsize)
html.write("    </style>\n")
html.write("    <meta http-equiv='refresh' content='%d'>\n" % HTMLrefreshinterval)
html.write("  </head>\n\n")
html.write("  <body>\n\n")
html.write("    <img src='src/zke.png' style='z-index: 2;'>\n\n")

# Fetch current time.
curtime = (int)(time.time())

# Produce individual outputs.
for elem in set(lines):
  elem = elem.strip(' \t\n\r')
  if elem in blacklist: continue
  hashval = md5.new(elem + salt).hexdigest()
  hashnum = hashval.replace('a','').replace('b','').replace('c','').replace('d','').replace('e','').replace('f','')
  color = hashval[:6]
  movementX = (50 - (float)(hashnum[6:8])) / 400
  movementY = (50 - (float)(hashnum[8:10])) / 400
  posX = 0.95 * (((float)(hashnum[0:2]) + movementX * curtime) % 100)
  posY = 0.95 * (((float)(hashnum[2:4]) + movementY * curtime) % 100)
  rot = 0.05 * (int)(hashnum[4:6])
  html.write("<span style='color: #%s; left: %.2f%%; top: %.2f%%; transform: rotate(%ddeg); border: none #%s;'>%s</span>\n" % (color,posX,posY,rot,color,elem))


# Finalize HTML.
html.write("\n  </body>\n</html>\n")
html.close()

# Status message.
print "Successfully created file " + results + "."
