import sys, os

inputfile = sys.argv[1]
rfile = open(inputfile, "r")
content = rfile.readlines()
rfile.close()
content = [line.strip() for line in content]
for line in content:
    rline = line.strip().split("->")
    pre = rline[0].strip()
    now = rline[1].strip()
    os.rename(now, pre)
