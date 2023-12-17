import sys, re

inputfile = sys.argv[1]
if inputfile == None:
    print("Input filepath is empty")
    sys.exit("Execution stopped.")
reg = "\\d+"
sortBy = None
if len(sys.argv) > 2:
    reg = sys.argv[2]
p = re.compile(reg)

if len(sys.argv) > 3:
    sortBy = sys.argv[3]

rfile = open(inputfile, "r", encoding="utf-8")
content = rfile.readlines()
rfile.close()
content = [line.strip() for line in content]


# content.sort(key=lambda l: int(re.findall('\d+', l)[3]))
def func(s):
    numlist = re.findall(reg, s)
    leng = len(numlist)
    if leng > 0:
        global sortBy
        if sortBy == None:
            sortBy = leng - 1
        return int(numlist[int(sortBy)])
    else:
        print(">>> reg length 0 " + reg + " " + s + str(re.match(p, s)))


content.sort(key=func)
print(content)
wfile = open(inputfile, "w", encoding="utf-8")
for i in content:
    wfile.write(i + "\n")
wfile.close()
