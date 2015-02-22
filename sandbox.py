import subprocess
import re

print "sandbox started!"

front = "Stereo Headphones FP"
rear = "Stereo Headphones"

proc = subprocess.Popen(["amixer sget \"Analog Output\""], shell = True, stdout=subprocess.PIPE)
for line in proc.stdout:
    if "Item0" in line:
        m = re.search("'(.*)'", line)
        if m.group(1) == front:
            print "FRONT !"
        elif m.group(1) == rear:
            print "REAR !"

