import os

server_path = '/home/louis/ROM/LA/out/target/product/gemini/obj/KERNEL_OBJ/../../../../../..'
local_path = '/home/louis/WORK/CM14/'
blacklist = ['qbam_probe'] # Fixed leaks not in built image (dma_async_device_register)

def getLine(string):
	return os.popen("addr2line -f -e vmlinux " + string[6:22]).read()

# Open files
tmp = open("kmemleak.txt","r")

# Write leaks
leaks = os.popen('grep "kmemleak" -n kmemleak.txt | cut -f1 -d:').readlines()

# Read leaks
data = tmp.readlines()
buf = []
for i in leaks:
	buf.append(data[int(i[:-1])+2])

# Filter and print
ret = list(set(buf))
for j in ret:
	if any(x in j for x in blacklist): continue
	print "*****************"
	print "DUMP = " + j[:-1]
	print "ADDR = " + (getLine(j)[:-1]).replace(server_path,local_path)
	print "*****************"

# Close
tmp.close()

